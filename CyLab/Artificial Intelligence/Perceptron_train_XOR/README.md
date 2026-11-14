# Perceptron Training on XOR Data

## Overview

This exercise demonstrates how a single-layer perceptron learns from XOR-style data using the classic perceptron learning rule.

The objective was to tune the learning rate and observe the training process until the model achieved the required **75% accuracy**.

The exercise highlights an important limitation of a single perceptron: XOR data is not linearly separable, so a single linear decision boundary cannot classify all four points correctly.

## Objective

- Understand how a perceptron learns using weighted inputs.
- Observe how misclassified samples trigger weight updates.
- Experiment with the learning rate.
- Understand linear separability through the XOR problem.
- Achieve the target accuracy of 75%.

## Concepts Learned

### 1. Perceptron

A perceptron is a basic binary classification model that takes input features, multiplies them by weights, adds a bias, and produces a prediction.

Its weighted sum can be represented as:

\[
z = w_1x_1 + w_2x_2 + b
\]

The prediction is determined by applying a threshold activation function.

### 2. XOR and Linear Separability

XOR (Exclusive OR) produces an output of 1 when its two inputs differ and 0 when they are the same.

| Input 1 | Input 2 | Output |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

A dataset is linearly separable when a single straight line can divide its classes without misclassification.

XOR is not linearly separable. No single straight decision boundary can correctly classify all four data points.

### 3. Perceptron Learning Rule

The classic perceptron update rule is:

\[
w_i \leftarrow w_i + \eta(y-\hat{y})x_i
\]

Where:

- \(w_i\): Weight associated with an input feature.
- \(\eta\): Learning rate.
- \(y\): Actual output.
- \(\hat{y}\): Predicted output.
- \(x_i\): Input feature.

The model updates its weights when a sample is misclassified. Correctly classified samples do not trigger updates.

## Experiment and Observations

The learning rate was set to **1.75**.

The training interface displayed the following updates:

| Step | Sample | Actual Output | Prediction | Error |
|---|---|---:|---:|---:|
| 1 | (-2, -2) | 0 | 1 | -1 |
| 2 | (2, 2) | 0 | 1 | -1 |

Both samples were misclassified, triggering weight updates.

After the second update, the displayed parameters were:

| Parameter | Value |
|---|---:|
| Learning rate | 1.75 |
| \(w_1\) | 1.00 |
| \(w_2\) | -1.00 |
| Bias | -3.50 |

The final accuracy reached **75%**, satisfying the exercise's success condition.

## Key Observations

1. A perceptron adjusts its weights when it encounters misclassified samples.
2. The learning rate controls the magnitude of weight updates.
3. A linear classifier is restricted to a straight decision boundary.
4. XOR cannot be perfectly classified using a single-layer perceptron.
5. Increasing the learning rate cannot overcome a limitation caused by the model's architecture.

## Why 75% Accuracy?

The XOR dataset requires a nonlinear decision boundary to classify every point correctly.

A single-layer perceptron can only learn a linear decision boundary. Therefore, it cannot achieve 100% accuracy on the XOR dataset.

The 75% target demonstrates this architectural limitation rather than a failure to train the model properly.

More complex architectures, such as multilayer perceptrons with nonlinear activation functions, can learn the XOR relationship.

## Key Takeaway

This exercise helped demonstrate the difference between a model's learning process and its architectural capabilities.

Training adjustments can improve a model's performance, but they cannot always overcome fundamental limitations in the model itself.

Understanding linear separability is essential when choosing an appropriate machine learning architecture for a classification problem.

## Flag

`academy{x0r_unl34rn4bl3_by_p3rc3pt0r0ns_d7c0c598}`