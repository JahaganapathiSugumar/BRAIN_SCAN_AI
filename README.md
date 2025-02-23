# Brain Scan AI - Brain Tumor Detection

## Overview
Brain Scan AI is a deep learning-based model designed to classify MRI brain scans into two categories: **normal (no tumor)** and **tumor-affected (yes tumor)**. This project leverages Convolutional Neural Networks (CNNs) to analyze medical images and provide accurate predictions, assisting in early detection and diagnosis of brain tumors.

## Features
- **Brain Tumor Classification:** Identifies whether a given brain scan has a tumor or not.
- **Deep Learning Model:** Utilizes a Convolutional Neural Network (CNN) for classification.
- **Image Preprocessing:** Uses OpenCV and PIL for resizing and processing MRI scan images.
- **Train-Test Splitting:** Efficiently splits the dataset for training and evaluation.
- **Performance Metrics:** Evaluates model accuracy using test data and visualizes results.

## Dataset
The dataset consists of MRI brain scans categorized as:
- **Normal (No Tumor)** - Stored in the `dataset/no/` folder.
- **Tumor-affected (Yes Tumor)** - Stored in the `dataset/yes/` folder.

## Model Architecture
- **Input:** Preprocessed MRI scan images
- **Hidden Layers:** Convolutional, Pooling, Fully Connected layers
- **Output:** Binary classification (Normal/Tumor)
- **Loss Function:** Sparse Categorical Crossentropy
- **Optimizer:** Adam

## Results
- The model achieves **89% accuracy** in distinguishing between tumor and normal brain scans.
- Training and validation accuracy trends are plotted for performance analysis.

## Web Deployment
The project is deployed using Render at:
[Brain Scan AI](https://brain-scan-ai.onrender.com/)

## Future Enhancements
- Improve model accuracy with a larger dataset
- Implement real-time MRI scan analysis
- Deploy as a mobile app for easy accessibility


## Contributors
- **[S JAHAGANAPATHI]** - Developer

## Acknowledgments
Special thanks to open-source contributors and medical imaging datasets used in this project.

