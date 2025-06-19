from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'example'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/resume')
def resume():
    return render_template('resume.html')
@app.route('/services')
def service():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO messages (name, email, message, submitted_at) VALUES (%s, %s, %s, %s)",
                    (name, email, message, datetime.now()))
        mysql.connection.commit()
        cur.close()

        return render_template('success.html')
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
