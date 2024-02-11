# Import necessary libraries
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
import numpy as np

# Load pre-trained VGG16 model
base_model = VGG16(weights='imagenet')

# Function for food image classification
def classify_food_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = base_model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        print(f"{i + 1}: {label} ({score:.2%})")

# Example usage
img_path = "path/to/your/food/image.jpg"
classify_food_image(img_path)
