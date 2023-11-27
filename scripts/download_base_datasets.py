"""
This script downloads various datasets from Kaggle and saves them in the 'data/raw' directory.
"""

import os
from tqdm import tqdm
from kaggle.api.kaggle_api_extended import KaggleApi

# Kaggle datasets
kaggle_datasets = [
    "wcukierski/enron-email-dataset",
    "rtatman/fraudulent-email-corpus",
    "subhajournal/phishingemails",
    "suraj520/customer-support-ticket-dataset",
    "ozlerhakan/spam-or-not-spam-dataset",
]

# Function to initialize Kaggle API
def initialize_kaggle_api():
    api_instance = KaggleApi()
    api_instance.authenticate()
    return api_instance

# Function to download datasets from Kaggle and extract them
def download_and_extract_dataset(api_instance, dataset_identifier, path='data/raw'):
    dataset_key = dataset_identifier.split('/')[-1]
    dataset_path = f'{path}/{dataset_key}'

    if not os.path.exists(dataset_path):
        api_instance.dataset_download_files(dataset_identifier, path=path, unzip=True)
        tqdm.write(f'Dataset {dataset_key} downloaded and extracted in {path}.')
    else:
        tqdm.write(f'Dataset {dataset_key} already exists in {path}.')

if __name__ == "__main__":
    # Initialize Kaggle API
    api = initialize_kaggle_api()

    # Create 'data/raw' directory if it doesn't exist
    if not os.path.exists('data/raw'):
        os.makedirs('data/raw')

    # Download Kaggle datasets
    with tqdm(total=len(kaggle_datasets), desc='Downloading datasets') as pbar:
        for dataset in kaggle_datasets:
            download_and_extract_dataset(api, dataset)
            pbar.update(1)

    print("All datasets have been downloaded and extracted successfully.")
