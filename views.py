"""
Author: Nino Ross
Class: SDEV 300

This is lab assignment 8 for SDEV 300. This is the views
for the Flask application.
"""
import re
import socket
from datetime import datetime
import logging
from flask import Blueprint, render_template, redirect, request, flash
from flask_login import login_required, logout_user, login_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from .models import Users, db


views = Blueprint('views', __name__)

# Regular expression for password checker.
PATTERN = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{12,}$")

logging.basicConfig(level='WARNING',
                    format="{message}",
                    style='{',
                    filename='logs.log',
                    filemode='w')
logging.captureWarnings(True)


# Redirect if already logged in.
@views.route("/")
def landing():
    """ Renders the landing/cover page as root. """
    return render_template("landing.html")


# Login and Register methods
@views.route("/login", methods=['GET', 'POST'])
def login():
    """ Renders the login webpage. """
    # Gets IP address of the user, and formats the date & time.
    ip_address = socket.gethostbyname(socket.gethostname())
    ip_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Redirects user to home page if already logged in.
    if current_user.is_authenticated:
        return redirect('/index')
    else:
        if request.method == 'POST':
            email = request.form.get("email")
            password = request.form.get("password")
            user = Users.query.filter_by(email=email).first()

            if user:
                if check_password_hash(user.password, password):
                    flash("Logged in!", category='success')
                    login_user(user, remember=True)
                    return redirect('/index')
                else:
                    # Log failed login attempts and display date.
                    logging.warning(f"Login Failure [IP:{ip_address}] "
                                    f"[DATE:{ip_date}]")

                    flash('Password is incorrect.', category='error')
            else:
                flash('Email does not exist.', category='error')

        return render_template("login.html")


@views.route("/registration", methods=['GET', 'POST'])
def registration():
    """ Renders the registration webpage. """
    # Redirects user to home page if already logged in.
    if current_user.is_authenticated:
        return redirect('/index')
    else:
        if request.method == 'POST':
            first_name = request.form.get('firstname')
            last_name = request.form.get('lastname')
            email = request.form.get('email')
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')

            if len(email) < 4:
                flash("Email must be greater than 4 characters.", category='error')
            elif len(first_name) < 2:
                flash("First name must be greater than 2 characters", category='error')
            elif len(last_name) < 2:
                flash("Last name must be greater than 2 characters", category='error')
            elif not re.match(PATTERN, password1):
                # Password > 12 chars, 1 upper, 1 lower, 1 number, 1 special char
                flash("Password must contain 12 characters, 1 upper, 1 lower, "
                      "1 number, and 1 special character.", category='error')
            elif password1 != password2:
                flash("Password is not the same.", category='error')
            else:
                pw_hash = generate_password_hash(password1)
                new_user = Users(first_name=first_name, last_name=last_name,
                                 email=email, password=pw_hash)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)

                flash("Account successfully created!", category='success')
                return redirect('/login')

        return render_template("registration.html")


# Authenticated pages
@views.route("/index/")
@login_required
def index():
    """ Renders the home page and passes in the date. """
    date = datetime.now()
    return render_template("index.html", date=date)


@views.route("/links")
@login_required
def other_links():
    """ Renders the links webpage. """
    return render_template("links.html")


@views.route("/blogs")
@login_required
def blogs():
    """ Renders the blogs webpage. """
    return render_template("blogs.html")


@views.route("/about")
@login_required
def about():
    """ Renders the about webpage. """
    return render_template("about.html")


@views.route("/logout")
@login_required
def logout():
    """ Renders the registration webpage. """
    logout_user()
    return redirect('/login')


# Allows the user to reset password, and checks for validity.
@views.route("/password-reset", methods=['GET', 'POST'])
def password_reset():
    """ This method renders the password reset template.
     And allows the user to reset their password.
     Also checks for NIST SP 800-63B compliance. """

    with open('CommonPassword.txt', 'r', encoding='UTF-8') as file:
        password_list = file.read().splitlines()

        if request.method == 'POST':
            email = request.form.get("email")
            password1 = request.form.get("password1")
            password2 = request.form.get("password2")
            user = Users.query.filter_by(email=email).first()

            if user:
                if not re.match(PATTERN, password1):
                    # Password > 12 chars, 1 upper, 1 lower, 1 number, 1 special char
                    flash("Password must contain 12 characters, 1 upper, 1 lower, "
                          "1 number, and 1 special character.", category='error')
                elif re.compile('|'.join(password_list), re.IGNORECASE).search(password1):
                    flash("Password is too common. Please enter a "
                          "different password.", category='error')
                elif password1 != password2:
                    flash("Passwords are not the same. Please Try again.", category='error')
                else:
                    pw_hash = generate_password_hash(password1)
                    user.password = pw_hash
                    db.session.commit()
                    flash("Password successfully changed. Please login!", category='success')

                    if current_user.is_authenticated:
                        logout_user()

                    return redirect('/login')
            else:
                flash("Sorry that email does not exist. Please try again.", category='error')

    return render_template("password-reset.html")
