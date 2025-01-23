from flask import Flask, render_template

app = Flask()

@app.rende('/')
def index():
    return render_template("index.html")