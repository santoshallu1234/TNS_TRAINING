# Heart Disease Detection Project - Complete Documentation

## Project Overview

This project implements a machine learning solution for heart disease detection using classification algorithms. It includes a Svelte frontend for user interaction, a FastAPI backend for serving predictions, and Docker for containerization.

## Project Structure

```
PROJECT/
├── heart_disease_dataset.csv                    # Dataset file
├── heart-disease-detection-frontend/           # Frontend application
│   ├── src/                                    # Source code
│   │   ├── App.svelte                          # Main application component
│   │   ├── app.css                             # Global styles
│   │   ├── main.js                             # Application entry point
│   │   └── lib/
│   │       └── components/                     # UI components
│   │           ├── Header.svelte
│   │           ├── Footer.svelte
│   │           ├── PredictionForm.svelte
│   │           ├── PredictionResult.svelte
│   │           └── ModelInfo.svelte
│   ├── package.json                            # Frontend dependencies
│   ├── README.md                               # Frontend documentation
│   ├── Dockerfile                              # Frontend Docker configuration
│   ├── docker-compose.yml                      # Multi-container setup
│   ├── setup-instructions.html                 # Backend setup instructions
│   └── PROJECT_PRESENTATION.md                 # Project presentation
└── PROJECT_DOCUMENTATION.md                    # This file
```

## Prerequisites

- Node.js (v14 or higher)
- Python (v3.7 or higher)
- Docker (optional, for containerization)
- npm or yarn package manager

## Setup Instructions

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd heart-disease-detection-frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Access the application at `http://localhost:5173`

### Backend Setup

1. Create a new directory for the backend in the parent folder:
   ```bash
   cd ..
   touch main.py
   touch requirements.txt
   touch Dockerfile.backend
   ```

2. Add the following content to `requirements.txt`:
   ```
   fastapi==0.68.0
   uvicorn[standard]==0.15.0
   scikit-learn==1.0.2
   pandas==1.3.3
   numpy==1.21.2
   pydantic==1.8.2
   joblib==1.1.0
   ```

3. Add the following content to `main.py`:
   ```python
   from fastapi import FastAPI
   from pydantic import BaseModel
   import pandas as pd
   import numpy as np
   from sklearn.ensemble import RandomForestClassifier
   from sklearn.model_selection import train_test_split
   import joblib
   import os

   app = FastAPI(title="Heart Disease Detection API")

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
   ```

4. Add the following content to `Dockerfile.backend`:
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY . .

   EXPOSE 8000

   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

5. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### Connecting Frontend to Backend

1. In the frontend `App.svelte` file, uncomment and modify the `handlePredict` function:
   ```javascript
   function handlePredict(data) {
     loading = true;
     
     fetch('http://localhost:8000/predict', {
       method: 'POST',
       headers: {
         'Content-Type': 'application/json',
       },
       body: JSON.stringify(data),
     })
     .then(response => response.json())
     .then(result => {
       prediction = result;
       loading = false;
     })
     .catch(error => {
       console.error('Error:', error);
       loading = false;
     });
   }
   ```

## Docker Deployment

### Running with Docker Compose

1. Ensure both Dockerfiles are in place:
   - Frontend: `heart-disease-detection-frontend/Dockerfile`
   - Backend: `Dockerfile.backend` (in parent directory)

2. Update the `docker-compose.yml` in the frontend directory:
   ```yaml
   version: '3.8'

   services:
     frontend:
       build: .
       ports:
         - "3000:3000"
       depends_on:
         - backend
       environment:
         - NODE_ENV=production

     backend:
       build: 
         context: ../
         dockerfile: Dockerfile.backend
       ports:
         - "8000:8000"
       environment:
         - ENV=production
       volumes:
         - ../heart_disease_dataset.csv:/app/heart_disease_dataset.csv
   ```

3. Run the complete application:
   ```bash
   cd heart-disease-detection-frontend
   docker-compose up --build
   ```

4. Access the application:
   - Frontend: `http://localhost:3000`
   - Backend API: `http://localhost:8000`
   - Backend API Documentation: `http://localhost:8000/docs`

