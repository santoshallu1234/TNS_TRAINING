# Heart Disease Detection Frontend

This is a Svelte frontend application for the Heart Disease Detection project. It provides a user-friendly interface for healthcare professionals to input patient data and receive heart disease predictions based on machine learning models.

## Features

- Patient data input form with validation
- Prediction results display with risk assessment
- Model performance comparison
- Responsive design for various screen sizes

## Project Structure

```
src/
├── App.svelte          # Main application component
├── app.css             # Global styles
├── main.js             # Application entry point
└── lib/
    └── components/
        ├── Header.svelte         # Application header
        ├── Footer.svelte         # Application footer
        ├── PredictionForm.svelte # Patient data input form
        ├── PredictionResult.svelte # Prediction results display
        └── ModelInfo.svelte      # Model performance information
```

## Setup Instructions

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

3. Build for production:
   ```bash
   npm run build
   ```

## Integration with FastAPI Backend

To connect this frontend with your FastAPI backend:

1. Update the `handlePredict` function in `App.svelte` to make actual API calls instead of mock data:

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

2. Make sure your FastAPI backend is running on `http://localhost:8000`

## Components

### PredictionForm.svelte
- Collects patient data through a comprehensive form
- Validates input data
- Emits a `predict` event with the form data

### PredictionResult.svelte
- Displays prediction results
- Shows risk assessment (high/low)
- Provides confidence score
- Offers health recommendations based on the prediction

### ModelInfo.svelte
- Displays performance metrics for different ML models
- Explains key performance indicators

## Styling

The application uses CSS modules for component styling and follows a consistent color scheme:
- Primary color: #e74c3c (Alizarin Crimson) for actions and highlights
- Secondary colors: Various shades of grays and blues for backgrounds and text
- Responsive design that works on mobile, tablet, and desktop

## Development

This project uses Vite as the build tool and development server. For more information, refer to the [Vite documentation](https://vitejs.dev/).

## Docker Integration

To containerize this frontend application:

1. Create a Dockerfile:
```dockerfile
# Use Node.js 16 as base image
FROM node:16

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY . .

# Build the application
RUN npm run build

# Install serve to run the static files
RUN npm install -g serve

# Expose port
EXPOSE 3000

# Run the application
CMD ["serve", "-s", "dist", "-l", "3000"]
```

2. Build and run the Docker container:
```bash
docker build -t heart-disease-frontend .
docker run -p 3000:3000 heart-disease-frontend
```