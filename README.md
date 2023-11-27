# 🐟 PhishNet

![PhishNet Art](/assets/phishnet-art-base.png)

**DISCLAIMER**: *The content provided by **PhishNet** is exclusively for educational and research purposes **ONLY**. The training data for the models under **PhishNet** umbrella; have been carefully cleaned to remove any **sensitive** or **personally identifiable information (PII)** to ensure ethical compliance and privacy. The views and opinions expressed are solely those of the authors and do not reflect any associated organizations. No warranty is provided regarding the accuracy or reliability of the information. Usage of **PhishNet** and its outputs is at your own risk, with no liability for any resultant damages. This project does not endorse illegal activities and should be used responsibly.*

## TL;DR

**PhishNet** is a research project utilizing **Reinforced Self-Training (ReST)** and fine-tuned set of **Large Language Models (LLMs)** to create a high-quality synthetic dataset of phishing emails. Trained on various valuable email datasets (see [citations](#citations)), this project aims to dive into the exploration of adversarial AI and expand our understanding of AI safety.

## Table Of Content

- [Disclaimer](#disclaimer)
- [TL;DR](#tldr)
- [Methodology](#methodology)
  - [Data Collection](#data-collection)
  - [Model Training](#model-training)
  - [Data Generation](#data-generation)
<!-- - [Hugging Face Space](#hugging-face-space)
- [Hugging Face Configuration](#hugging-face-configuration)
- [How to Use in Hugging Face Spaces](#how-to-use-in-hugging-face-spaces) -->
- [Local Installation & Usage](#local-installation--usage)
- [Results and Evaluation](#results-and-evaluation)
- [Citations](#citations)
- [License](#license)

## Methodology

- **Data Collection**: Various datasets such as Enron Email Dataset, Spam Mails Database, etc.
- **Model Training**: Using various LLMs with Reinforced Self-Training.
- **Data Generation**: Synthesizing phishing emails for research.

## Local Installation & Usage

If you prefer to run PhishNet locally:

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the model with your input data.

## Results and Evaluation

This section is under development and will be updated soon.

## Citations

- Radford, A., Wu, J., Child, R., et al. (2019). Language Models are Unsupervised Multitask Learners. [Link](https://github.com/openai/gpt-2)

```
@article{radford2019language,
  title={Language Models are Unsupervised Multitask Learners},
  author={Radford, Alec and Wu, Jeff and Child, Rewon and Luan, David and Amodei, Dario and Sutskever, Ilya},
  year={2019}
}
```

- Gulcehre, C., Le Paine, T., Srinivasan, S., et al. (2023). Reinforced Self-Training (ReST) for Language Modeling. arXiv preprint arXiv:2308.08998. [Link](https://arxiv.org/abs/2308.08998)

```
@misc{gulcehre2023reinforced,
      title={Reinforced Self-Training (ReST) for Language Modeling}, 
      author={Caglar Gulcehre and Tom Le Paine and Srivatsan Srinivasan and Ksenia Konyushkova and Lotte Weerts and Abhishek Sharma and Aditya Siddhant and Alex Ahern and Miaosen Wang and Chenjie Gu and Wolfgang Macherey and Arnaud Doucet and Orhan Firat and Nando de Freitas},
      year={2023},
      eprint={2308.08998},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

- The Enron Email Dataset. Kaggle. [Link](https://www.kaggle.com/datasets/wcukierski/enron-email-dataset)
- Phishing Email Detection. Kaggle. [Link](https://www.kaggle.com/datasets/subhajournal/phishingemails)
- Customer Support Ticket Dataset. Kaggle [Link](https://www.kaggle.com/datasets/suraj520/customer-support-ticket-dataset)
- Spam or Not Spam Dataset. Kaggle [Link](https://www.kaggle.com/datasets/ozlerhakan/spam-or-not-spam-dataset)

## License

**PhishNet** is released under the **MIT** License. The full text of the license can be found via [LICENSE.md](LICENSE).
