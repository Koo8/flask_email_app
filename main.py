from flask import Flask, request, render_template
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextField
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = "averYHardTOguessSTring"
bootstrap = Bootstrap(app)


app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = "happycodeeveryday@gmail.com"
app.config['MAIL_PASSWORD'] = "gymtogocoit"

mail = Mail(app)

class EmailForm(FlaskForm):
    email = StringField("What is your email")
    body = TextField()
    submit = SubmitField("Submit")

@app.route('/', methods=["POST", "GET"])
def index():
    form = EmailForm()
    email = request.form.get('email')
    print('email : ' + email)
    body = request.form.get('body')
    print('body:' + body)
    if email is not None and body is not None:
        msg = Message("Changed Message", sender="change this email address",recipients=[email])
        msg.body = body
        mail.send(msg)
        form.email.data = ""
        form.body.data = ""

    return render_template('index.html',form = form)

if __name__ == "__main__":
    app.run(debug=True)