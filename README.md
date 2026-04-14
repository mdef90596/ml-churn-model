# 📊 Churn Prediction ML Pipeline

An end-to-end machine learning project for predicting customer churn, built with a modern MLOps stack and designed for scalability and production deployment.

---

## ⚙️ 1. Environment Setup

- Python virtual environment configured  
- Dependencies managed via `requirements.txt`  
- Project structure initialized with modular folders  

---

## 🔍 2. Exploratory Data Analysis (EDA)

- Understand dataset structure and distributions  
- Identify missing values and feature relationships  
- Perform initial visualizations to guide feature engineering  

---

## 🧩 3. Modularized EDA & Feature Engineering

- Refactor EDA into reusable modules  
- Implement custom encoding:
  - Binary encoding (e.g., Yes/No → 1/0)  
- Explore:
  - Seaborn for visualization  
  - Decision Trees for feature understanding  
  - XGBoost for model-ready transformations  

---

## 🏋️ 4. Model Training

- Train churn prediction model using XGBoost  
- Evaluate performance using appropriate metrics  
- Track experiments with MLflow  

---

## 🌐 5. Serving & UI

- Build API endpoints using FastAPI  
- Serve predictions in real-time  
- Optional lightweight UI for user interaction  

---

## 📦 6. Containerization

- Package application using Docker  
- Ensure reproducibility across environments  

---

## 🔄 7. CI/CD Pipeline

- Automate testing and deployment workflows  
- Integrate with version control for continuous delivery  

---

## ☁️ 8. AWS Deployment & End User Access

- Deploy containers to AWS infrastructure  
- Use Kubernetes for scaling and orchestration  
- Provide accessible endpoints for end users  

---

## 🎯 Goal

Build a production-ready churn prediction system that is:
- Scalable  
- Modular  
- Reproducible  
- Ready for real-time inference  
