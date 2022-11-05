from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/solution')
def solution():
    return render_template('solution.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

app.run(debug=True)