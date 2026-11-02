Handwritten Digit Recognition using CNN & RNN
Project Overview

This project compares Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs) on the MNIST handwritten digit dataset.
The models classify handwritten digits (0-9) from 28×28 grayscale images.
A Streamlit web application was also developed to allow users to upload digit images and obtain real-time predictions.

Dataset
MNIST Dataset
-60,000 Training Images
-10,000 Testing Images
-28×28 Grayscale Images
-10 Classes (0-9)

Models:
CNN
Architecture:
-Conv2D(1 → 32)
-ReLU
-MaxPool
-Conv2D(32 → 64)
-ReLU
-MaxPool
-Fully Connected Layer
-Output Layer (10 Classes)
Accuracy: 99.21%

RNN
Architecture:
-Input: (28 Timesteps, 28 Features)
-RNN (Hidden Size = 128)
-Fully Connected Layer
-Output Layer (10 Classes)
Accuracy: 96.48%

Results:
Model	Accuracy
-CNN	99.21%
-RNN	96.48%

Conclusion:
CNN achieved higher accuracy because convolution operations preserve spatial information in images, whereas RNN processes the image sequentially as rows.

Streamlit App
Features:
-Upload digit image
-Real-time prediction
-Confidence score display
-CNN model deployment

Run:
-streamlit run app.py
<img width="1306" height="847" alt="Screenshot 2026-11-02 201200" src="https://github.com/user-attachments/assets/2280024e-2d27-48ed-a5ab-67d5bbdef55b" />


