from flask import render_template,request
from app import app,db
from app.include.classes.category import *
from app.include.classes.message import *
from app.include.forms import CategoryForm,WriteMessage,WriteTopic
  
@app.route("/")
def frontpage():
    return render_template("frontpage.html",categories=Category.query.all())

@app.route("/category/")
def category_view():
    id = request.args.get("id")
    messages = Message.query.filter_by(msg_parent=-1).all()
    return render_template("category.html",messages=messages)

@app.route("/category/add/")
def addCategory():
    form = CategoryForm()
    return render_template("add_category.html",form=CategoryForm(),success="none")

@app.route("/category/add/",methods=["POST"])
def addCategory_post():
    form = CategoryForm(request.form)
    c = Category(form.name.data,form.description.data,-1)

    if not form.validate():
        return render_template("add_category.html",form=form,success="none")

    db.session().add(c)
    db.session().commit()
    return render_template("add_category.html",success="block",form=form)

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
    pagenm = request.args.get("page")
    messages = Message.query.filter_by(msg_parent=id).all()
    return render_template("thread.html",Form=WriteMessage(),id=id,messages=messages)

@app.route("/thread/add/")
def threadAdd():
    id = request.args.get("id")
    return render_template("add_thread.html",form=WriteTopic())

@app.route("/thread/add/",methods=["POST"])
def threadAdd_post():
    id = request.args.get("id")
    form = WriteTopic(request.form)
    m = Message(id,-1,-1,form.topic.data,form.body.data)

    if not form.validate():
        return render_template("add_thread.html",form=form,success="none")

    db.session().add(m)
    db.session().commit()    
    return render_template("add_thread.html",form=WriteTopic(),success="block")

@app.route("/message/add",methods=["POST"])
def sendMessage_post():
    form = WriteMessage(request.form)
    parent = request.args.get("parent")
    m = Message(-99,parent,-1,form.topic.data,form.body.data)

    if not form.validate():
       return redirect("")

    db.session().add(m)
    db.session().commit()
    return redirect("/thread/?id="+parent)

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

