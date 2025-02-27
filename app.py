from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registrar')
def registrar():
    return render_template('registrar.html')

@app.route('/recuperar')
def recuperar():
    return render_template('recuperar.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
