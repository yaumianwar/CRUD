import datetime
from flask import render_template, redirect, session
from db import database
from models import Polls

app = Flask(__name__)
app.config.from_object('config')
database.init_app(app)


# show all polls
@app.route("/polls")
def allpolls():
    # Polls.query.all() == select*from polls(tablename)
    polls = Polls.query.all()
    return render_template("polls.html",  **locals())

# show one poll by id
@app.route("/polls/:id")
def poll(id):
    # Post.query.get(id) == select*from polls(tablename) where id = ''
    poll = Polls.query.get(id)
    if not poll:
        abort(404)
    return render_template("user_poll.html",  **locals())

# create poll
@app.route("/polls/add", methods=["POST", "GET"])
def addpoll():
    if request.method == "POST":
        name = request.form.get("name", None)
        candidate = request.form.get("candidate", None)
        # create new record in database
        polls = Polls(name,candidate)
        polls.createdtime = datetime.datetime.now()
        database.session.add(polls)
        database.session.commit()
        return redirect("somewhere")

    return render_template("index.html", **locals())
