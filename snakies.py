import streamlit as st
import numpy as np
from PIL import Image

# Backend functions and libraries
import os
import cv2
from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow.keras.layers import DepthwiseConv2D as OriginalDepthwiseConv2D

# Ensure TensorFlow uses CPU
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Custom layer handling
class CustomDepthwiseConv2D(OriginalDepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        # Handle the 'groups' parameter if present; remove if incompatible
        kwargs.pop('groups', None)
        super(CustomDepthwiseConv2D, self).__init__(*args, **kwargs)

# Register custom objects to avoid deserialization issues
custom_objects = {'DepthwiseConv2D': CustomDepthwiseConv2D}

try:
    # Attempt to load the model with custom objects
    model = tf.keras.models.load_model(
        'efficientnetv2-s-SnakeAIModel-60.53.h5', 
        custom_objects=custom_objects,
        compile=False  # Compile separately to control optimizer and loss functions
    )
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Compile the model after loading
model.compile(optimizer='Adamax', loss='categorical_crossentropy')  # Adjust as needed

# Class labels for predictions
class_labels = [
    'Asian coral snakes', 'Asian keelbacks', 'Bamboo snakes', 'Bearded snakes', 
    'Blind snakes', 'Blunt-headed tree snake', 'Bockadams', 'Bronzebacks', 
    'Brown snakes', 'Cat snakes', 'Cobras', 'Collared snakes', 'Crab-eating snakes', 
    'Dragon snakes', 'Estuarine snakes', 'Green pit vipers', 'Ground snakes', 
    'Keelbacks', 'King cobra', 'Kraits', 'Kukri snake', 'Long-glanded coral snakes', 
    'Mangrove snakes', 'Mock vipers', 'Mountain keelbacks', 'Mountain pit vipers', 
    'Mountain reed snakes', 'Mountain snakes', 'Mountain stream snakes', 'Mud snakes', 
    'Olive sea snakes', 'Pipe snakes', 'Pit vipers', 'Pythons', 'Racers', 
    'Rat snakes', 'Reed snakes', 'Sand snakes', 'Sea kraits', 'Sea snakes', 
    'Slug-eating snakes', 'Smooth snakes', 'Sunbeam snakes', 'Tentacled snake', 
    'Tree snakes', 'True vipers', 'Wart snakes', 'Whip snakes', 
    'Wolf snakes & bridle snakes'
]

# Function to predict and display results
def predict_and_display(img_array):
    preds = model.predict(img_array)
    probabilities = preds[0]
    top_3_indices = np.argsort(probabilities)[::-1][:3]
    top_3_probabilities = probabilities[top_3_indices] * 100

    prediction1 = f"{class_labels[top_3_indices[0]]} : Probability {top_3_probabilities[0]:.2f}%"
    prediction2 = f"{class_labels[top_3_indices[1]]} : Probability {top_3_probabilities[1]:.2f}%"
    prediction3 = f"{class_labels[top_3_indices[2]]} : Probability {top_3_probabilities[2]:.2f}%"
    return prediction1, prediction2, prediction3

def show():
    st.write("#")

    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        st.write("")

    with col2:
        st.title(":green[Snakies] - ลองใช้ AI ของเราเพื่อจำแนกชนิดงูไทย")
        st.write("อัพโหลดรูปเพิ่มเพื่อจำแนกชนิด")

        with st.container():
            uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
            if uploaded_file is not None:
                col4, col5, col6 = st.columns([0.25, 0.5, 0.25])
                with col5:
                    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
                    image = Image.open(uploaded_file).convert('RGB')
                    image = image.resize((224, 224))  # Resize to match the model's input size
                    img_array = np.array(image)
                    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

                    prediction1, prediction2, prediction3 = predict_and_display(img_array)
                    st.write(f"Prediction with Most Probability: :blue-background[{prediction1}]")
                    st.write(f"Prediction with Second Most Probability: :green-background[{prediction2}]")
                    st.write(f"Prediction with Third Most Probability: :orange-background[{prediction3}]")
            else:
                st.write("Waiting on image upload")

    with col3:
        st.write("")

# Display the interface
if __name__ == "__main__":
    show()
