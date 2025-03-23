from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Tambahkan logika autentikasi di sini
        if username == 'admin' and password == 'password':
            return redirect(url_for('home'))
        else:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)