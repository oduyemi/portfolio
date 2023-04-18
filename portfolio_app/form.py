from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, length, Regexp, Email
from portfolio_app.models import Msg

class ContactForm(FlaskForm):
    username = StringField("username",
        validators=[
            DataRequired(),
            length(min=2, max=30, message = "Please provide a valid name"),
            Regexp(
                "^[A-Za-z]  [A-Za-z.]*", 0, "Your Last name must contain only letters")],
        render_kw={"placeholder": "Your name"})

    email = StringField("email",
        validators=
            [DataRequired(),
            Email(),
            Regexp('[a-z0-9]+@[a-z]+.[a-z]{2,3}', 0, "Please provide a valid email address")],
            render_kw={"placeholder": "Your email"})

    subject = StringField("subject",
        validators=[
            DataRequired(),
            length(min=2, max=50, message = "Please provide a valid name")],
        render_kw={"placeholder": "Subject"})

    msg = TextAreaField("msg",
        validators=[
            DataRequired(),
            length(min=2, max=1000, message = "Please provide a valid name")],
        render_kw={"placeholder": "Message"})
    

    submit = SubmitField("Send Message")
    


class LoginForm(FlaskForm):
    username = StringField("email",
        validators=
            [DataRequired(),
            length(min=6, max=30),
            Email(),
            Regexp('[a-z0-9]+@[a-z]+.[a-z]{2,3}', 0, "Please provide a valid email address")],
            render_kw={"placeholder": "Enter your email address"})
    
    password = PasswordField("password",
        validators=
            [DataRequired(),
            length(min=8, max=20)],
            render_kw={"placeholder": "Enter your password"})
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class AdminMessage(FlaskForm):
    message = TextAreaField("message",
    validators=
    [DataRequired(),
    length(min=5, max=1000)],
    render_kw={"placeholder": "Your comment here..."})
    
    submit = SubmitField("Work on it")

