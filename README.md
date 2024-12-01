# **Computer Systems Security Project -- Group 11**  

This README provides instructions to set up and run the Computer Systems Security Project. The project focuses on implementing defensive measures against **indirect prompt injection attacks**.

---

## **Prerequisites**  

- **Python**: Ensure **Python 3.11.5** is installed on your system.  
  [Download Python 3.11.5](https://www.python.org/downloads/release/python-3115/).  

---

## **Installation**  

### 1. Clone the Repository  
```bash
git clone https://github.com/kathaleeend1000/Computer-Systems-Security-Project-.git
```

### 2. Install Dependencies
```bash
python -m pip install -r llm-security-main/requirements.txt
```

---

## **Model Training (for Scenario 2)**  

The trained model is too large to be included in the repository. Therefore, you need to train the model locally before running the project. Follow these steps: 

### 1. Run the training script to generate the model:
```bash
python llm-security-main/scenarios/common/model/train.py
```

---

## **Running the Project**  
After installing the dependencies and training the model, you can explore various scenarios and functionalities of the project.

The final version includes a Logistic Regression-based classifier in the second scenario, trained with embeddings from a Sentence Transformer, to identify malicious injection attempts in a syntetic external website. The application supports dynamic analysis of website content triggering scenario failures when injections are detected. The model is trained to distinguish between safe and injection-prone text with high sensitivity and allows customizable thresholds for classification. The detection framework works effectively for the provided datasets and predefined scenarios, but it may require further tuning or retraining for more complex injection patterns using larger dataset.

---

## **Citation**  

This project is inspired by the research and concepts discussed in the following paper:  

```bibtex
@misc{https://doi.org/10.48550/arxiv.2302.12173,
  doi = {10.48550/ARXIV.2302.12173},
  url = {https://arxiv.org/abs/2302.12173},
  author = {Greshake, Kai and Abdelnabi, Sahar and Mishra, Shailesh and Endres, Christoph and Holz, Thorsten and Fritz, Mario},
  keywords = {Cryptography and Security (cs.CR), Artificial Intelligence (cs.AI), Computation and Language (cs.CL), Computers and Society (cs.CY), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {More than you've asked for: A Comprehensive Analysis of Novel Prompt Injection Threats to Application-Integrated Large Language Models},
  publisher = {arXiv},
  year = {2023},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
