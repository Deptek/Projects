{
 "cells": [
  {
   "cell_type": "raw",
   "id": "82c48b42-2b3f-492f-8d68-8f0b22fa981e",
   "metadata": {},
   "source": [
    "Handwritten Digit Recognition using CNN & RNN\n",
    "Project Overview\n",
    "\n",
    "This project compares Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs) on the MNIST handwritten digit dataset.\n",
    "The models classify handwritten digits (0-9) from 28×28 grayscale images.\n",
    "A Streamlit web application was also developed to allow users to upload digit images and obtain real-time predictions.\n",
    "\n",
    "Dataset\n",
    "MNIST Dataset\n",
    "\n",
    "60,000 Training Images\n",
    "10,000 Testing Images\n",
    "28×28 Grayscale Images\n",
    "10 Classes (0-9)\n",
    "Models\n",
    "CNN\n",
    "Architecture:\n",
    "\n",
    "Conv2D(1 → 32)\n",
    "ReLU\n",
    "MaxPool\n",
    "Conv2D(32 → 64)\n",
    "ReLU\n",
    "MaxPool\n",
    "Fully Connected Layer\n",
    "Output Layer (10 Classes)\n",
    "Accuracy:\n",
    "\n",
    "99.21%\n",
    "\n",
    "RNN\n",
    "Architecture:\n",
    "\n",
    "Input: (28 Timesteps, 28 Features)\n",
    "RNN (Hidden Size = 128)\n",
    "Fully Connected Layer\n",
    "Output Layer (10 Classes)\n",
    "Accuracy:\n",
    "\n",
    "96.48%\n",
    "\n",
    "Results\n",
    "Model\tAccuracy\n",
    "CNN\t99.21%\n",
    "RNN\t96.48%\n",
    "Conclusion\n",
    "CNN achieved higher accuracy because convolution operations preserve spatial information in images, whereas RNN processes the image sequentially as rows.\n",
    "\n",
    "Streamlit App\n",
    "Features:\n",
    "\n",
    "Upload handwritten digit image\n",
    "Real-time prediction\n",
    "Confidence score display\n",
    "CNN model deployment\n",
    "Run:\n",
    "streamlit run app.py"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
