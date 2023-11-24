# 🐟 PhishNet

![PhishNet Art](https://github.com/sirlolcat/PhishNet/assets/85698684/1cc320ce-3878-4cb0-b2fd-c6c757dd82af)

***DISCLAIMER:** The content provided by **PhishNet** is exclusively for educational and research purposes **ONLY**. The views and opinions expressed are solely those of the authors and do not reflect any associated organizations. No warranty is provided regarding the accuracy or reliability of the information. Usage of **PhishNet** and its outputs is at your own risk, with no liability for any resultant damages. I believe in the saying 'Sun is the best disinfectant,' my aim is to delve into adversarial AI to promote a safer future. This project does not endorse illegal activities and should be used responsibly.*

## TL;DR
**PhishNet** is a research project utilizing **Reinforced Self-Training (ReST)** and **GPT-2** to create a high-quality synthetic dataset of phishing emails. Trained on various valuable email datasets (see citations), this project aims to dive into the exploration of adversarial AI and expand our understanding of AI safety.

## Citations
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
- Radford, A., Wu, J., Child, R., et al. (2019). Language Models are Unsupervised Multitask Learners. [Link](https://github.com/openai/gpt-2)
```
@article{radford2019language,
  title={Language Models are Unsupervised Multitask Learners},
  author={Radford, Alec and Wu, Jeff and Child, Rewon and Luan, David and Amodei, Dario and Sutskever, Ilya},
  year={2019}
}
```
- The Enron Email Dataset. Carnegie Mellon University. [Link](https://www.cs.cmu.edu/~enron/)
- Fraudulent Email Corpus. Kaggle. [Link](https://www.kaggle.com/datasets/rtatman/fraudulent-email-corpus)
- Spam Mails Database. Kaggle. [Link](https://www.kaggle.com/datasets/venky73/spam-mails-dataset)
- Phishing Email Detection. Kaggle. [Link](https://www.kaggle.com/datasets/subhajournal/phishingemails)

## Table Of Content
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Methodology](#methodology)
  - [Data Collection](#data-collection)
  - [Model Training](#model-training)
  - [Data Generation](#data-generation)
- [Results and Evaluation](#results-and-evaluation)
- [Contributing](#contributing)
- [License](#license)
