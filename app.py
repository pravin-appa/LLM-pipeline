from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Vext API key to access LLM pipeline
api_key = 'XjyKjf51.5yrjeLpBvnGvuQq28BwO36pjLw1EPdnN'

# Headers
headers = {
    'Content-Type': 'application/json',
    'ApiKey': f'Api-Key {api_key}',
}

# Vext API URL
url = 'https://payload.vextapp.com/hook/E5GBCSEKCI/catch/$(pravin)'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/response', methods=['POST'])
def response():
    # Retrieve form data
    question = request.form.get('Question')
    
    # Create payload as a dictionary with a string value
    data = {
        "payload": question  # Ensure this is a string
    }
    
    # Send request to Vext API
    response = requests.post(url, json=data, headers=headers)
    response_json = response.json()
    output_text = response_json.get('text', 'No response text received.')
    
    return render_template("home.html", response_text=output_text)

if __name__ == '__main__':
    app.run(debug=True)
