import logging
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
#import worker  # Import the worker module
import worker2  # Import the worker module

# Initialize Flask app and CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.logger.setLevel(logging.ERROR)

# Define the route for the index page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')  # Render the index.html template

# Define the route for processing messages
@app.route('/process-message', methods=['POST'])
def process_message_route():
    try:
        user_message = request.json['userMessage']  # Extract the user's message from the request
        app.logger.debug(f'User message: {user_message}')
        print('user_message', user_message)

        #bot_response = worker.process_prompt(user_message)  # Process the user's message using the worker module
        bot_response = worker2.process_prompt(user_message)  # Process the user's message using the worker module
        app.logger.debug(f'Bot response: {bot_response}')

        # Return the bot's response as JSON
        return jsonify({
            "botResponse": bot_response
        }), 200    
    except Exception as e:
        error_message = f"Error processing message: {e}"
        app.logger.error(error_message)
        return jsonify({
            "botResponse": error_message
        }), 500

# Define the route for processing documents
@app.route('/process-document', methods=['POST'])
def process_document_route():
    try:
        # Check if a file was uploaded
        if 'file' not in request.files:
            error_message = "File not uploaded correctly."
            app.logger.error(error_message)

            return jsonify({
                "botResponse": "It seems like the file was not uploaded correctly, can you try "
                            "again. If the problem persists, try using a different file"
            }), 400

        file = request.files['file']  # Extract the uploaded file from the request

        file_path = file.filename  # Define the path where the file will be saved
        file.save(file_path)  # Save the file

        #worker.process_document(file_path)  # Process the document using the worker module
        worker2.process_document(file_path)  # Process the document using the worker module
        app.logger.debug('Document processed successfully.')

        # Return a success message as JSON
        return jsonify({
            "botResponse": "Thank you for providing your PDF document. I have analyzed it, so now you can ask me any "
                        "questions regarding it!"
        }), 200
    except Exception as e:
        error_message = f"Error processing document: {e}"
        app.logger.error(error_message)
        return jsonify({
            "botResponse": error_message
        }), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')
