from flask import render_template,request,redirect,url_for
from flask_login import login_user,logout_user
from . import auth
from app.models import Author

@auth.route("/register", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        form = request.form
        username = form.get("username")
        email = form.get("email")
        password = form.get("password")
        confirm_password = form.get("confirm_password")
        if username == None or email == None or password == None or confirm_password == None:
            error = "Username, email and passwords are required"
            return render_template("register.html", error=error)
        if " " in username:
            error = "Username should not have a space"
            return render_template("register.html", error=error)
        if " " in email:
            error = "Email address should not have a space"
            return render_template("register.html", error=error)
        if password != confirm_password:
            error = "Passwords do not match"
            return render_template("register.html", error=error)
        else:
            author = Author.query.filter_by(username=username).first()
            if author != None:
                error = "User with that username exists"
                return render_template("register.html", error=error)

            author = Author.query.filter_by(email=email).first()
            if author != None:
                error = "User with that email address exists"
                return render_template("register.html", error=error)

            author = Author(username=username, email=email)
            author.set_password(password)
            author.save_author()
            return redirect(url_for("auth.loginauthor"))
    return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def loginauthor():
    if request.method == "POST":
        form = request.form
        username = form.get("username")
        password = form.get("password")
        author = Author.query.filter_by(username=username).first()
        if author == None:
            error = "User with that username does not exist"
            return render_template("login.html", error=error)
        correct_password = author.check_password(password)
        if correct_password == False:
            error = "User with that username does not exist"
            return render_template("login.html", error=error)
        login_user(author)
        return render_template("index.html")
    return render_template("login.html")

@auth.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return render_template("home.html")
