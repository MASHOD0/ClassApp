from flask import Flask, render_template, request, session, redirect, url_for, flash
from datetime import datetime 
from FileHandler import db, queries

conn = db.ClassesDB_Connect()

#starting the app
app = Flask(__name__)

#session requires ou to have a secret key
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
    return render_template('home.html')

    









if __name__ == "__main__":
    app.run(debug=True)