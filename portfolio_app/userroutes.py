from flask import render_template, request, flash
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length, ValidationError, Regexp, Email
from werkzeug.exceptions import HTTPException
from portfolio_app.models import Msg, Status
from portfolio_app.form import ContactForm

from portfolio_app import starter, db


@starter.route('/', methods = ["GET", "POST"], strict_slashes = False)
def home():
    form=ContactForm()
    if request.method == "GET":
        return render_template('user/index.html',form = form)
    else:
        name=request.form.get("username")
        mail=request.form.get("email")
        subject=request.form.get("subject")
        message=request.form.get("msg")
        if name !='' and mail != "" and subject !='' and message !='':
            new_msg = Msg(msg_username=name, msg_email=mail, msg_subject=subject, msg_content=message,msg_status_id=1)
            db.session.add(new_msg)
            db.session.commit()
            flash("Thank you for reaching out, I will get back to you shortly", "success")
            return render_template('user/index.html', form = form)
        else:
            flash('You must fill the form correctly to signup', "danger")

 