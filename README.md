# ❤️ Heart Disease Prediction App

A web application that predicts the likelihood of heart disease based on medical attributes using a machine learning model. This project includes a Flask server and a responsive web interface for making predictions.

**Live Demo**: [https://heart-disease-detection-in-python.onrender.com/](https://heart-disease-detection-in-python.onrender.com/)

## 📋 Overview

This application uses a trained machine learning model to predict heart disease based on patient data. The model was trained using the heart disease dataset containing 1024 patient records with various medical attributes, achieving an accuracy of approximately 98%.

## 🔍 Features

- **Intuitive Web Interface**: Clean, responsive design with both light and dark mode support
- **Real-time Prediction**: Instant heart disease risk assessment
- **User-friendly Form**: Easy input of medical parameters
- **Accessibility**: Mobile and desktop compatible
- **Theme Preferences**: Remembers user's light/dark mode preference

## 🧠 Machine Learning Model

The application uses a Decision Tree Classifier model (pre-trained and saved as `heart_disease_model.pkl`), which achieved the highest accuracy (~98%) during evaluation compared to other models like Gaussian Naive Bayes and SVM.

## 📊 Input Parameters

The model requires the following features for prediction:

- **age**: Age of the patient
- **sex**: Sex (1 = male; 0 = female)
- **cp**: Chest pain type (4 values)
- **trestbps**: Resting blood pressure (in mm Hg)
- **chol**: Serum cholesterol in mg/dl
- **fbs**: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
- **restecg**: Resting electrocardiographic results
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise-induced angina
- **oldpeak**: ST depression induced by exercise
- **slope**: The slope of the peak exercise ST segment
- **ca**: Number of major vessels (0–3) colored by fluoroscopy
- **thal**: Thalassemia (3 = normal; 6 = fixed defect; 7 = reversible defect)

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, TailwindCSS
- **Machine Learning**: scikit-learn, joblib
- **Data Processing**: NumPy, Pandas

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/jhonney13/heart_app.git
   cd heart_app
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## 📱 Usage

1. Enter the required medical parameters in the form
2. Click the "Predict" button
3. View the prediction result indicating likelihood of heart disease

## ⚠️ Important Notes

- This application is for educational purposes only
- Always consult with healthcare professionals for medical advice
- The model has a reported accuracy of 98%, but actual results may vary

## 🧪 Model Evaluation

The machine learning model was evaluated using:
- **Accuracy Score**: ~98.54%
- **Confusion Matrix**: Visual representation of true vs predicted values
- **Classification Report**: Includes precision, recall, and F1-score

## 🔄 Future Improvements

- Add more detailed explanations for each input parameter
- Implement user accounts for saving prediction history
- Add visualization of prediction confidence
- Enhance mobile responsiveness
- Add multi-language support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Made with ❤️ by [Vipul Singh Parmar](https://github.com/jhonney13)

For any queries or collaborations, feel free to reach out!
