# TreeNity_AI_Forestry
TreeNity is an AI-powered environmental monitoring project that analyzes **tree canopy cover**, **species health**, and **survival predictions** using open environmental datasets and machine learning.   It supports reforestation, biodiversity tracking, and sustainability research.
# 🌱 TreeNity: AI for Sustainable Forestry

**Hackathon:** Execute: AI Genesis Hackathon (Lablab.ai)  
**Duration:** April – May 2025  
**Role:** Backend Developer & ML Contributor  

## 🧩 Overview
TreeNity is an AI-powered environmental monitoring project that analyzes **tree canopy cover**, **species health**, and **survival predictions** using open environmental datasets and machine learning.  
It supports reforestation, biodiversity tracking, and sustainability research.

## ⚙️ Components
1. **Tree_Canopy_Cover.ipynb** – Analyzes canopy cover patterns using environmental features.  
2. **Tree_Health_SPECIES.ipynb** – Evaluates tree species and health indicators.  
3. **Tree_Survival_Prediction.ipynb** – Predicts tree survival chances using a Random Forest model.  
4. **Analyzing_Tree_Species.pdf** – Dataset documentation and exploratory analysis.

## 🧠 Machine Learning Model
- Model: `RandomForestClassifier`
- Goal: Predict tree survival probability based on:
  - Temperature (°C)
  - Rainfall (mm)
  - Soil Type
  - Fire Frequency
  - Planting Month

## 💻 Tech Stack
Python · Pandas · Scikit-learn · NumPy · GeoPandas · Streamlit · FastAPI  

## 🚀 How to Run
```bash
pip install -r requirements.txt
jupyter notebook notebooks/Tree_Survival_Prediction.ipynb
