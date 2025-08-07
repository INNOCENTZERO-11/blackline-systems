import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db, login_manager
from .models import User, Tool

main = Blueprint("main", __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main.route("/")
def home():
    return render_template("home.html")

@main.route("/dashboard")
def dashboard():
    tools = Tool.query.all()
    return render_template("dashboard.html", tools=tools)

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("main.admin"))
        flash("Invalid credentials")
    return render_template("login.html")

@main.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    if not current_user.is_admin:
        return redirect(url_for("main.dashboard"))
    
    if request.method == "POST":
        file = request.files["file"]
        filename = file.filename
        filepath = os.path.join("app/uploads", filename)
        file.save(filepath)
        
        tool = Tool(
            name=request.form["name"],
            description=request.form["description"],
            filename=filename
        )
        db.session.add(tool)
        db.session.commit()
        flash("Tool uploaded!")
    
    return render_template("admin.html")

@main.route("/download/<filename>")
def download(filename):
    return send_from_directory("uploads", filename)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))
