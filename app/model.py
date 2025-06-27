import os 
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load the pre-trained model
model = load_model('app/trained_model.h5')

# Calorie database (sample data)
calorie_db = {
    'Apple pie': 237,
    'Beet salad':52,
    'Bread pudding': 210,
    'Cheesecake': 321,
    'Chicken curry': 110,
    'Chicken wings': 254,
    'Chocolate cake': 283,
    'Chocolate mousse': 450,
    'Churros': 447,
    'Club sandwich': 220,
    'Cup cakes': 305,
    'Deviled eggs': 155,
    'Donuts': 412,
    'Dumplings': 124,
    'French fries': 312,
    'French toast': 229,
    'Fried rice': 163,
    'Frozen yogurt': 159,
    'Garlic bread': 350,
    'Hamburger': 295,
    'Hot and sour soup': 39,
    'Hot dog': 290,
    'Ice cream': 207,
    'Lasagna': 135,
    'Macaroni and cheese': 164,
    'Macarons': 380,
    'Nachos': 306,
    'Omelette': 154,
    'Onion rings': 411,
    'Pancakes': 227,
    'Pizza': 266,
    'Ramen': 436,
    'Red velvet cake': 367,
    'Samosa': 308,
    'Spring rolls': 154,
    'Steak': 271,
    'Strawberry shortcake': 346,
    'Tacos': 226,
    'Tiramisu': 283,
    'Waffles': 291
    #Add more food items and their calorie counts
}

def preprocess_image(file):
    img = Image.open(file)
    img = img.resize((224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.0
    return img

def predict_food_items(file): 
    # Preprocess the image 
    img = preprocess_image(file) 
    #  Run the prediction 
    predictions = model.predict(img) 
    #  Get the predicted class index 
    predicted_class_index = np.argmax(predictions, axis=1)[0]
     # Get the class label from the prediction
    class_labels = list(calorie_db.keys()) 
    predicted_class = class_labels[predicted_class_index]
    return [predicted_class]