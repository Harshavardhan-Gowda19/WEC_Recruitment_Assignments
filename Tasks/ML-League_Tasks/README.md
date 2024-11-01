---

# ML-League Assignment 1: Loan Repayment Prediction Model

## Overview

In this project, I built a model to predict whether someone is likely to repay a loan. The prediction is based on key characteristics like gender, age, and annual income to understand who’s more likely to keep up with loan payments.

### Key Features

- **Demographics**: By looking at gender and age, I explored any patterns that might affect loan repayment.
- **Income**: Annual income is essential since it reflects a person's financial stability, which is linked to their ability to repay loans.
- **Credit Scores**: I included three key score features (*source_score_1*, *source_score_2*, and *source_score_3*). These work similarly to credit scores, giving insights into the likelihood of repayment. They turned out to be very useful in identifying higher-risk individuals.

### Model and Results

Using a **Support Vector Machine (SVM)** model, I achieved a strong accuracy of **96%**. This accuracy highlights how important the credit score columns are, acting much like a bank’s CIBIL score to predict loan repayment.

---

# ML-League Assignment 2: Malware Detection Model

## Overview

This project focuses on creating a model to detect malware, but there’s a challenge: the dataset is highly imbalanced, with far fewer examples of malware than non-malware, making it tough for the model to perform well.

### Dataset and Challenges

The imbalance means the model finds it hard to detect malware accurately, as it’s trained on a lot more examples of non-malware than malware. This imbalance often results in lower accuracy.

### Model and Approach

To keep things simple, I built a straightforward model that focuses on efficiency. I tried techniques like adjusting class weights and resampling to handle the imbalance, but accuracy stayed between **20% and 26%**. This was a learning experience in how class imbalance affects model performance.

---

# ML-League Assignment 3: Multi-Class Classification with CNN

## Overview

This project uses a Convolutional Neural Network (CNN) to classify images into **9 different classes**. The model performed well on the training set, achieving **98% accuracy**, but struggled with the validation set, where accuracy dropped to **60%**.

### Model and Challenges

The model is quite complex to capture detailed patterns in the data, but this complexity may have caused overfitting, as shown by the gap between training and validation accuracy. Unfortunately, I didn’t have time to reduce the complexity, but this is definitely something to focus on for future improvement.

---
