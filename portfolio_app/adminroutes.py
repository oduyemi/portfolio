from flask import render_template,request,redirect,session,url_for
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash,check_password_hash
from portfolio_app import starter, db
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length, ValidationError, Regexp, Email
from werkzeug.exceptions import HTTPException
from portfolio_app.models import Msg, Admin
from portfolio_app.form import LoginForm, AdminMessage



from portfolio_app import starter

@starter.route("/admin/login", methods = ["GET", "POST"], strict_slashes = False)
def login():
    form = LoginForm()
    if request.method=='GET':
        return render_template('admin/adminlogin.html', title="Login", form=form)
    else:
        if form.validate_on_submit:
            username = form.username.data
            password = form.password.data
            #hashed = generate_password_hash(password)
            if username !="" and password !="":
                user = db.session.query(Admin).filter(Admin.admin_username==username, Admin.admin_password==password).first() 
                adminid = user.admin_id
                session["_admin"] = adminid
                return redirect(url_for('dashboard'))


@starter.route("/admin/logout", strict_slashes = False)
def adminlogout():
    if session.get("_admin") != None:
        session.pop("_admin",None)
    return redirect('/admin/login')     


@starter.route("/admin/dashboard", methods = ["GET", "POST"], strict_slashes = False)
def dashboard():
    form=AdminMessage()
    message = form.message.data
    
    if session.get('_admin') != None:
        mdeets = db.session.query(Msg).filter(Msg.msg_status_id==1).all()
        
        if request.method == 'GET':
            return render_template("admin/admindashboard.html", mdeets=mdeets, form=form)
    else:
        return redirect("/admin/login")


@starter.route('/admin', methods = (["GET", "POST"]), strict_slashes = False)
def adminhome():
    if request.method == 'GET':
        return redirect(url_for("login"))
    else:
        username =request.form.get('username')
        pwd=request.form.get('pwd')
        if username != "" or pwd !="":
            loggedin = Admin(admin_username=username, admin_password=pwd)
            db.session.add(loggedin)
            db.session.commit()
            return redirect('/admin/login')


@starter.route("/admin/email_purse", strict_slashes = False)
def email():
    if session.get('_admin') != None:
        mdeets=db.session.query(Msg).all()
        return render_template('admin/email.html',mdeets=mdeets)


@starter.route("/admin/messages_in_view", strict_slashes = False)
def in_view():
    if session.get('_admin') != None:
        mdeets=db.session.query(Msg).where(Msg.msg_status_id==2).all()
        return render_template('admin/inview.html',mdeets=mdeets)


@starter.route("/admin/messages_sorted", strict_slashes = False)
def sorted():
    if session.get('_admin') != None:
        mdeets=db.session.query(Msg).where(Msg.msg_status_id==3).all()
        return render_template('admin/sorted.html',mdeets=mdeets)


@starter.route("/delete/<int:id>", strict_slashes = False)
def delete(id): 
    item=Msg.query.get_or_404(id)
    try:
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('dashboard'))
        
    except:
        return redirect(url_for('dashboard'))


@starter.route("/update/<user>", methods = ["Get", "POST"], strict_slashes = False)
def work_on_it(user):
    query=f"UPDATE msg SET msg_status_id=2 WHERE '{user}'=msg_id"
    db.session.execute(text(query))
    db.session.commit()
    return redirect(url_for("in_view"))

@starter.route("/sorted/<messages>", methods = ["Get", "POST"], strict_slashes = False)
def sorted_msg(messages):
    sort=f"UPDATE msg SET msg_status_id=3 WHERE '{messages}'=msg_id"
    db.session.execute(text(sort))
    db.session.commit()
    return redirect(url_for("sorted"))
    
    


