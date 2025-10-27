# How to Run the Heart Disease Detection Project

This document provides step-by-step instructions for running the complete Heart Disease Detection project, including both the frontend and backend components.

## Project Structure

```
PROJECT/
├── heart_disease_dataset.csv       # Dataset file
├── main.py                         # FastAPI backend application
├── requirements.txt                # Python dependencies
├── Dockerfile.backend              # Backend Docker configuration
├── PROJECT_DOCUMENTATION.md        # Complete project documentation
├── heart-disease-detection-frontend/  # Svelte frontend application
│   ├── src/                        # Frontend source code
│   ├── package.json                # Frontend dependencies
│   ├── Dockerfile                  # Frontend Docker configuration
│   └── docker-compose.yml          # Multi-container setup
```

## Option 1: Run with Docker (Recommended)

This is the easiest way to run the complete application with both frontend and backend services.

### Prerequisites
- Docker installed on your system

### Steps

1. **Navigate to the frontend directory:**
   ```bash
   cd heart-disease-detection-frontend
   ```

2. **Build and run both services:**
   ```bash
   docker-compose up --build
   ```

3. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - Backend API Documentation: http://localhost:8000/docs

4. **To stop the services:**
   Press `Ctrl+C` in the terminal, or run:
   ```bash
   docker-compose down
   ```

## Option 2: Run Services Separately

### Backend Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the backend server:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Verify the backend is running:**
   Open http://localhost:8000 in your browser. You should see:
   ```json
   {
     "message": "Heart Disease Detection API"
   }
   ```

### Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd heart-disease-detection-frontend
   ```

2. **Install frontend dependencies:**
   ```bash
   npm install
   ```

3. **Start the frontend development server:**
   ```bash
   npm run dev
   ```

4. **Access the frontend:**
   Open http://localhost:5173 in your browser.

## Option 3: Run Backend with Docker, Frontend Locally

1. **Start the backend with Docker:**
   ```bash
   docker build -t heart-disease-backend -f Dockerfile.backend .
   docker run -p 8000:8000 -v ${PWD}/heart_disease_dataset.csv:/app/heart_disease_dataset.csv heart-disease-backend
   ```

2. **Run the frontend locally:**
   ```bash
   cd heart-disease-detection-frontend
   npm install
   npm run dev
   ```

## Deploying to Render

This project includes a `render.yaml` configuration file for easy deployment to Render.

### Prerequisites
- A GitHub account
- A Render account (https://render.com)

### Deployment Steps

1. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/heart-disease-detection.git
   git push -u origin main
   ```

2. **Create services on Render:**
   - Go to your Render dashboard
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository
   - Render will automatically detect the `render.yaml` file
   - The configuration will create both frontend and backend services

3. **Configure environment variables (if needed):**
   - No additional environment variables are required for basic deployment

4. **Access your deployed application:**
   - Render will provide URLs for both services
   - Frontend: `https://your-service-name.onrender.com`
   - Backend: `https://your-service-name-api.onrender.com`

### Notes on Render Deployment

- The frontend is built using `npm install && npm run build` and served statically
- The backend uses Python with dependencies installed from `requirements.txt`
- Render automatically handles HTTPS and custom domains
- Automatic deploys are enabled when you push to your GitHub repository

## Using the Application

1. **Enter patient information** in the form:
   - Age (0-120)
   - Sex (Male/Female)
   - Chest Pain Type
   - Resting Blood Pressure
   - Cholesterol
   - Fasting Blood Sugar
   - Resting ECG Results
   - Max Heart Rate
   - Exercise Induced Angina
   - ST Depression
   - ST Slope
   - Number of Major Vessels
   - Thalassemia

2. **Click "Predict"** to get the heart disease prediction

3. **View the results** including:
   - Risk assessment (High/Low)
   - Model confidence score
   - Health recommendations

## API Endpoints

### Health Check
```
GET http://localhost:8000/
```

### Prediction
```
POST http://localhost:8000/predict
```

Example request body:
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

Example response:
```json
{
  "heart_disease": 1,
  "confidence": 0.87
}
```

## Troubleshooting

### Common Issues

1. **Port already in use:**
   - Change the port in the Dockerfile or docker-compose.yml
   - Or stop the process using the port:
     ```bash
     # Find process using port 8000
     netstat -ano | findstr :8000
     # Kill the process
     taskkill /PID <PID> /F
     ```

2. **CORS errors:**
   Already handled in the backend with CORS middleware.

3. **Model not found:**
   The application will automatically train and save a model if it doesn't exist.

4. **Connection refused:**
   Ensure both frontend and backend services are running.

### Development Tips

1. **Frontend development:**
   - The frontend uses Vite for hot reloading
   - Changes to Svelte components will automatically refresh in the browser

2. **Backend development:**
   - The backend uses uvicorn with hot reloading (--reload flag)
   - Changes to Python files will automatically restart the server

3. **Debugging:**
   - Check browser console for frontend errors
   - Check terminal output for backend errors
   - Use the FastAPI documentation at http://localhost:8000/docs for API testing

## Project Components

### Frontend (Svelte)
- **PredictionForm.svelte**: Patient data input form
- **PredictionResult.svelte**: Prediction results display
- **ModelInfo.svelte**: Model performance information
- **Header.svelte/Footer.svelte**: Page header and footer

### Backend (FastAPI)
- **main.py**: Main application with API endpoints
- **heart_disease_model.joblib**: Trained machine learning model (created automatically)
- **heart_disease_dataset.csv**: Dataset for training the model

## Machine Learning Model

The project uses a Random Forest classifier with the following performance metrics:
- Accuracy: ~85%
- Precision: ~87%
- Recall: ~84%
- F1-Score: ~85%

The model is automatically trained when the backend starts if it doesn't already exist.