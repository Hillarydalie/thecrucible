from flask import render_template, url_for,request,redirect
from flask_login import login_required,current_user
from . import main
from .. import db
from ..models import Author,Blog,Blogcomment
from datetime import datetime
from app.requests import getQuotes

@main.route("/home")
@login_required
def homepage():
    quote = getQuotes()
    another_quote = getQuotes()
    blogs = Blog.query.all()
    return render_template(("index.html"), blogs=blogs, quote = quote,another_quote = another_quote)

@main.route("/newblog")
@login_required
def newblog():
    return render_template(("blogpost.html"))

@main.route("/blog", methods=["GET", "POST"])
@login_required
def new_blog():
    if request.method == "POST":
        form = request.form
        title = form.get("blogtitle")
        blogcontent = form.get("blogpost")
        blog = Blog(title=title, description=blogcontent, author=current_user)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for("main.newblog"))
    return render_template("index.html/home")

@main.route('/blog/details/<blog_id>')
@login_required
def blog_details(blog_id):
    blogpost = Blog.query.filter_by(id=blog_id).first()
    blogcomment = Blogcomment.query.filter_by(id = blog_id).all()
    return render_template('details.html', blogpost = blogpost)

@main.route("/comment/save/<blogcomment_id>", methods=["GET","POST"])
@login_required
def save_comments(blogcomment_id):
    if request.method == "POST":
        content = request.form.get("content")
        new_comment = Blogcomment(content=content, author=current_user, post_id=blogcomment_id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for("main.blog_details", blog_id=blogcomment_id))

@main.route("/comment/delete/<blogcomment_id>")
@login_required
def delete_comment(blogcomment_id):
    if request.method == "POST":
        blogcomment = Blogcomment.query.filter_by(id = blogcomment_id).first()
        new_comment = Blogcomment(content=content, author=current_user, post_id=blogcomment_id)
        db.session.delete(new_comment)
        db.session.commit()
        return render_template("main.blog_details", blog_id=blogcomment_id)

@main.route("/profile", methods=["GET", "POST"])
@login_required
def load_profile():
    return render_template("profile.html")