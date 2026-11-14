# CTF Writeup: Perceptron – XNOR Classification

## 1. Challenge Overview

- **Challenge Name:** Perceptron – XNOR Classification
- **Category:** Machine Learning / AI
- **Difficulty:** Not specified
- **Target:** `http://chatelaine.cylabacademy.net:15403/`
- **Objective:** Train a single perceptron on XNOR data and achieve the required 75% accuracy to reveal the flag.

### Challenge Description

The challenge provides an interactive perceptron learning environment using XNOR data.

The objective is to observe how a perceptron learns through the classic perceptron update rule. Only misclassified points trigger weight updates, and no weight decay is applied.

Since XNOR is not linearly separable, a single perceptron cannot achieve 100% accuracy. The required target is 75%.

---

## 2. Concepts Involved

### What is a Perceptron?

A perceptron is a simple binary classification algorithm that takes input features, multiplies them by corresponding weights, adds a bias, and produces a prediction.

The mathematical representation is:

\[
z=w_1x_1+w_2x_2+b
\]

The prediction is determined using a threshold function:

\[
\hat{y} =
\begin{cases}
1 & z\geq 0\\
0 & z<0
\end{cases}
\]

Where:
- \(x_1,x_2\): Input features.
- \(w_1,w_2\): Weights.
- \(b\): Bias.
- \(\hat y\): Predicted output.

### Understanding XNOR

XNOR is a Boolean logical operation that produces 1 when both inputs are equal and 0 when they are different.

| Input 1 | Input 2 | XNOR Output |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

The important property of XNOR is that it is not linearly separable.

A single perceptron can only create a linear decision boundary. It cannot correctly classify all four XNOR combinations using one straight line.

Therefore, 100% accuracy is impossible for a single perceptron on this dataset.

---

## 3. Approach and Methodology

### Step 1: Accessing the Instance

Opened the challenge URL in the browser:

`http://chatelaine.cylabacademy.net:15403/`

The application displayed:
- An interactive XNOR classification graph.
- A learning-rate control.
- A Run Training button.
- A training log showing predictions, errors, weights, bias, and accuracy.
- A status panel displaying the final accuracy and flag.

### Step 2: Understanding the Training Process

The challenge uses the classic perceptron learning rule.

The weight update equation is:

\[
w_i^{new}=w_i^{old}+\eta(y-\hat y)x_i
\]

The bias update is:

\[
b^{new}=b^{old}+\eta(y-\hat y)
\]

Where:
- \(\eta\) is the learning rate.
- \(y\) is the actual output.
- \(\hat y\) is the predicted output.
- \(x_i\) is the input feature.

An update occurs only when the prediction is incorrect.

### Step 3: Observing the Training Log

The learning rate was set to 4.75.

The application recorded the following updates:

| Step | Sample | Prediction | Error | W1 | W2 | Bias | Accuracy |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | (-2,-2) → 1 | 0 | 1 | -8.50 | -8.50 | 4.75 | 25% |
| 2 | (2,2) → 1 | 0 | 1 | 1.00 | 1.00 | 9.50 | 50% |
| 3 | (-2,2) → 0 | 1 | -1 | 10.50 | -8.50 | 4.75 | 75% |

Each misclassified sample triggered an update to the weights and bias.

### Step 4: Reaching the Target Accuracy

After the third update, the application displayed:

- Training progress: 3/16
- Final accuracy: 75.0%
- Target accuracy: 75%

The status panel confirmed that the required accuracy had been achieved.

The application then revealed the challenge flag.

---

## 4. Why 75% Is the Maximum Target

A single perceptron generates a linear decision boundary.

However, the XNOR dataset has two positive points at opposite corners and two negative points at the remaining corners.

These classes cannot be separated perfectly using a single straight line.

Consequently, at least one of the four points must be misclassified.

\[
Accuracy=\frac{3}{4}\times100=75\%
\]

This demonstrates an important limitation of single-layer perceptrons.

A multilayer neural network with hidden neurons can learn XNOR because it can construct nonlinear decision boundaries.

---

## 5. Flag

**Flag obtained:**

`academy{xnor_unl34rn4bl3_by_p3rc3ptr0ns_a0ea474c}`

---

## 6. Key Takeaways

Through this challenge, I explored:

1. The fundamentals of perceptrons and binary classification.
2. The classic perceptron learning and weight update rule.
3. How prediction errors influence weights and bias.
4. Linear separability and its importance in classification.
5. Why a single-layer perceptron cannot perfectly classify XOR/XNOR datasets.
6. The importance of hidden layers in overcoming