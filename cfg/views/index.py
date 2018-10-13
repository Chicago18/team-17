

from collections import OrderedDict, defaultdict
import os
import uuid
import shutil
import hashlib
import tempfile
import arrow
import flask
from flask import send_from_directory, abort
import cfg




def create_account(form):
    """Create account."""
    # Save uploaded file

    # User information
    fullname = form['fullname']
    username = form['username']
    location = form['location']
    email = form['email']
    company = form['company']
    affiliation = form['affiliation']
    password = form['password']


    # User tried to create a password with empty string
    if password == "":
        abort(400)

    database = cfg.model.get_db()
    cur = database.cursor()

    # User tried to create account with existing username
    cur.execute("SELECT * FROM users")
    for row in cur:
        if username == row['username']:
            abort(409)

    # Search query
    insert = """
            INSERT INTO users
                (username, fullname, location, email, company, affiliation, password)
            VALUES
                (?, ?, ?, ?, ?, ?, ?)
            """
    values = (username, fullname, location, email, company, affiliation,
              password)
    # Inserts new user into database
    cur.execute(insert, values)

    # Saves changes
    database.commit()
    flask.session['username'] = username




@cfg.app.route('/', methods=['GET', 'POST'])
def show_index():
    """Root page."""
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('show_login'))

    context = {'logname': flask.session['username']}


    return flask.render_template("login.html", **context)



@cfg.app.route('/login/', methods=['GET', 'POST'])
def show_login():
    """Login page."""
    context = {'logname': ""}
    if flask.request.method == 'POST':
        database = cfg.model.get_db()
        cur = database.cursor()
        username = flask.request.form['username']
        password = flask.request.form['password']
        cur.execute("SELECT * FROM users")
        for row in cur:
            if username == row['username'] and password == row['password']:
                print("found")
                flask.session['username'] = username
                context['logname'] = username
                return flask.redirect(flask.url_for('resource'))

        # User not found
        abort(403)

    return flask.render_template("login.html", **context)


@cfg.app.route('/accounts/logout/', methods=['GET', 'POST'])
def show_logout():
    """Logout page."""
    flask.session.clear()
    return flask.redirect(flask.url_for('show_login'))


@cfg.app.route('/signup/', methods=['GET', 'POST'])
def show_create():
    """Create account page."""
    if flask.request.method == 'POST':
        print("yes")
        create_account(flask.request.form)

        return flask.redirect(flask.url_for('show_index'))

    return flask.render_template("/signup.html")


 # Profile page
@cfg.app.route('/profile/<path:user>/', methods=['GET', 'POST'])
def profile(user):
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('show_login'))
    context = {'logname': flask.session['username'], 'email': "", 'fullname': "",
                'location': "", 'company': "", 'affiliation': "", 'username': user, 'name': ""}
    database = cfg.model.get_db()
    cur = database.cursor()
    print(context['logname'], user)
    if context['logname'] == user:
        cur.execute("SELECT * FROM users")
        for row in cur:
            if user == row['username']:
                context['email'] = row['email']
                context['fullname'] = row['fullname']
                context['location'] = row['location']
                context['company'] = row['company']
                context['affiliation'] = row['affiliation']
    else:
        cur.execute("SELECT * FROM testimony")
        for row in cur:
            if user == row['name']:
                context['email'] = row['email']
                context['name'] = row['name']
                context['location'] = row['location']
                context['company'] = row['company']
                context['affiliation'] = row['affiliation']
    return flask.render_template("/profile.html", **context)

# Discussion page
@cfg.app.route('/discussion/', methods=['GET', 'POST'])
def discussion():
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('show_login'))
    context = {'logname': flask.session['username'], 'discussion': []}

    database = cfg.model.get_db()
    cur = database.cursor()

    #if (request to sort by most recent):
    #if (request to sort by category):
    #if (request to sort by alphabetical): (ELSE)
    cur.execute("SELECT * FROM discussion ORDER BY post")
    for row in cur:
        context['discussion'].append(row)

    # Saves changes
    database.commit()
    return flask.render_template("/discussion.html", **context)

    # Resource page
@cfg.app.route('/resource/', methods=['GET', 'POST'])
def resource():
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('show_login'))
    context = {'logname': flask.session['username'], 'resources': []}

    database = cfg.model.get_db()
    cur = database.cursor()

    cur.execute("SELECT * FROM resources")
    for row in cur:
        context['resources'].append(row)

    # Saves changes
    database.commit()

    return flask.render_template("/resource.html", **context)

@cfg.app.route('/testimony/', methods=['GET', 'POST'])
def testimony():
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('show_login'))
    context = {'logname': flask.session['username'], 'testimonies': []}

    database = cfg.model.get_db()
    cur = database.cursor()

    cur.execute("SELECT * FROM testimony")
    for row in cur:
        context['testimonies'].append(row)

    # Saves changes
    database.commit()
    return flask.render_template("/testimony.html", **context)
