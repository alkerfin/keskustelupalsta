from flask import render_template,request
from app import app,db
from app.include.classes.category import *
from app.include.forms import CategoryForm
  
@app.route("/")
def frontpage():
    return render_template("frontpage.html",categories=Category.query.all())

@app.route("/category/")
def category_view():
    id = request.args.get("id")
    return render_template("category.html")

@app.route("/category/add/")
def addCategory():
    return render_template("add_category.html",form=CategoryForm(),success="none")

@app.route("/category/add/",methods=["POST"])
def addCategory_post():
    form = CategoryForm(request.form)
    c = Category(form.name.data,form.description.data,-1)

    if not form.validate()
	return render_template("add_category",form=form,success="none")

    db.session().add(c)
    db.session().commit()
    return render_template("add_category.html",success="block")

@app.route("/category/edit/")
def editCategory():
    id = request.args.get("id")
    return render_template("edit_category.html",success="none",category=Category.query.filter(Category.id==id).one_or_none())

@app.route("/category/edit/",methods=["POST"])
def editCategory_post():
    id = request.args.get("id")
    c = Category.query.get(id)
    c.topic = request.form.get("topic")
    c.description = request.form.get("description")
    db.session().add(c)
    db.session().commit()
    return render_template("edit_category.html",success="block",category=Category.query.filter(Category.id==id).one_or_none())

@app.route("/thread/")
def thread():
    id = request.args.get("id")
    return render_template("thread.html")

@app.route("/message/add")
def sendMessage():
    parent = request.args.get("parent")
    return render_template("index.html")

@app.route("/message/edit")
def editMessage():
    return render_template("index.html")

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/signup/")
def signup():
    return render_template("signup.html")


@app.route("/demo")
def content():
    return render_template("demo.html", nimi=nimi, lista=lista, esineet=esineet)

