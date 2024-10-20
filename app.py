from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quote')
def quote():
    #response = requests.get('https://api.quotable.io/random')
    response = requests.get('https://api.quotable.io/random', verify=False)

    quote_data = response.json()
    return jsonify(quote=quote_data['content'], author=quote_data['author'])

if __name__ == '__main__':
    app.run(debug=True)
