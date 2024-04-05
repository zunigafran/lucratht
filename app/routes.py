from flask import request, jsonify
from app import app
from app.openai_integration import generate_text

# Welcome route
@app.route('/welcome')
def welcome():
    return "Welcome to the NLP application! You can ask questions on the homepage."

@app.route('/homepage', methods=['POST'])
def homepage():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON data received'}), 400

    question = data.get('question', '')
    if question:
        # Process the question
        # For demonstration, let's just return the question back to the user
        response = {'response': f"You asked: '{question}'"}

        return jsonify(response), 200
    else:
        return jsonify({'error': 'Question is required'}), 400
