from flask import Flask, flash, redirect, render_template, \
     request, url_for

import IPython

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/putfile', methods=['GET', 'POST'])
def putfile():
    if request.method == 'POST':
        print request.data
        print request.files
        return 'hi'
    # IPython.embed()
    return render_template('putfile.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
           request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
