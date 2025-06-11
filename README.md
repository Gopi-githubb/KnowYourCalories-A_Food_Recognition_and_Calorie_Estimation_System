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

```bash
KnowYourCalories/
├── app.py                         # Main Flask application
├── food_recognition.py           # Logic to load model and predict food
├── calorie_estimation.py         # Maps predictions to calorie values
├── requirements.txt              # List of required Python libraries
│
├── model/
│   ├── train_model.py            # Code to train MobileNetV2
│   └── trained_model.h5          # Trained model file
│
├── templates/
│   └── index.html                # Upload interface
│
├── static/
│   ├── style.css                 # Styling for frontend
│   └── script.js                 # Optional JavaScript
│
├── utils/
│   ├── calorie_db.py             # Calorie database (food: calories)
│   └── helper_functions.py       # Any utility/helper code
│
├── feedback/
│   └── feedback.txt              # Stores user corrections
│
├── docs/
│   └── KnowYourCaloriesPaper.pdf # Your research paper
│
└── README.md
```

## 🧪 Getting Started

Follow these steps to set up and run the project on your local machine.

### ✅ Prerequisites

- Python 3.8 or above  
- Git installed

### ⚙️ Installation & Running the App

```bash
# 1. Clone the repository
git clone https://github.com/Gopi-githubb/KnowYourCalories-A_Food_Recognition_and_Calorie_Estimation_System.git
cd KnowYourCalories-A_Food_Recognition_and_Calorie_Estimation_System

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # For macOS/Linux
venv\Scripts\activate         # For Windows

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Run the Flask application
python app.py
```

### 🌐 Access the Application
Once the Flask server is running, open your browser and go to:
http://127.0.0.1:5000


You will be able to:

- 📷 Upload a food image  
- 🔍 Get the food name and estimated calories  
- ✍️ Submit feedback if the prediction is incorrect  

---

## 📸 Sample Screenshots


- 🖼️ Home Page
-   
  ![Home Page](screenshots/home.png)

- 🖼️ Upload & Prediction Result
- 
  ![Upload Result](screenshots/prediction_result.png)

- 🖼️ Feedback Form
- 
  ![Feedback](screenshots/feedback_form.png)

---

## 👨‍💻 Team Members

| Name              | Email                            |
|-------------------|----------------------------------|
| **B. Sujal**      | sujal703991@gmail.com            |
| **K. E. Mahathi** | mahathikamavaram@gmail.com       |
| **K. Gopi Chand** | gopichandk.edu@gmail.com         |

> **Guided by:**  
> Dr. B. Suvarnamukhi  
> Associate Professor, Dept. of CSE  
> Sreyas Institute of Engineering and Technology, Hyderabad


---

## 📜 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full details.

---

## 📄 Research Paper

📘 Read our paper: [`KnowYourCaloriesPaper.pdf`](docs/KnowYourCaloriesPaper.pdf)

---

## 🙌 Acknowledgements

- Sreyas Institute of Engineering and Technology  
- JNTUH Hyderabad  
- TensorFlow, Flask, OpenCV communities  
- All teammates and contributors






