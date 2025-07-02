# 🍱 KnowYourCalories: Food Recognition and Calorie Estimation System

**KnowYourCalories** is a deep learning-based web application designed to recognize food items from images and estimate their calorie content. The system promotes dietary awareness and supports healthier eating habits by providing instant nutritional insights.

Developed as part of an academic research project at **Sreyas Institute of Engineering and Technology, Hyderabad**, this solution integrates **MobileNetV2** for food classification and **Flask** for web deployment.

---

## 📋 Abstract

This system offers a robust solution for recognizing food and estimating calorie content using the **MobileNetV2 deep learning model**. Known for its speed and efficiency, MobileNetV2 accurately identifies different foods from images and calculates their associated calorie counts.

The application is accessible through an intuitive web interface where users can upload pictures of their meals. The pre-trained MobileNetV2 model classifies the food, and calorie estimation is performed using a predefined calorie database.

Additionally, a user feedback mechanism allows users to correct inaccurate predictions, helping improve the model's accuracy over time.

---

## 🎯 Objectives

- ✅ Develop a food recognition system using a deep learning model.
- ✅ Estimate the total calorie content of recognized food items using a predefined database.
- ✅ Build a user-friendly web interface for easy image uploads and display of results.
- ✅ Incorporate a user feedback mechanism to improve system performance over time.

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
├── app/                     # Flask backend application logic
├── static/                  # Static files (CSS, JavaScript)
├── templates/               # HTML templates for web interface
├── food-101/                # Food-101 dataset used for training/testing
├── app.py                   # Main Flask application file
├── datasetcreation.py       # Script for dataset preparation
├── train\_model.py           # MobileNetV2 model training script
├── test.py                  # Script for testing the trained model
├── app.zip                  # Compressed project folder (optional)
├── research\_paper/          # Academic research paper
│   └── KnowYourCaloriesPaper.pdf
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies (to be created)

````

---

## 📈 Methodology

1. **Model Selection:**  
   MobileNetV2 was selected for its balance between accuracy and computational efficiency, making it suitable for deployment on resource-constrained devices.

2. **Dataset Preparation:**  
   - Dataset: **Food-101**  
   - Preprocessing: Images resized to 224×224 pixels, normalized, and tensorized.

3. **Model Training:**  
   - Performed transfer learning using MobileNetV2.
   - The final layer was modified to match the number of food classes.

4. **Web Interface Development:**  
   - Developed using **Flask**.
   - Frontend: **HTML**, **CSS**, and **JavaScript**.
   - Image upload functionality implemented for user inputs.

5. **Prediction and Calorie Estimation:**  
   - Uploaded images are processed and fed into the trained model.
   - Predictions are mapped to calorie values from a predefined database.

6. **User Feedback Mechanism:**  
   - Users can provide feedback if the prediction is incorrect.
   - Feedback is stored for future model improvements.

---

## ✅ Results

- ✅ **Accuracy:** Achieved high accuracy in food recognition across multiple categories.
- ✅ **Efficiency:** Demonstrated fast and efficient image processing, suitable for real-time use.
- ✅ **User Interface:** Provided an intuitive and easy-to-use web interface.
- ✅ **User Feedback:** Enabled continuous improvement through user-submitted feedback.

---

## ✅ Installation

### Prerequisites:

- Python 3.8 or higher
- Git

### Installation Steps:

```bash
# 1. Clone the repository
git clone https://github.com/Sujal-Bangari/KnowYourCalories.git
cd KnowYourCalories

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows

# 3. Install required Python packages
pip install -r requirements.txt

# 4. Run the Flask application
python app.py
````

---

## 🚀 Usage

Once the Flask server is running, open your web browser and navigate to:

```
http://127.0.0.1:5000
```

### Features:

* 📷 Upload a food image.
* 🔍 View the predicted food name and estimated calorie count.
* ✍️ Submit feedback if the prediction is inaccurate.

---

## 📸 Screenshots *(Optional)*

> *You can create a `/screenshots` folder and add images here for better visualization.*

* 🖼️ Home Page
* 🖼️ Prediction Result
* 🖼️ Feedback Form

---

## ✅ Conclusion

This project demonstrates the successful application of **MobileNetV2** for food recognition and calorie estimation. The system provides an efficient, user-friendly tool for dietary tracking and health management.

The integration of a feedback mechanism and real-time processing ensures the system remains accurate and reliable, meeting the needs of diverse users.

---

## ✅ Future Work

* 📌 **Expand Calorie Database:** Include a broader range of food items.
* 📌 **Model Improvement:** Further improve accuracy using additional data and user feedback.
* 📌 **Mobile Application Development:** Build a mobile app version for enhanced accessibility.

---

## 👨‍💻 Team Members

| Name          | Email                                                           |
| ------------- | --------------------------------------------------------------- |
| B. Sujal      | [sujal703991@gmail.com](mailto:sujal703991@gmail.com)           |
| K. E. Mahathi | [mahathikamavaram@gmail.com](mailto:mahathikamavaram@gmail.com) |
| K. Gopi Chand | [gopichandk.edu@gmail.com](mailto:gopichandk.edu@gmail.com)     |

**Guided By:**
Dr. B. Suvarnamukhi
Associate Professor, Department of CSE
Sreyas Institute of Engineering and Technology, Hyderabad

---

## 📄 Research Paper 📚

Our detailed research paper describing this project is available here:

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
* Our teammates, faculty, and all contributors

---

```

---

