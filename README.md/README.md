
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-API-black)
![Machine Learning](https://img.shields.io/badge/ML-NaiveBayes-orange)
![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FJS-yellow)



# 🚀 AI-Powered Spam Message Detection System (End-to-End ML Project)
An end-to-end machine learning web application that detects spam messages in real-time using NLP (TF-IDF + Naive Bayes) with Flask API and frontend integration.



## 🏗️ System Architecture

User → Frontend (HTML/JS) → Flask API → TF-IDF Vectorizer → ML Model → Prediction → UI Response





🚀 Spam Message Detection Web App
🧠 Overview

A full-stack Machine Learning web application that detects whether a message is Spam or Ham in real-time using a trained NLP model. Built with Flask API backend and a simple HTML/JavaScript frontend, fully deployment-ready.

✨ Features
🤖 ML-based Spam Detection (Naive Bayes + TF-IDF)
⚙️ Flask REST API (/predict)
🌐 Frontend integration (HTML + JS Fetch API)
📊 Real-time message classification
🔒 Clean JSON-based API response
☁️ Deployment-ready (Render / Vercel)
🏗️ Tech Stack

Frontend:

HTML5
CSS3
JavaScript (Fetch API)

Backend:

Python
Flask
Flask-CORS

Machine Learning:

Scikit-learn
Pandas
NumPy
TF-IDF Vectorizer
Multinomial Naive Bayes
🧠 How It Works
User enters a message in UI
Frontend sends request to Flask API
Text is converted using TF-IDF Vectorizer
ML model predicts Spam or Ham
Result is returned as JSON
UI displays prediction instantly
🔗 API Endpoint
POST /predict
Request:
{
  "message": "Congratulations! You won a prize"
}
Response:
{
  "prediction": "spam"
}
🚀 Project Structure
backend/
 ├── app.py
 ├── model.pkl
 ├── vectorizer.pkl
 ├── train_model.py
 ├── requirements.txt

frontend/
 ├── index.html
 ├── script.js
⚡ Setup Instructions
1. Clone repository
git clone https://github.com/your-username/spam-detection.git
cd spam-detection
2. Install dependencies
pip install -r requirements.txt
3. Run backend
python app.py
4. Open frontend

Use Live Server in VS Code

🌍 Deployment
Backend: Render / Railway
Frontend: Vercel / Netlify
Update API URL in frontend from localhost → deployed URL
📌 Future Improvements
📈 Spam probability score
🧠 Deep Learning model upgrade
🔐 User authentication system
💾 Database storage for messages
📱 Mobile-friendly UI
👨‍💻 Author

Built as a Full Stack AI Project for learning ML + Flask + API integration + deployment.



🧠 WHY THIS IMPRESSES RECRUITERS
## 🎯 Key Highlights

- Real-world ML deployment project
- Full-stack integration (Frontend + Backend + ML)
- REST API development using Flask
- NLP-based text classification system
- Production-ready architecture design






