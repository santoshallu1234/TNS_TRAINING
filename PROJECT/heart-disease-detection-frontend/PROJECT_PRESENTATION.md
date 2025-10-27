# Heart Disease Detection using Classification Algorithms

## Capstone Project 2 Presentation

---

## 1. Project Overview

### Title
Heart Disease Detection using Classification Algorithms

### Category
Supervised Learning (Classification)

### Problem Statement
Heart disease is one of the leading causes of death worldwide. Early and accurate detection through diagnostic screening can significantly improve patient survival rates and reduce healthcare costs.

This project aims to build machine learning models that predict the presence of heart disease based on patients' demographic, clinical, and diagnostic test data, enabling healthcare professionals to make timely and informed decisions.

---

## 2. Objectives

- Develop and compare multiple classification algorithms (Decision Tree, Random Forest, Logistic Regression, SVM) to predict heart disease
- Present actionable findings to stakeholders in the healthcare domain
- Create an intuitive web interface for healthcare professionals to input patient data and receive predictions

---

## 3. Dataset Information

### Dataset Name/Source
heart_disease_dataset

### Size & Features
- Number of records: 400
- Target variable: heart_disease (0 = No, 1 = Yes)
- Features: 13 Features + 1 ClassLabel (heart_disease)

### Features
1. Age
2. Sex
3. Chest Pain Type
4. Resting Blood Pressure
5. Cholesterol
6. Fasting Blood Sugar
7. Resting ECG
8. Max Heart Rate
9. Exercise-Induced Angina
10. ST Depression
11. ST Slope
12. Num Major Vessels
13. Thalassemia

### Pre-processing
- No missing values in the dataset
- Data is already in numerical format
- Split data into training (80%) and testing (20%) sets

---

## 4. Tools & Technologies

### Development Tools
- Python (Pandas, NumPy, Scikit-learn, SciPy)
- Svelte (Frontend Framework)
- FastAPI (Backend Framework)
- Docker (Containerization)

### Machine Learning Algorithms
- Decision Tree
- Random Forest
- Logistic Regression
- Support Vector Machine (SVM)

---

## 5. Evaluation Criteria

### Primary Metrics
- Recall (Sensitivity)
- Precision
- F1-score
- ROC-AUC

### Secondary Metrics
- Specificity
- Accuracy

---

## 6. Frontend Implementation

### Technology Stack
- Svelte for reactive UI components
- CSS3 for responsive styling
- Vite for build tooling

### Key Components
1. **Header Component** - Project title and description
2. **Prediction Form** - Input form for patient data
3. **Prediction Result** - Display of prediction results with risk assessment
4. **Model Information** - Performance metrics comparison
5. **Footer Component** - Copyright information

### Features
- Responsive design for all device sizes
- Form validation for data integrity
- Loading states for API requests
- Clear visualization of results
- Detailed model performance information

---

## 7. Backend Integration

### FastAPI Backend
- RESTful API endpoints
- Machine learning model serving
- Data validation with Pydantic
- Automatic API documentation

### API Endpoints
- `GET /` - Health check endpoint
- `POST /predict` - Heart disease prediction endpoint

### Docker Integration
- Containerized frontend and backend services
- Docker Compose for multi-container applications
- Easy deployment and scaling

---

## 8. Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Random Forest | 85.5% | 87.2% | 84.1% | 85.6% |
| Decision Tree | 78.9% | 80.3% | 77.6% | 78.9% |
| Logistic Regression | 82.3% | 83.7% | 81.2% | 82.4% |
| SVM | 83.7% | 85.1% | 82.4% | 83.7% |

---

## 9. Results and Findings

### Key Insights
- Random Forest achieved the highest accuracy (85.5%) among all models
- All models showed good performance with F1-scores above 78%
- Chest pain type and ST depression were identified as important features

### Clinical Implications
- The model can assist healthcare professionals in early detection
- Provides quantitative risk assessment for better decision-making
- Reduces the burden of manual analysis for routine cases

---

## 10. Future Enhancements

### Model Improvements
- Hyperparameter tuning for better performance
- Ensemble methods to combine multiple models
- Feature engineering to extract more meaningful features

### Application Enhancements
- User authentication and patient record management
- Historical prediction tracking
- Integration with hospital information systems
- Mobile application development

---

## 11. Conclusion

This project successfully demonstrates the application of machine learning algorithms for heart disease detection. The developed Svelte frontend provides an intuitive interface for healthcare professionals to input patient data and receive predictions. The Random Forest model performed best with an accuracy of 85.5%, making it suitable for clinical decision support.

The combination of modern web technologies and machine learning provides a powerful tool for improving healthcare outcomes through early detection of heart disease.

---

## 12. Questions?

Thank you for your attention. I'm happy to answer any questions you may have about the project.