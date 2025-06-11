# 🍱 KnowYourCalories – Food Recognition and Calorie Estimation System

**KnowYourCalories** is a web-based system that uses deep learning to identify food items from images and estimate their calorie content. Built with **MobileNetV2** and **Flask**, this application enables users to upload meal images and instantly receive nutritional insights. The system is designed to help users track their food intake and adopt healthier eating habits.

---

## 🚀 Project Features

- 🔍 **Food Recognition** using the MobileNetV2 deep learning model
- 🍔 **Calorie Estimation** based on a predefined food-calorie database
- 🌐 **Web Interface** developed with Flask, HTML, CSS, and JavaScript
- ✍️ **User Feedback Mechanism** to improve model accuracy over time
- 📈 **Real-time Results** with intuitive UI and interactive experience

---

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Flask
- **Machine Learning**: TensorFlow, Keras (MobileNetV2)
- **Libraries**: OpenCV, NumPy, Pandas
- **Tools**: Visual Studio Code, Git, GitHub

---

## 📂 Project Structure
KnowYourCalories/
├── app.py                         # Main Flask application
├── food_recognition.py           # Model prediction logic
├── calorie_estimation.py         # Calorie calculation logic
├── requirements.txt              # Python dependencies
│
├── model/
│   ├── train_model.py            # Training script
│   └── trained_model.h5          # Pretrained MobileNetV2 model
│
├── templates/
│   └── index.html                # Web interface
│
├── static/
│   ├── style.css                 # Styling for frontend
│   └── script.js                 # Optional JS functionality
│
├── utils/
│   ├── calorie_db.py             # Food-calorie mapping
│   └── helper_functions.py       # Any reusable utilities
│
├── feedback/
│   └── feedback.txt              # User-submitted corrections
│
├── docs/
│   └── KnowYourCaloriesPaper.pdf # Project research paper
│
└── README.md



