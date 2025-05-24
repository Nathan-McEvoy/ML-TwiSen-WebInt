# ML Text Sentiment Web App

A web-integrated machine learning application that analyzes the sentiment of user-provided text, classifying it as
Positive, Neutral, Negative, or Irrelevant.

## Overview
This project consists of a Flask backend that serves a linear algorithm machine learning model for text sentiment
analysis and a React frontend that provides a user interface to input text and display the predicted sentiment.
The backend uses a pre-trained model (`twitter_training.pkl`) with text preprocessing, and the frontend allows users
to enter text via a textarea and view results.

## Features
- **Backend**: Flask API with a single POST endpoint (`/api/text-sentiment`) for sentiment prediction.
- **Frontend**: React app with a textarea for text input, a submit button, and a display for the sentiment result.
- **Model**: Pre-trained machine learning model for classifying text sentiment.
- **CORS**: Configured to allow communication between the frontend (`http://localhost:5173`) and backend (`http://localhost:5000`).

## Prerequisites
- **Python 3.8+**: For running the Flask backend.
- **Node.js 16+**: For running the React frontend.
- **pip** and **npm**: For installing dependencies.

## Backend Setup
1. Navigate to the `backend/` directory:
   ```bash
   cd backend
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the Flask server:
   ```bash
   python app.py
The backend will run on http://localhost:5000 by default

## Frontend Setup
1. Navigate to the `frontend/` directory:
   ```bash
   cd frontend
2. Install dependencies:
   ```bash
   npm install
3. Run the React development server:
   ```bash
   npm run dev
The frontend will run on http://localhost:5173 (Vite default)

## Usage
1. Open your browser to http://localhost:5173.
2. Enter text in the textarea (e.g., "I love this!").
3. Click the "Submit" button to send the text to the backend.
4. View the predicted sentiment (e.g., "Positive") displayed above the textarea.

## API Details
- Endpoint: POST /api/text-sentiment
- Request Body: JSON object { "text": "your input text" }
- Response: JSON object { "result": "Positive" } (or Neutral, Negative, Irrelevant)
- Example:
   ```bash
  curl -X POST http://localhost:5000/api/text-sentiment -H "Content-Type: application/json" -d '{"text":"I love this!"}'
  
## Development Notes
- The backend uses flask-smorest for API structure and flask-cors for cross-origin requests.
- The frontend uses TypeScript (App.tsx) with a typed SentimentResponse interface for the API response.
- The machine learning model is loaded from ml_data/twitter_training.pkl and preprocesses text using a custom text_preprocessing module.

## Troubleshooting
- CORS Issues: Ensure the Flask server is running and CORS is configured for http://localhost:5173.
- API Errors: Check the Flask console for errors (e.g., model prediction issues) and verify the input text is valid.
- Frontend Errors: Use browser DevTools (F12 > Network/Console) to debug API requests or rendering issues.

## Future Improvements
- Greater tweaking for a higher model prediction accuracy.
- Enhance the UI with styling (e.g., Tailwind CSS).
- (?)Include a history of previous sentiment predictions.

## Credits
- The training and validation data used are from: https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis
- This README was written with AI (Grok) assistance

## Notes
As of writing, the above setup steps have yet to be tested