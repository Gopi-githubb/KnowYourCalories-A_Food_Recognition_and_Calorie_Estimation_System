from flask import request, jsonify, render_template
from app import app
from app.model import predict_food_items, calorie_db
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    food_items = predict_food_items(file)
    calories = sum([calorie_db.get(food, 0) for food in food_items])
    return jsonify({'food': food_items, 'calories': calories})

@app.route('/feedback', methods=['POST']) 
def feedback(): 
    data = request.get_json() 
    correct_food_name = data.get('correctFoodName') 
    # Store feedback in a text file 
    feedback_dir = 'feedback' 
    os.makedirs(feedback_dir, exist_ok=True) 
    with open(os.path.join(feedback_dir, 'feedback.txt'), 'a') as f: 
        f.write(f'Correct food name: {correct_food_name}\n') 
    return jsonify({'message': 'Feedback received'})