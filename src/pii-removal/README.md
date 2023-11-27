# 🛡️ PhishNet - PII Removal / Privacy Compliance

![PhishNet Art](/assets/phishnet-art-pii-removal.png)

## Table of Contents

- [Introduction](#introduction)
- [Objective](#objective)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Results and Methodological Approach](#results-and-methodological-approach)
  - [Quantitative Metrics](#quantitative-metrics)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)
- [License](#license)

## Introduction

As part of our commitment to ethical AI research and development, this module is dedicated to the meticulous removal of any private, sensitive, or personally identifiable information (PII) from our datasets. Ensuring privacy and compliance is paramount in our quest to create a high-quality synthetic dataset of phishing emails.

## Objective

Our primary goal is to pre-process and sanitize the datasets used in **PhishNet** training, effectively stripping out all **PII** and **sensitive** information. This process, conducted on **T4** GPUs, is crucial in maintaining the integrity of our research and upholding our ethical standards. We ensure that our model is **NEVER** trained on `raw` datasets, only on data that has been thoroughly sanitized for PII (`processed`).

## How It Works

- **Automated Detection**: Utilizing Named-Entity Recognition (**NER**), this tool automatically identifies potential PII in raw datasets under `data/raw`. (PII is defined as: `EMAIL`, `PERSON`, `ORG`, `CARDINAL`, `GPE`, `LOC`)
- **Removal Process**: Once detected, PII is obfuscated or anonymized to ensure no sensitive information is retained.
- **Quality Assurance**: Post-processing checks are conducted to verify the thoroughness of PII removal.

## Usage

1. **Preparation**: Ensure that raw datasets are placed in the `data/raw` directory.
2. **Execution**: Run the PII Removal script by executing `python3 pii-removal.py` directly.
3. **Output**: Processed datasets, free from PII, are saved in `data/processed`.

## Technologies Used

- **NLP Library**: [Spacy](https://spacy.io/)
- **Programming Language**: [Python 3.10](https://www.python.org/downloads)
- **Regular Expressions**: [re](https://docs.python.org/3/library/re.html)

## Results and Methodological Approach

The process of PII removal for each raw dataset is encapsulated respectively in charts named `<dataset>_replacements_and_improvement_chart.png`, found in the `docs/pii-removal` directory. Instances of this chart illustrate both the quantity of PII entities removed (represented by the green bars) and the relative improvement in privacy (depicted by the blue line) for each chunk of data processed.

### Quantitative Metrics

- **Number of Replacements**: Indicates the count of PII entities detected and removed per chunk, providing a direct measure of the tool's activity.
- **Improvement Score**: A normalized measure indicating the proportion of text altered due to PII removal. It is calculated as the ratio of the number of characters removed to the total characters in the chunk, providing a standardized metric for comparing privacy enhancement across chunks.

For a comprehensive explanation of the chart and its significance in the context of privacy enhancement, please refer to the README in the `docs/pii-removal` folder.

## Contributing

We appreciate contributions from the community! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## Disclaimer

*The PII Removal tool is a part of the **PhishNet** project, which is intended strictly for educational and research purposes **ONLY**. While we strive for accuracy, we offer no warranty regarding the completeness of PII removal. Usage is at your own risk.*

## License

This PII Removal module, like the rest of the **PhishNet** project, is released under the [MIT License](LICENSE).
