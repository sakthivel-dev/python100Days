from flask import Flask, render_template,request,redirect,url_for
import sqlite3 

app=Flask(__name__)
app.config['MYSQL_DB'] = 'flask'
# mysql = MySQL(app)

conn = sqlite3.connect('example.db',check_same_thread=False)
cursor = conn.cursor()

# Creating a Table and Inserting Data:
# You can create a table and insert data into it using SQL commands:
# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        firstName TEXT,
        lastName TEXT,
        age INTEGER,
        mailId TEXT,
        password TEXT
        )
""")
               
@app.route('/')
def home():
    return "Welcome to the home page!"

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        print(request)
        firstName=request.form['firstname']
        lastName=request.form['lastname']
        mailId=request.form['email']
        password=request.form['password']
        age=request.form['age']
        cursor.execute("INSERT INTO Users (firstName, lastName, age, mailId, password) VALUES (?, ?, ?, ?, ?)", (firstName, lastName, age, mailId, password))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    
    return render_template('signup.html')

if __name__ == '__main__':
    app.run()
