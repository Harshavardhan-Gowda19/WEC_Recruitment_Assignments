ML-LEAGUE Assignments:
---

# ML-League_Assignment-1

## Loan Repayment Prediction Model

In this project, I developed a model to predict the likelihood of loan repayment by assessing critical features like gender, age, and annual income. Using these features as a foundation, I analyzed the data to better understand the characteristics of individuals more likely to fulfill their repayment obligations.

### Key Features

- **Demographic Attributes**: Gender and age were analyzed to identify trends related to repayment patterns, providing initial insights into borrower profiles.
- **Income Levels**: Annual income plays a significant role in repayment capabilities, as it is directly correlated to financial stability.
- **Credit Scores**: The model incorporates three crucial features, *source_score_1*, *source_score_2*, and *source_score_3*, which function similarly to traditional credit scores. These scores serve as core indicators for evaluating a candidate’s repayment likelihood and proved essential in distinguishing high-risk individuals.

### Model and Performance

The model is built using a **Support Vector Machine (SVM)**, which achieved a commendable accuracy of **96%**. This strong performance underscores the model's effectiveness in assessing loan repayment probability based on selected features. The breakthrough came with the inclusion of the *source_score* columns, which provided critical insights akin to CIBIL scores used by banks to gauge creditworthiness.

---
# ML-League_Assignment-2

## Malware Detection Model

This project involves building a classification model aimed at detecting malware, leveraging a dataset that unfortunately exhibits significant class imbalance. Due to this imbalance, achieving high accuracy presented challenges, with the model’s accuracy ranging between **20% and 26%** despite various attempts to improve performance.

### Dataset and Challenges

The dataset used for malware detection reflects a stark imbalance in class representation, which is common in real-world cybersecurity scenarios. Such imbalance can make it difficult for the model to accurately identify minority classes, leading to lower overall accuracy.

### Model and Approach

The model architecture here is simpler than others, focusing on efficiency while managing the limitations posed by the data. Various techniques, including resampling methods and class weights, were explored to mitigate the impact of imbalance, yet accuracy gains were constrained within a 20-26% range.

---
Here's an enhanced README description for Assignment 3:

---

# ML-League_Assignment-3

## CNN Classification Model for Multi-Class Classification

This project involves building a Convolutional Neural Network (CNN) to classify data into **9 distinct classes**. While the model achieved an impressive **98% accuracy** on the training dataset, its performance on the validation dataset hovered around **60%**, suggesting a potential issue with overfitting.

### Model Architecture and Challenges

The model was initially designed with a complex architecture to enhance its ability to learn intricate patterns within the data. However, this complexity likely contributed to overfitting, as evidenced by the substantial accuracy gap between training and validation sets. Given time constraints, reducing the model’s complexity wasn't feasible within this project phase, but it stands as a key area for future improvement.

---
