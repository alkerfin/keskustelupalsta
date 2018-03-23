from flask import Flask,render_template
app = Flask(__name__)
  
class Item:
    def __init__(self, name):
        self.name = name

nimi = "Essi Esimerkki"

lista = [1, 1, 2, 3, 5, 8, 11]

esineet = []
esineet.append(Item("Eka"))
esineet.append(Item("Toka"))
esineet.append(Item("Kolmas"))
esineet.append(Item("Neljäs"))
  
@app.route("/")
def frontpage():
    return render_template("frontpage.html")

@app.route("/category/:id")
def category():
    return render_template("category.html")

@app.route("/category/add")
def addCategory():
    return render_template("add_category.html")

@app.route("/category/edit/:id")
def editCategory():
    return render_template("edit_category.html")

@app.route("/thread/:id")
def thread():
    return render_template("thread.html")

@app.route("/message/send")
def sendMessage():
    return render_template("index.html")

@app.route("/message/edit/:id")
def editMessage():
    return render_template("index.html")

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/signup/")
def signup:
    return render_template("signup.html")


@app.route("/demo")
def content():
    return render_template("demo.html", nimi=nimi, lista=lista, esineet=esineet)

if __name__ == "__main__":
    app.run(debug=True)
