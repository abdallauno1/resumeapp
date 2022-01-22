from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import smtplib


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mady.db'
# app.run(host="localhost", port=5050, debug=True)
# INIT THE DATABASE
db = SQLAlchemy(app)

#create data base model
class Mady(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(200), nullable=False)
    lname = db.Column(db.String(200), nullable=False)
    mail = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

#create a function to return a string when we add something

    def __repr__(self):
        return '<Name %r>' % self.id



@app.route('/')
def index():
    title = "Mady Abdalla"
    return  render_template("index.html" ,title = title)


@app.route('/form', methods=["POST"])
def form():
    title = "Contact"
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
   # sending mail
    """
    msg = "Thanks, You have been subsribed to my newsletter..."
    server = smtplib.SMTP("smtp.gmail",587)
    server.starttls()
    server.login("mail_adress","password") # enter your email address & password
    server.sendmail("mail_adress", email, msg)
    """
    if not first_name or not last_name or not email:
        error_msg = " Sorry Contacting faild, all fields are required! "
        return render_template("/Contact.html" , title=title ,error_msg=error_msg)

    return  render_template("form.html",title=title,first_name=first_name,last_name=last_name,email=email)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000)