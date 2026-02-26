from flask import Flask, render_template, jsonify
import random
import os

app = Flask(__name__)

# List of meals with their image paths
meals = [
    {'name': 'Pizza', 'image': 'images/pizza.jpg'},
    {'name': 'Burger', 'image': 'images/burger.jpg'},
    {'name': 'Sushi', 'image': 'images/sushi.jpg'},
    {'name': 'Ramen', 'image': 'images/ramen.jpg'},
    {'name': 'Dürüm', 'image': 'images/durum.jpg'},
    {'name': 'Dumplings', 'image': 'images/dumplings.jpg'},
    {'name': 'Sweets', 'image': 'images/sweets.jpg'}
]

@app.route('/')
def home():
    """Display the main page"""
    return render_template('index.html')

@app.route('/pick-meal')
def pick_meal():
    """Return a random meal as JSON"""
    selected_meal = random.choice(meals)
    return jsonify(selected_meal)

if __name__ == '__main__':
    app.run(debug=True)
