🫀 CardioGluco Risk Predictor

A full-stack Machine Learning web application that predicts the risk of Heart Disease ❤️ and Diabetes 🩸, and provides real-time insights, visual analytics, and personalized health recommendations.

---

🚀 Live Demo

🔗 (Add your deployed link here after Render deployment)
Example: https://cardiogluco.onrender.com

---

📌 Features

🔍 Prediction System

- Heart Disease Risk Prediction
- Diabetes Risk Prediction
- Probability-based risk scoring

📊 Data Visualization

- Interactive Pie Charts (Risk vs Safe)
- Animated Risk Score Indicator
- Clean Dashboard UI

🧠 Smart Insights Engine

- Key Risk Factors Detection
- Personalized Health Recommendations
- Dynamic insight generation based on inputs

🎨 User Interface

- Modern responsive design
- Smooth transitions & animations
- Clean medical dashboard layout

---

🏗️ Project Structure

cardiogluco-risk-predictor/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── models/
│   │   ├── heart_model.pkl
│   │   ├── diabetes_model.pkl
│   │   └── scalers.pkl
│   └── utils/
│       ├── preprocess.py
│       └── recommendations.py
│
├── frontend/
│   ├── index.html
│   ├── heart.html
│   ├── diabetes.html
│   ├── css/
│   ├── js/
│   └── assets/
│
└── notebooks/
    ├── heart_model_training.ipynb
    └── diabetes_model_training.ipynb

---

⚙️ Tech Stack

💻 Frontend

- HTML5
- CSS3
- JavaScript (Vanilla JS)

⚙️ Backend

- Python
- Flask

🤖 Machine Learning

- Scikit-learn
- Pandas
- NumPy

📊 Visualization

- Chart.js / Custom JS charts

---

🧪 How It Works

1. User enters medical data
2. Frontend sends data via API ("fetch")
3. Flask backend processes input
4. ML model predicts risk probability
5. Results are returned as JSON
6. UI displays:
   - Risk percentage
   - Graphical charts
   - Key risk factors
   - Recommendations

---

▶️ Run Locally

1️⃣ Clone Repository

git clone https://github.com/your-username/cardiogluco-risk-predictor.git
cd cardiogluco-risk-predictor

2️⃣ Install Dependencies

pip install -r backend/requirements.txt

3️⃣ Start Backend Server

python backend/app.py

4️⃣ Open in Browser

http://127.0.0.1:5000/

---

🌐 Deployment Guide

✅ Recommended: Render (Full Stack)

1. Push project to GitHub
2. Go to https://render.com
3. Create New Web Service
4. Connect GitHub repo

🔧 Build Command

pip install -r backend/requirements.txt

▶️ Start Command

python backend/app.py

---

⚠️ Important Changes Before Deployment

Replace this:

fetch("http://127.0.0.1:5000/predict/heart")

With:

fetch("/predict/heart")

(Same for diabetes API)

---

🚫 GitHub Pages Limitation

- Only supports frontend
- Backend (Flask) will NOT work

---

📸 Screenshots

🖥️ Dashboard

(Add screenshot here)

📊 Risk Visualization

(Add screenshot here)

🧠 Insights & Recommendations

(Add screenshot here)

---

💡 Future Enhancements

- 🔐 User authentication system
- 📈 Health history tracking
- 🧑‍⚕️ Doctor recommendations
- 📱 Mobile app version
- 🧠 Deep learning model integration

---

🤝 Contributing

Contributions are welcome!

Steps:

1. Fork the repository
2. Create new branch
3. Make changes
4. Submit Pull Request

---

📄 License

This project is for educational and academic purposes.

---

👩‍💻 Author

Aliya Begum

---

⭐ Support

If you found this project helpful:

- ⭐ Star the repository
- 🍴 Fork it
- 📢 Share it

---

🧠 Inspiration

Built to combine Machine Learning + Healthcare + Web Development into a real-world impactful solution.

---
