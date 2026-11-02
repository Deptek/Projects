# Creating a feature to accept image 

import streamlit as st 

# Defining the model architecture since we only have saved the best model parameters

import torch 
import torch.nn as nn 
class CNN(nn.Module):
    def __init__(self): 
        super(CNN, self).__init__()

        self.conv_layers= nn.Sequential(
            nn.Conv2d(1, 32,kernel_size=3, padding= 1), 
            nn.ReLU(), 
            nn.MaxPool2d(2), 

            nn.Conv2d(32, 64,kernel_size=3, padding= 1), 
            nn.ReLU(), 
            nn.MaxPool2d(2),
        )
        self.fc_layers= nn.Sequential(
            nn.Linear(64*7*7, 128), 
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(128, 10) # 10 final o/p's 0 to 9
        )

    def forward(self, x): 
        x= self.conv_layers(x)
        x= x.view(x.size(0), -1)
        x= self.fc_layers(x)

        return x
        
# Loading the model with desired parameters

model =CNN()

model.load_state_dict(torch.load("cnn_model.pth", map_location="cpu")) # maplocation= just brings model and weights to same place-> CPU.

model.eval()

# Pre-processing image
from PIL import Image
from torchvision import transforms 
import matplotlib.pyplot as plt
from PIL import ImageOps

transform= transforms.Compose([  # converting new image into the exact way our model desires.
    transforms.Grayscale(),
    transforms.Resize((28,28)), 
    transforms.ToTensor(),
    transforms.Normalize((0.1307,),(0.3081))
])

# streamlit UI
st.title("Handwritten digit recognition")

uploaded_file= st.file_uploader("Upload a digit image", type=["png","jpg","jpeg"])

if uploaded_file is not None: 
    st.image(uploaded_file, caption="Uploaded Image", width=200)
    st.success("Image uploaded sucessfully!")
    image= Image.open(uploaded_file)
    image_tensor= transform(image) 
    #st.image(image_tensor.squeeze().numpy(),caption= "Processed Image")
    image_tensor= image_tensor.unsqueeze(0) # this will give [1,1,28,28]

    with torch.no_grad(): 
        outputs= model(image_tensor) 

        _,pred= torch.max(outputs,1)

        probs = torch.softmax(outputs, dim=1)

        confidence, pred = torch.max(probs, 1)

        st.success(f"Predicted digit: {pred.item()}")

        st.write(f"Confidence: {confidence.item()*100:.2f}%")

    


