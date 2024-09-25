from flask import Flask, jsonify
import requests

topic = 'pizza'

r = requests.get(f'https://newsdata.io/api/1/latest?apikey=pub_544064f4ed63ce81c7478f27000f5d3ce1caf&q={topic}')

app = Flask(__name__)

@app.route('/')
def get_api():
    response = {'result': r.json()}
    return jsonify(response)
app.run(port=5000)