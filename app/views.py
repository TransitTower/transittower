from flask import render_template

from . import app


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/rooms")
def rooms():
    return render_template('rooms.html')


@app.route("/activities")
def activities():
    return render_template('activities.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/location")
def location():
    return render_template('location.html')


@app.route("/book")
def book():
    return render_template('book.html')


@app.route("/gallery")
def gallery():
    return render_template('gallery.html')


@app.route("/privacy")
def privacy():
    return render_template('privacy.html')


@app.route("/terms")
def terms():
    return render_template('terms.html')


@app.route("/faq")
def faq():
    return render_template('faq.html')
