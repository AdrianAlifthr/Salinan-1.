import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Configure API key for Google Generative AI
genai.configure(api_key="AIzaSyAv5YmcpdWtw-9CE5B1SnlalMJ0igHV8Wg")

# Create the model with configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Create a Flask app
app = Flask(__name__)

# Function to generate response
def GeneratedResponse(input_text):
    response = model.generate_content([
        "kamu adalah BOTO bot pariwisata sumatera utara, jadi jawab dengan demikian",
        f"input: {input_text}",
        "output: ",
    ])
    return response.text

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for generating the bot response
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    bot_response = GeneratedResponse(user_input)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
