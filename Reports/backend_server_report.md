# Backend Server Report

## Project Title
AI-Based Student Performance Prediction

## Objective
To develop a backend server that receives student information and returns predicted student performance through API endpoints.

## Technology Used
- Python
- Flask
- JSON

## API Endpoints

### 1. Home Route
Endpoint: /
Method: GET

Purpose:
Checks whether the backend server is running.

### 2. Health Check
Endpoint: /api/health
Method: GET

Purpose:
Verifies that the backend server is working properly.

### 3. Prediction API
Endpoint: /api/predict
Method: POST

Purpose:
Receives student details and returns the predicted performance.

## JSON Response

Example:

```json
{
    "status": "success",
    "prediction": "Good Performance"
}
```

## Conclusion

The backend server successfully provides API endpoints for the AI-Based Student Performance Prediction system.
