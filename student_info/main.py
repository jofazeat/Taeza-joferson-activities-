from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import hashlib

app = Flask(__name__)

# Flask MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'student_info_sys'

SALT = 'qwertyuiod123456'  # You should use a more secure and secret value

mysql = MySQL(app)
app.secret_key = '8799855785'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['POST'])
def check_user():
    try:
        username = request.form['username']
        password = request.form['password']

        # Hash password with salt
        salted = (SALT + password).encode('utf-8')
        hashed_password = hashlib.sha512(salted).hexdigest()

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, hashed_password))
        user = cur.fetchone()
        cur.close()

        if user:
            return render_template('home.html')  # Or redirect to another secure page
        else:
            flash('Invalid username or password')
            return redirect(url_for('index'))

    except Exception as e:
        flash(f"An error occurred: {str(e)}")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
