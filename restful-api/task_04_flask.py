#!/usr/bin/python3
"""
Simple API development using Flask.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store user data in memory
users = {}


@app.route("/")
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all usernames"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns the status of the API"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for a specific user"""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user to the users dictionary"""
    # Parse JSON data
    data = request.get_json(silent=True)
    
    # Validation: Valid JSON
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    # Validation: Username presence
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # Validation: Username uniqueness
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # Add user and return success
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
