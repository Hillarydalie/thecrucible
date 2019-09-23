from flask import render_template, url_for,request,redirect
from flask_login import login_required,current_user
from . import main
from .. import db
from ..models import Blog
from datetime import datetime

@main.route("/")
@login_required
def homepage():
    blogs = Blog.query.all()
    return render_template(("index.html"), blogs=blogs)

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
    print(blogpost,'********')
    return render_template('details.html', blogpost = blogpost)