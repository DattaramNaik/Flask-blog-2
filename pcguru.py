from flask import Flask, render_template,request,redirect,sessions,send_file,flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message
from datetime import datetime
import json

with open('config.json','r') as c:         #json file accessing syntax
    parameter =json.load(c)["parameter"]



app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/pcserviceguru' #database mysql syntax
db = SQLAlchemy(app)
app.secret_key = "super-secret-key"

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USE_TLS = False,
    MAIL_USERNAME = parameter['gmail-user'],
    MAIL_PASSWORD=  parameter['gmail-password']
)
mail = Mail(app)

class contact_mail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(20), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(20), nullable=True)
    subject = db.Column(db.String(20), nullable=False)



@app.route('/', methods =['GET','POST'])
def home():
    if request.method =="POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        msg =request.form['message']

        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[parameter['gmail-user']],
                          body=msg + "\n" 'Contact no.: '+ phone + "\n" + email
                          )
        flash('Thanks For Submitting Your Details. We Get Back to You Soon.','success')
    return render_template('index.html',parameter=parameter)

@app.route('/about', methods =['GET','POST'])
def about():
    if request.method =="POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        msg =request.form['message']

        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[parameter['gmail-user']],
                          body=msg + "\n" 'Contact no.: '+ phone + "\n" + email
                          )
        flash('Thanks For Submitting Your Details. We Get Back to You Soon.', 'success')
    return render_template('about.html',parameter=parameter)


@app.route('/lapdesk', methods =['GET','POST'])
def lapdesk():
    if request.method =="POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        msg =request.form['message']

        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[parameter['gmail-user']],
                          body=msg + "\n" 'Contact no.: '+ phone + "\n" + email
                          )
        flash('Thanks For Submitting Your Details. We Get Back to You Soon.', 'success')
    return render_template('lapdes.html',parameter=parameter)

@app.route('/product', methods =['GET','POST'])
def product():
    if request.method =="POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        msg =request.form['message']

        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[parameter['gmail-user']],
                          body=msg + "\n" 'Contact no.: '+ phone + "\n" + email
                          )
        flash('Thanks For Submitting Your Details. We Get Back to You Soon.', 'success')
    return render_template('product.html',parameter=parameter)

@app.route('/cctv', methods =['GET','POST'])
def cctv():
    if request.method =="POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        msg =request.form['message']

        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[parameter['gmail-user']],
                          body=msg + "\n" 'Contact no.: '+ phone + "\n" + email
                          )
        flash('Thanks For Submitting Your Details. We Get Back to You Soon.', 'success')
    return render_template('cctv.html',parameter=parameter)

@app.route('/contact', methods =['GET','POST'])
def contact():
    if request.method =="POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        msg =request.form['message']

        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[parameter['gmail-user']],
                          body=msg + "\n" 'Subject: '+ subject + "\n" + email
                          )
        flash('Thanks For Submitting Your Details. We Get Back to You Soon.', 'success')

    return render_template('contact.html',parameter=parameter)

if __name__=="__main__":
    app.run(debug=True)