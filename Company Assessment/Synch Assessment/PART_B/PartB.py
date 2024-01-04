from flask import Flask, request, jsonify
import threading
import queue
import uuid
import time
import random
from typing import Dict

app = Flask(__name__)

# Dictionary to store asynchronous results
results_dict = {}
#queue for managing incoming requests
results_queue = queue.Queue()




def process_async_predictions():
    while True:
        try:
            # Retrieve a prediction task from the queue
            # As the method remove item from queue when its processing so you might get id not found in return when its getting processed by async predict it is default behaviour so I am not chainging the behaviour
            prediction_id, input_data = results_queue.get()

            # Check if it's a termination signal
            if prediction_id is None and input_data is None:
                break

            # Perform the asynchronous prediction
            async_predict(input_data, prediction_id)

        except Exception as e:
            print(f"Error processing async prediction: {str(e)}")

# Start the continuous processing thread
processing_thread = threading.Thread(target=process_async_predictions)
processing_thread.start()

# Mock model prediction function
def mock_model_predict(input: str) -> Dict[str, str]:
    time.sleep(random.randint(8, 15)) # Simulate processing delay
    result = str(random.randint(100, 10000))
    output = {"input": input, "result": result}
    return output

# Function for asynchronous prediction
def async_predict(input_data, prediction_id):
    result = mock_model_predict(input_data)
    # Save the result for later retrieval
    results_dict[prediction_id] = result

# POST endpoint for prediction (synchronous or asynchronous)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input data from the request
        user_input = request.json.get('input_data')

        # Check if input data is provided
        if user_input is None:
            return jsonify({'error': 'Input data is missing'}), 400

        # Check if the request is asynchronous
        async_mode = request.headers.get('Async-Mode', '').lower() == 'true'

        if async_mode:
            # Generate a unique prediction_id
            prediction_id = str(uuid.uuid4())

            # Start the asynchronous prediction task in a separate thread
            results_queue.put((prediction_id, None))
            # Respond to the user with a 202 status code and the prediction_id
            response_data = {
                'message': 'Request received. Processing asynchronously.',
                'prediction_id': prediction_id
            }
            return jsonify(response_data), 202
        else:
            # If synchronous, perform the prediction immediately
            prediction_result = mock_model_predict(user_input)
            return jsonify({'prediction': prediction_result}), 200

    except Exception as e:
        # Handle any exceptions that may occur during prediction
        return jsonify({'error': str(e)}), 500

# Endpoint to retrieve asynchronous prediction result
@app.route('/predict/<prediction_id>', methods=['GET'])
def get_result(prediction_id):
    result = results_dict.get(prediction_id)

    if result:
        return jsonify({'prediction_id': prediction_id, 'result': result}), 200
    elif (prediction_id, None) in results_queue.queue:
        # If the prediction is still being processed
        return jsonify({'error': 'Prediction is still being processed.'}), 400
    else:
        # If the prediction ID is not valid
        return jsonify({'error': 'Prediction ID not found.'}), 404

if __name__ == '__main__':
    # Run the Flask app on localhost:8080
    app.run(port=8080)