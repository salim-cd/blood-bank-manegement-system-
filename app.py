from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Implement your user authentication here (e.g., checking against a database)
        return redirect(url_for('index'))  # Redirect after login
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')  # You can add a registration form

if __name__ == '__main__':
    app.run(debug=True)
