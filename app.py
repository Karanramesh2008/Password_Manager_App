import cry
import database as db
from flask import Flask, render_template,request,redirect,session

app=Flask(__name__)
app.secret_key="supersecret"

@app.route("/")
def login():
    db.createdb()
    if not db.is_master_set():
        return render_template("setup.html")
    return render_template("login.html")
@app.route("/setup",methods=["POST"])

def setup():
    master=request.form["master"]
    confirm=request.form["confirm"]
    if master!=confirm:
        return render_template("setup.html",error="Password don't match")
    db.save_master_hash(cry.hash_master(master))
    session["master"]=master
    return redirect("/home")

@app.route("/login",methods=["POST"])
def login_POST():
    master=request.form["master"]
    if cry.hash_master(master)==db.get_master_hash():
        session["master"]=master
        return redirect("/home")
    else:
        return render_template("login.html",error="Wrong master password!")
@app.route("/home")
def home():
    if 'master' not in session:
        return redirect("/")
    raw_passwords=db.get_all_password()
    passwords=[]
    for p in raw_passwords:
        dec=cry.decrypt(p[3],session["master"])
        passwords.append((p[0],p[1],p[2],dec))
    return render_template("home.html",passwords=passwords)

@app.route("/delete",methods=["POST"])
def delete():
    if "master" not in session:
        return redirect("/")
    site=request.form["site"]
    db.delete_password(site)
    return redirect("/home")
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/add",methods=["GET","POST"])
def add():
    if "master" not in session:
        return redirect("/")
    if request.method=="POST":
        site=request.form["site"]
        user=request.form["username"]
        passw=request.form["password"]
        encry=cry.encrypt(passw,session["master"])
        db.add_password(site,user,encry)
        return redirect("/home")
    return render_template("add.html")


if __name__=='__main__':
    app.run(debug=True)