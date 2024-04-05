# Lucra Take Home Test

## NLP Application

This is a Flask-based backend system that provides API endpoints for various natural language processing (NLP) tasks using OpenAI's API.

### Setup

To set up and run this application locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/nlp-application.git
   cd nlp-application
   ```

2. **Install Dependencies**:

   ```
   pip install -r requirements.txt
   ```
   
3. **Set Environment Variables**:
   If you haven't already, set your OpenAI API key as an environment variable:

   ```
   export OPENAI_API_KEY="your_openai_api_key_here"
   ```
   
4. **Run the Application**:
   ```
   python run.py
   ```
   The application will start running on http://localhost:5000/.

### API Documentation
#### Welcome Route
URL: /welcome
Method: GET
Description: Returns a welcome message for the NLP application.
Response: Returns a string message: "Welcome to the NLP application! You can ask questions on the homepage."

#### Homepage Route
URL: /homepage
Method: POST
Description: Accepts a question in the request body and processes it.
Request Body:
```json
{
    "question": "Your question goes here"
}
```
Response:
```json
{
    "response": "Processed response based on the question"
}
```
### Example Usage
#### Welcome Route
```bash
curl http://localhost:5000/welcome
```

Response:
```bash
Welcome to the NLP application! You can ask questions on the homepage.
```

#### Homepage Route
```bash
curl -X POST -H "Content-Type: application/json" -d '{"question": "What is the capital of France?"}' http://localhost:5000/homepage
```

Response:
```json
{
    "response": "You asked: 'What is the capital of France?'"
}
```

#### Notes
- Replace your_openai_api_key_here with your actual OpenAI API key.
- This README assumes you have Python and pip installed on your system.
- Ensure that your OpenAI API key has proper permissions to use the required endpoints.
- This application is for demonstration purposes and may require additional configuration for production use.
