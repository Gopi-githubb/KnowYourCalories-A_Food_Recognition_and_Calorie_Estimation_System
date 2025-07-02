# 🍱 KnowYourCalories: Food Recognition and Calorie Estimation System

KnowYourCalories is a deep learning-based web application that identifies food items from user-uploaded images and estimates their calorie content. The system is designed to promote dietary awareness and healthier eating habits by providing instant nutritional insights.

Built using **MobileNetV2** for food classification and **Flask** for web deployment, this project is a part of our academic research at **Sreyas Institute of Engineering and Technology**, Hyderabad.

---

## 📋 Abstract

This system offers a robust solution for recognizing foods and estimating their calorie content using the **MobileNetV2 deep learning model**. It is known for speed and efficiency in identifying different foods from images and calculating their associated calorie counts. The web interface allows users to upload meal images, receive predictions, and get calorie estimations. A user feedback mechanism helps refine the model over time.

---

## 🎯 Objectives

- ✅ To develop a deep learning-based food recognition system using MobileNetV2.
- ✅ To estimate the total calorie content of recognized food items using a predefined calorie database.
- ✅ To create an intuitive and user-friendly web interface for easy image uploads and result display.
- ✅ To incorporate a user feedback system for continuous model improvement.

---

## 🛠️ Technologies Used

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python (Flask Framework)
- **Deep Learning:** TensorFlow, Keras (MobileNetV2)
- **Libraries:** OpenCV, NumPy, Pandas
- **Tools:** Visual Studio Code, Git, GitHub

---

## 📂 Project Directory Structure

```

KnowYourCalories/
├── app/                     # Flask application backend logic
├── static/                  # Static frontend files (CSS, JavaScript)
├── templates/               # HTML templates for the web interface
├── food-101/                # Food-101 dataset (used for training and testing)
├── app.py                   # Main Flask application file
├── datasetcreation.py       # Script for dataset preprocessing and preparation
├── train\_model.py           # Script to train the MobileNetV2 model
├── test.py                  # Script for testing the trained model
├── app.zip                  # Compressed version of the app folder (optional)
├── research\_paper/          # Academic research paper
│   └── KnowYourCaloriesPaper.pdf
├── README.md                # Project documentation (this file)
└── requirements.txt         # Python dependencies (to be created)

````

---

## 📈 Methodology

1. **Model Selection:**  
   MobileNetV2 was selected for its balance between accuracy and computational efficiency.

2. **Dataset Preparation:**  
   - Utilized the **Food-101 dataset** containing various food categories.  
   - Images were resized, normalized, and tensorized to fit the model input requirements.

3. **Model Training:**  
   - Transfer learning with MobileNetV2.
   - The final layer was adjusted to classify the food categories in the dataset.

4. **Web Interface Development:**  
   - Developed using **Flask**, with **HTML**, **CSS**, and **JavaScript** for the frontend.

5. **Prediction and Calorie Estimation:**  
   - The trained model predicts the food class from the uploaded image.
   - A predefined calorie database is used to calculate total calories.

6. **User Feedback Mechanism:**  
   - Users can submit corrections if the prediction is wrong.
   - Feedback is stored for future model retraining.

---

## ⚙️ Installation

### ✅ Prerequisites:

- Python 3.8 or higher
- Git

### ✅ Installation Steps:

```bash
# 1. Clone the repository
git clone https://github.com/Sujal-Bangari/KnowYourCalories.git
cd KnowYourCalories

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate       # On macOS/Linux
venv\Scripts\activate          # On Windows

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Run the Flask application
python app.py
````

---

## 🚀 Usage

After running the Flask server, open your web browser and go to:

```
http://127.0.0.1:5000
```

### Features:

* 📷 **Upload a food image**
* 🔍 **View the predicted food name and estimated calorie count**
* ✍️ **Submit feedback if the prediction is inaccurate**

---

## 📸 Screenshots *(Optional)*

> *You can add actual images later by saving them in a `/screenshots` folder and updating the links below.*

### Example Screenshots:

* 🖼️ Home Page
* 🖼️ Prediction Result
* 🖼️ Feedback Form

---

## 👨‍💻 Team Members

| Name          | Email                                                           |
| ------------- | --------------------------------------------------------------- |
| B. Sujal      | [sujal703991@gmail.com](mailto:sujal703991@gmail.com)           |
| K. E. Mahathi | [mahathikamavaram@gmail.com](mailto:mahathikamavaram@gmail.com) |
| K. Gopi Chand | [gopichandk.edu@gmail.com](mailto:gopichandk.edu@gmail.com)     |

### Guided By:

**Dr. B. Suvarnamukhi**
Associate Professor, Department of CSE
Sreyas Institute of Engineering and Technology, Hyderabad

---

## 📄 Research Paper 📚

Our detailed research paper for academic reference is available here:

📄 [`research_paper/KnowYourCaloriesPaper.pdf`](research_paper/KnowYourCaloriesPaper.pdf)

---

## 📜 License

This project **currently does not have any open-source license**.

If you wish to use, modify, or distribute this project, **please contact the authors for permission**.

---

## 🙌 Acknowledgements

* Sreyas Institute of Engineering and Technology
* JNTUH Hyderabad
* TensorFlow, Flask, and OpenCV open-source communities
* Our team members and faculty

---

```

---


