from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

app = FastAPI(title="Heart Disease Detection API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check if model exists, otherwise train and save it
model_path = "heart_disease_model.joblib"
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    # Load and train model
    df = pd.read_csv("heart_disease_dataset.csv")
    X = df.drop("heart_disease", axis=1)
    y = df["heart_disease"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save the model
    joblib.dump(model, model_path)

class PatientData(BaseModel):
    age: int
    sex: int
    chest_pain_type: int
    resting_blood_pressure: int
    cholesterol: int
    fasting_blood_sugar: int
    resting_ecg: int
    max_heart_rate: int
    exercise_induced_angina: int
    st_depression: float
    st_slope: int
    num_major_vessels: int
    thalassemia: int

@app.get("/")
def read_root():
    return {"message": "Heart Disease Detection API"}

@app.post("/predict")
def predict_heart_disease(data: PatientData):
    # Convert input data to numpy array
    input_data = np.array([[
        data.age,
        data.sex,
        data.chest_pain_type,
        data.resting_blood_pressure,
        data.cholesterol,
        data.fasting_blood_sugar,
        data.resting_ecg,
        data.max_heart_rate,
        data.exercise_induced_angina,
        data.st_depression,
        data.st_slope,
        data.num_major_vessels,
        data.thalassemia
    ]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0].max()
    
    return {
        "heart_disease": int(prediction),
        "confidence": float(probability)
    }

@app.get("/algorithm/{algorithm_name}")
def get_algorithm_info(algorithm_name: str):
    """Return detailed information about a specific algorithm"""
    algorithm_details = {
        "Random Forest": {
            "name": "Random Forest",
            "type": "Ensemble Learning",
            "description": "An ensemble learning method that operates by constructing multiple decision trees during training and outputting the mode of the classes (classification) or mean prediction (regression) of the individual trees.",
            "how_it_works": [
                "Creates multiple decision trees from randomly selected subsets of the dataset",
                "Each tree makes its own prediction",
                "Final prediction is determined by majority voting (classification) or averaging (regression)",
                "Reduces overfitting compared to a single decision tree"
            ],
            "advantages": [
                "Reduces overfitting compared to individual decision trees",
                "Handles large datasets with higher dimensionality well",
                "Provides estimates of feature importance",
                "Robust to outliers and missing values"
            ],
            "disadvantages": [
                "Less interpretable than single decision trees",
                "Computationally more expensive than simpler algorithms",
                "Memory intensive due to storing multiple trees"
            ],
            "parameters": {
                "n_estimators": "100 (number of trees in the forest)",
                "random_state": "42 (controls randomness for reproducibility)"
            }
        },
        "Decision Tree": {
            "name": "Decision Tree",
            "type": "Tree-based Learning",
            "description": "A tree-like model of decisions and their possible consequences. It uses a tree structure to make decisions based on feature values.",
            "how_it_works": [
                "Starts with a root node representing the entire dataset",
                "Splits the data based on feature values that best separate classes",
                "Creates branches for each possible outcome of a test",
                "Continues recursively until leaf nodes contain homogeneous data"
            ],
            "advantages": [
                "Easy to understand and interpret",
                "Requires little data preprocessing",
                "Able to handle both numerical and categorical variables",
                "No assumptions about distribution of data"
            ],
            "disadvantages": [
                "Prone to overfitting with complex trees",
                "Can be unstable (small changes in data can result in different tree)",
                "Biased toward dominant classes in imbalanced datasets"
            ],
            "parameters": {
                "criterion": "Gini (measure of impurity used for splitting)",
                "max_depth": "None (maximum depth of the tree)",
                "min_samples_split": "2 (minimum samples required to split a node)"
            }
        },
        "Logistic Regression": {
            "name": "Logistic Regression",
            "type": "Linear Model",
            "description": "A statistical model that uses a logistic function to model a binary dependent variable, estimating probabilities using a logistic function.",
            "how_it_works": [
                "Uses the logistic (sigmoid) function to map any real value to between 0 and 1",
                "Fits the best parameters using maximum likelihood estimation",
                "Predicts probability that an instance belongs to a particular class",
                "Applies a threshold (usually 0.5) to make binary predictions"
            ],
            "advantages": [
                "Provides probability scores for predictions",
                "No assumptions about distributions of classes in feature space",
                "Less prone to overfitting with low-dimensional datasets",
                "Easy to regularize and update with new data"
            ],
            "disadvantages": [
                "Assumes linear relationship between features and log-odds",
                "Not suitable for non-linear problems",
                "Sensitive to outliers",
                "Requires large sample sizes for stable results"
            ],
            "parameters": {
                "penalty": "l2 (regularization technique)",
                "C": "1.0 (inverse of regularization strength)",
                "random_state": "42 (controls randomness for reproducibility)"
            }
        },
        "SVM": {
            "name": "Support Vector Machine",
            "type": "Kernel Method",
            "description": "A supervised learning model that finds the hyperplane that best separates different classes in the feature space.",
            "how_it_works": [
                "Finds the optimal hyperplane that maximizes the margin between classes",
                "Uses support vectors (data points closest to the hyperplane) for decision making",
                "Can handle non-linear classification using kernel functions",
                "Maps input vectors to higher-dimensional space for better separation"
            ],
            "advantages": [
                "Effective in high-dimensional spaces",
                "Memory efficient (uses subset of training points)",
                "Versatile with different kernel functions",
                "Robust to overfitting in high-dimensional space"
            ],
            "disadvantages": [
                "Computationally intensive for large datasets",
                "Does not directly provide probability estimates",
                "Sensitive to feature scaling",
                "Requires careful parameter tuning"
            ],
            "parameters": {
                "kernel": "rbf (Radial Basis Function kernel)",
                "C": "1.0 (regularization parameter)",
                "gamma": "scale (kernel coefficient)"
            }
        }
    }
    
    if algorithm_name in algorithm_details:
        return algorithm_details[algorithm_name]
    else:
        return {"error": f"Algorithm '{algorithm_name}' not found"}