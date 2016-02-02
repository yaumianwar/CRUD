import datetime
from flask import Flask, render_template, redirect, session, request
from db import database
from models import Polls

app = Flask(__name__)
app.config.from_object('config')
database.init_app(app)

@app.route("/")
def home():
    return render_template("index.html", **locals())

# show all polls
@app.route("/polls")
def allpolls():
    # Polls.query.all() == select*from polls(tablename)
    polls = Polls.query.all()
    return render_template("polls.html",  **locals())

# show one poll by id
@app.route("/polls/<int:id>")
def poll(id):
    # Post.query.get(id) == select*from polls(tablename) where id = ''
    polls = Polls.query.get(id)
    if not polls:
        abort(404)
    return render_template("poll.html",  **locals())

# create poll
@app.route("/pollsadd", methods=["POST", "GET"])
def addpoll():
    if request.method == "POST":
        name = request.form.get("name", None)
        candidate = request.form.get("candidate", None)
        # create new record in database
        polls = Polls(name,candidate)
        polls.createdtime = datetime.datetime.now()
        database.session.add(polls)
        database.session.commit()
        return redirect("/polls")

    return render_template("pollsadd.html", **locals())

# update data by id
@app.route("/pollsupdate/<int:id>", methods=["POST", "GET"])
def updatepoll(id):
    if request.method == "POST":
        newcandidate = request.form.get("candidate",None)
        polls = Polls.query.get(id)
        polls.candidate = newcandidate
        database.session.add(polls)
        database.session.commit()
        return render_template("poll.html", **locals())
    polls = Polls.query.get(id)

    return render_template("pollsupdate.html", **locals())


# delete data by id
@app.route("/pollsdelete/<int:id>")
def deletepoll(id):
    polls = Polls.query.get(id)
    database.session.delete(polls)
    database.session.commit()

    return render_template("index.html", **locals())

if __name__=="__main__":
	app.run(debug=True)
