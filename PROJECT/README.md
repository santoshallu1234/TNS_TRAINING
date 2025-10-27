# Heart Disease Detection Project

This is a capstone project for detecting heart disease using machine learning algorithms.

## Project Structure

- `heart-disease-detection-frontend/` - Svelte frontend application
- `main.py` - Python FastAPI backend
- `requirements.txt` - Python dependencies
- `heart_disease_dataset.csv` - Dataset for training the model
- `heart_disease_model.joblib` - Pre-trained machine learning model

## Deployment to Render

This project is configured for deployment to Render using the `render.yaml` file. The configuration defines two services:

1. **Frontend Service** - Svelte application served statically
2. **Backend Service** - Python FastAPI application

To deploy:

1. Fork this repository to your GitHub account
2. Create a new Web Service on Render
3. Connect your forked repository
4. Select the branch to deploy
5. Render will automatically detect the `render.yaml` file and deploy both services

The services will be available at:
- Frontend: `https://your-render-app-name.onrender.com`
- Backend API: `https://your-render-app-name-api.onrender.com`

## Local Development

See [HOW_TO_RUN.md](HOW_TO_RUN.md) for instructions on running the project locally.

## Documentation

- [Project Summary](PROJECT_SUMMARY.md)
- [Project Documentation](PROJECT_DOCUMENTATION.md)
- [Capstone Project Deliverables](CAPSTONE_PROJECT_DELIVERABLES.md)
- [Frontend Presentation](heart-disease-detection-frontend/PROJECT_PRESENTATION.md)