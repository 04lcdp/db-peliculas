from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['db']
collection = db['peliculas']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/peliculas')
def get_peliculas():
    peliculas = list(collection.find({}, {'_id': 0}))  # Obtener todas las películas sin el _id de MongoDB
    return jsonify(peliculas)

if __name__ == '__main__':
    app.run(debug=True)
