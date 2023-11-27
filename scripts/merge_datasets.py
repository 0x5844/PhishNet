import os
import pandas as pd

def merge_datasets(raw_data_dir, processed_data_dir, output_filename):
    # Define the path for raw and processed data directories
    raw_data_path = os.path.join(raw_data_dir)
    processed_data_path = os.path.join(processed_data_dir)

    # Ensure the processed data directory exists
    if not os.path.exists(processed_data_path):
        os.makedirs(processed_data_path)

    # List of dataset filenames in the raw data directory
    dataset_filenames = [f for f in os.listdir(raw_data_path) if os.path.isfile(os.path.join(raw_data_path, f))]

    # Initialize an empty DataFrame to append data
    combined_df = pd.DataFrame()

    # Read and append all datasets into one DataFrame
    for filename in dataset_filenames:
        file_path = os.path.join(raw_data_path, filename)
        # Read the CSV file and append it
        if filename.endswith('.csv'):
            df = pd.read_csv(file_path)
            combined_df = combined_df._append(df, ignore_index=True)
        elif filename.endswith('.txt'):  # Assuming the .txt file is in a readable format
            df = pd.read_csv(file_path, sep='\t')
            combined_df = combined_df._append(df, ignore_index=True)

    # Save the combined data to a new CSV file in the processed data directory
    combined_df.to_csv(os.path.join(processed_data_path, output_filename), index=False)
    print(f"Combined dataset saved to {os.path.join(processed_data_path, output_filename)}")

if __name__ == "__main__":
    RAW_DATA_DIR = 'data/raw'
    PROCESSED_DATA_DIR = 'data/processed'
    OUTPUT_FILENAME = 'combined_dataset.csv'

    merge_datasets(RAW_DATA_DIR, PROCESSED_DATA_DIR, OUTPUT_FILENAME)