## Features

### Frontend Features
- Responsive design for all device sizes
- Patient data input form with validation
- Real-time prediction results display
- Risk assessment visualization
- Model performance comparison
- Loading states for API requests

### Backend Features
- RESTful API for heart disease prediction
- Pre-trained Random Forest model
- Automatic model training if not found
- Input validation using Pydantic
- Automatic API documentation with Swagger UI
- Docker containerization support

## Machine Learning Models

### Implemented Algorithms
1. **Random Forest** - Ensemble method using multiple decision trees
2. **Decision Tree** - Simple tree-based classification
3. **Logistic Regression** - Linear classification algorithm
4. **Support Vector Machine (SVM)** - Margin-based classification

### Evaluation Metrics
- **Accuracy**: Proportion of correct predictions
- **Precision**: Proportion of true positives among positive predictions
- **Recall (Sensitivity)**: Proportion of true positives among actual positives
- **F1-Score**: Harmonic mean of precision and recall
- **ROC-AUC**: Area under the ROC curve

### Model Performance (Example Results)
| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Random Forest | 85.5% | 87.2% | 84.1% | 85.6% |
| Decision Tree | 78.9% | 80.3% | 77.6% | 78.9% |
| Logistic Regression | 82.3% | 83.7% | 81.2% | 82.4% |
| SVM | 83.7% | 85.1% | 82.4% | 83.7% |

## API Endpoints

### Health Check
```
GET /
```
Response:
```json
{
  "message": "Heart Disease Detection API"
}
```

### Prediction
```
POST /predict
```
Request Body:
```json
{
  "age": 58,
  "sex": 1,
  "chest_pain_type": 1,
  "resting_blood_pressure": 134,
  "cholesterol": 246,
  "fasting_blood_sugar": 0,
  "resting_ecg": 0,
  "max_heart_rate": 155,
  "exercise_induced_angina": 0,
  "st_depression": 0.4,
  "st_slope": 1,
  "num_major_vessels": 1,
  "thalassemia": 2
}
```

Response:
```json
{
  "heart_disease": 1,
  "confidence": 0.87
}
```

## Development Guidelines

### Frontend Development
- Use Svelte components for UI elements
- Follow the existing styling patterns
- Maintain responsive design principles
- Test components in isolation

### Backend Development
- Follow REST API best practices
- Use Pydantic for data validation
- Document API endpoints properly
- Implement error handling

### Machine Learning Development
- Use scikit-learn for model implementation
- Validate models with appropriate metrics
- Save trained models for reuse
- Document feature engineering steps

## Troubleshooting

### Common Issues

1. **Port already in use**
   - Solution: Change the port in the Dockerfile or docker-compose.yml

2. **Model not found**
   - Solution: Ensure the dataset file is in the correct location

3. **Connection refused**
   - Solution: Check if both frontend and backend services are running

4. **CORS errors**
   - Solution: Add CORS middleware to the FastAPI application:
     ```python
     from fastapi.middleware.cors import CORSMiddleware

     app.add_middleware(
         CORSMiddleware,
         allow_origins=["*"],
         allow_credentials=True,
         allow_methods=["*"],
         allow_headers=["*"],
     )
     ```

## Future Enhancements

### Model Improvements
- Hyperparameter tuning using GridSearchCV
- Feature selection techniques
- Ensemble methods combining multiple algorithms
- Deep learning approaches

### Application Enhancements
- User authentication and authorization
- Patient record management
- Historical prediction tracking
- Integration with hospital information systems
- Mobile application development

### Deployment Enhancements
- Cloud deployment (AWS, Azure, GCP)
- CI/CD pipeline implementation
- Load balancing for high availability
- Monitoring and logging solutions

## Conclusion

This project successfully demonstrates the application of machine learning algorithms for heart disease detection. The combination of modern web technologies (Svelte, FastAPI) and machine learning provides a powerful tool for improving healthcare outcomes through early detection of heart disease.

The modular architecture allows for easy maintenance and future enhancements, making it a solid foundation for a production-ready medical application.