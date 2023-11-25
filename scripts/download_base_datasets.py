"""
This module downloads various datasets from Kaggle and saves them locally.
"""

import os
import requests
from tqdm import tqdm
from kaggle.api.kaggle_api_extended import KaggleApi

def download_file(url, filename):
    """
    Downloads a file from the given URL and saves it to the specified filename.
    """
    with requests.get(url, stream=True, timeout=10) as r:  # Added timeout
        total_length = int(r.headers.get('content-length'))
        with open(filename, 'wb') as f:
            for chunk in tqdm(r.iter_content(chunk_size=1024), total=total_length//1024, unit='KB', desc=f'Downloading {filename}'):
                if chunk:
                    f.write(chunk)
if not os.path.exists('datasets'):
    os.makedirs('datasets')

# Kaggle datasets
kaggle_datasets = [
    "wcukierski/enron-email-dataset",
    "rtatman/fraudulent-email-corpus",
    "venky73/spam-mails-dataset",
    "subhajournal/phishingemails",
    "suraj520/customer-support-ticket-dataset",
    "ozlerhakan/spam-or-not-spam-dataset",
]

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Download Kaggle datasets
for dataset in kaggle_datasets:
    dataset_key = dataset.rsplit('/', maxsplit=1)[-1]
    dataset_path = f'datasets/{dataset_key}'
    if not os.path.exists(dataset_path):
        print(f'Trying to download {dataset_key}...')
        api.dataset_download_files(dataset, path='datasets', unzip=True, quiet=False)

print("Datasets downloaded and renamed successfully.")
