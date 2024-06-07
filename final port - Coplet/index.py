from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Here you can add logic to handle the form data, such as sending an email or saving to a database
    print(f"Received message from {name} ({email}): {message}")
    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)
