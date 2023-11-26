import os
import re
from concurrent.futures import ProcessPoolExecutor
import spacy
import pandas as pd
from tqdm.auto import tqdm
import matplotlib.pyplot as plt

# Load a spaCy model with NER, disabling unnecessary components
nlp = spacy.load('en_core_web_md', disable=['parser', 'tagger', 'lemmatizer'])

# Regex for email detection
email_regex = re.compile(r'\b\S+@\S+\.\S+\b')

# Function to process a batch of texts
def process_batch(batch):
    results = []
    for text in batch:
        if isinstance(text, str):
            # Split large texts into smaller parts if they exceed a certain length
            max_length = 1000000  # Set the max length for a part
            parts = [text[i:i + max_length] for i in range(0, len(text), max_length)]
            
            combined_cleaned_text = ""
            combined_improvement_score = 0
            for part in parts:
                original_length = len(part)
                part = re.sub(email_regex, '[EMAIL]', part)
                doc = nlp(part)
                pii_labels = {'PERSON', 'ORG', 'CARDINAL', 'GPE', 'LOC'}
                for ent in doc.ents:
                    if ent.label_ in pii_labels:
                        part = part.replace(ent.text, f'[{ent.label_}]')
                cleaned_length = len(part)
                combined_cleaned_text += part
                combined_improvement_score += (original_length - cleaned_length) / original_length if original_length > 0 else 0

            results.append((combined_cleaned_text, 1, combined_improvement_score / len(parts)))
        else:
            results.append((text, 0, 0.0))
    return results

def process_csv_in_chunks(file, chunksize=1000, batchsize=100):
    cleaned_file_path = file.replace('raw', 'processed').replace('.csv', '_cleaned.csv')
    replacements_tracker = []
    improvement_metric = []

    total_rows = pd.read_csv(file, usecols=['Email Text']).shape[0]
    total_chunks = (total_rows + chunksize - 1) // chunksize

    for chunk_number, chunk in enumerate(pd.read_csv(file, chunksize=chunksize)):
        desc = f"Processing Chunk {chunk_number+1}/{total_chunks}"
        replacements = 0
        improvement_score = 0.0

        updated_texts = []
        with tqdm(total=len(chunk), desc=desc, unit="rows") as pbar:
            batches = [chunk['Email Text'][i:i+batchsize] for i in range(0, len(chunk), batchsize)]
            with ProcessPoolExecutor() as executor:
                for batch_results in executor.map(process_batch, batches):
                    for text, repl, score in batch_results:
                        updated_texts.append(text)
                        replacements += repl
                        improvement_score += score
                    pbar.update(len(batch_results))

        replacements_tracker.append(replacements)
        improvement_metric.append(improvement_score / len(chunk) if len(chunk) > 0 else 0)

        chunk['Email Text'] = updated_texts
        mode = 'w' if chunk_number == 0 else 'a'
        header = mode == 'w'
        chunk.to_csv(cleaned_file_path, index=False, mode=mode, header=header)

    return pd.DataFrame({
        'chunk_index': range(len(replacements_tracker)),
        'replacements': replacements_tracker,
        'improvement_score': improvement_metric
    })

# Main execution block
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, '..', '..', 'data', 'raw', 'Phishing_Email.csv')

    chunk_size = 1000  # Adjust as needed
    batch_size = 100  # Adjust the batch size as needed

    replacements_df = process_csv_in_chunks(file_path, chunk_size, batch_size)

    # Plotting the results
    fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()
    ax1.bar(replacements_df['chunk_index'], replacements_df['replacements'], color='g')
    ax2.plot(replacements_df['chunk_index'], replacements_df['improvement_score'], color='b')

    ax1.set_xlabel('Chunk Index')
    ax1.set_ylabel('Number of Replacements', color='g')
    ax2.set_ylabel('Average Improvement Score', color='b')

    plt.title('PII Replacements and Improvement Score per Chunk')
    plt.savefig(os.path.join(script_dir, '..', '..', 'docs', 'replacements_and_improvement_chart.png'))
    plt.show()
