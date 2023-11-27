import os
import re
import spacy
import pandas as pd
from tqdm.auto import tqdm
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor

# Constants and configurations
NLP_MODEL = 'en_core_web_md'
PII_LABELS = {'PERSON', 'ORG', 'CARDINAL', 'GPE', 'LOC'}
EMAIL_REGEX = re.compile(r'\b\S+@\S+\.\S+\b')
MAX_LENGTH = 2000000

# Initialize spaCy model with configurations
def init_spacy_model():
    nlp = spacy.load(NLP_MODEL, disable=['parser', 'tagger', 'lemmatizer'])
    nlp.max_length = MAX_LENGTH
    return nlp

nlp = init_spacy_model()

# Function to remove PII using regex and NER
def remove_pii(text, nlp):
    text = re.sub(EMAIL_REGEX, '[EMAIL]', text)
    doc = nlp(text)
    replacements_count = 0
    for ent in doc.ents:
        if ent.label_ in PII_LABELS:
            text = text.replace(ent.text, f'[{ent.label_}]')
            replacements_count += 1
    return text, replacements_count

# Process a single row of data
def process_row(row, text_columns, nlp):
    row_replacements = 0
    for col in text_columns:
        text = row[col]
        if isinstance(text, str):
            cleaned_text, replacements = remove_pii(text, nlp)
            row[col] = cleaned_text
            row_replacements += replacements
    return row, row_replacements

# Apply PII removal to a chunk of data
def process_chunk(chunk, text_columns, nlp):
    chunk_replacements = 0
    for i, row in chunk.iterrows():
        processed_row, row_replacements = process_row(row, text_columns, nlp)
        chunk.iloc[i] = processed_row
        chunk_replacements += row_replacements
    return chunk, chunk_replacements

# Parallel processing of chunks
def parallel_process_chunks(chunks, text_columns, nlp):
    processed_chunks = []
    replacements_tracker = []
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_chunk, chunk, text_columns, nlp) for chunk in chunks]
        for future in tqdm(futures, total=len(futures), desc="Processing Chunks"):
            processed_chunk, chunk_replacements = future.result()
            processed_chunks.append(processed_chunk)
            replacements_tracker.append(chunk_replacements)
    return processed_chunks, replacements_tracker

# Calculate improvement score based on replacements
def calculate_improvement_score(replacements_tracker, data_length):
    total_replacements = sum(replacements_tracker)
    return total_replacements / (data_length * MAX_LENGTH)

# Process the CSV in chunks and apply PII removal
def process_csv_in_chunks(file_path, chunksize=1000):
    # Get text columns to process
    sample_df = pd.read_csv(file_path, nrows=0)
    text_columns = sample_df.select_dtypes(include=['object']).columns.tolist()
    
    # Read the dataset in chunks
    chunks = [chunk for chunk in pd.read_csv(file_path, chunksize=chunksize)]
    cleaned_file_path = file_path.replace('.csv', '_cleaned.csv')

    # Process chunks in parallel
    processed_chunks, replacements_tracker = parallel_process_chunks(chunks, text_columns, nlp)
    
    # Calculate the improvement score
    improvement_score = calculate_improvement_score(replacements_tracker, len(chunks))

    # Write processed data back to a cleaned CSV
    for i, processed_chunk in enumerate(processed_chunks):
        mode = 'w' if i == 0 else 'a'
        header = True if i == 0 else False
        processed_chunk.to_csv(cleaned_file_path, index=False, mode=mode, header=header)
    
    return replacements_tracker, improvement_score

# Main execution block
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(script_dir, '..', '..', 'data', 'processed')
    file_name = 'combined_dataset.csv'
    file_path = os.path.join(data_dir, file_name)

    replacements_tracker, improvement_score = process_csv_in_chunks(file_path, chunksize=3000)

    # Plotting the results
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.bar(range(len(replacements_tracker)), replacements_tracker, color='g')
    ax2.plot(range(len(replacements_tracker)), [improvement_score] * len(replacements_tracker), color='b', linestyle='--')
    ax1.set_xlabel('Chunk Index')
    ax1.set_ylabel('Number of Replacements', color='g')
    ax2.set_ylabel('Improvement Score', color='b')
    plt.title('PII Replacements and Improvement Score per Chunk')
    plt.savefig(os.path.join(script_dir, '..', '..', 'docs', 'replacements_chart.png'))
    plt.show()
