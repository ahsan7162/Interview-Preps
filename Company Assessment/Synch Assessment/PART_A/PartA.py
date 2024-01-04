import time
import random
from typing import Dict
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock model prediction function
def mock_model_predict(input: str) -> Dict[str, str]:
    time.sleep(random.randint(8, 15)) # Simulate processing delay
    result = str(random.randint(100, 10000))
    output = {"input": input, "result": result}
    return output

# POST endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get user input data from the request
            user_input = request.json.get('input_data')

            # Check if input data is provided
            if user_input is None:
                return jsonify({'error': 'Input data is missing'}), 400

            # Invoke the mock_model_predict function
            prediction_result = mock_model_predict(user_input)

            # Return the prediction result with a 200 status code
            return jsonify({'prediction': prediction_result}), 200

        except Exception as e:
            # Handle any exceptions that may occur during prediction
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on localhost:8080
    app.run(port=8080)