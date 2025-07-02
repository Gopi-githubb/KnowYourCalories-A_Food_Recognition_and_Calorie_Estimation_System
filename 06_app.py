from flask import Flask, render_template, send_from_directory, request, jsonify
# from waitress import serve
from app import app
from app.model import predict_food_items, calorie_db
from flask_cors import CORS 
import os
# from hypercorn.config import Config
# from hypercorn.asyncio import serve

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

# config = Config()
# config.bind = ["127.0.0.1:8000"]

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


if __name__ == '__main__':
    app.run(debug=True)


# if __name__ == "__main__":
#     serve(app, host='127.0.0.1', port=5000)
