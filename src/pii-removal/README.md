# 🛡️ PhishNet - PII Removal / Privacy Compliance

![pii-removal](https://github.com/sirlolcat/PhishNet/assets/85698684/279c7efc-b716-4122-bed7-13a6577df4d9)


## Introduction

As part of our commitment to ethical AI research and development, this module is dedicated to the meticulous removal of any private, sensitive or personally identifiable information (PII) from our datasets. Ensuring privacy and compliance is paramount in our quest to create a high-quality synthetic dataset of phishing emails.

## Objective

Our primary goal is to pre-process and sanitize the datasets used in **PhishNet** training, effectively stripping out all **PII** and **sensitive** information. This process is crucial in maintaining the integrity of our research and upholding our ethical standards.

## How It Works

- **Automated Detection**: Utilizing advanced NLP techniques, this tool automatically identifies and flags potential PII in raw datasets under `data/raw`.
- **Removal Process**: Once detected, PII is removed or anonymized to ensure no sensitive information is retained.
- **Quality Assurance**: Post-processing checks are conducted to verify the thoroughness of PII removal.

## Usage

1. **Preparation**: Ensure that raw datasets are placed in the `data/raw` directory.
2. **Execution**: Run the PII Removal script by executing `python3 pii-removal.py` directory.
3. **Output**: Processed datasets, free from PII, are saved in `data/processed`.

## Technologies Used

- **NLP Libraries**: [Spacy](https://spacy.io/).
- **Programming Language**: Python 3.10.

## Contributing

We appreciate contributions from the community! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## Disclaimer

*The PII Removal tool is a part of the **PhishNet** project, which is intended strictly for educational and research purposes **ONLY**. While we strive for accuracy, we offer no warranty regarding the completeness of PII removal. Usage is at your own risk.*

## License

This PII Removal module, like the rest of the **PhishNet** project, is released under the [MIT License](LICENSE).
