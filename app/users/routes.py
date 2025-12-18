from flask import Blueprint, render_template, request, redirect, url_for
from app.models import User
from app.users.service import (
    get_all_users, create_user, update_user, delete_user
)

bp = Blueprint("users", __name__)

@bp.route("/")
def index():
    users = get_all_users()
    return render_template("index.html", users=users)

@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        create_user(request.form["name"], request.form["email"])
        return redirect(url_for("users.index"))
    return render_template("create.html")

@bp.route("/edit/<int:user_id>", methods=["GET", "POST"])
def edit(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == "POST":
        update_user(user, request.form["name"], request.form["email"])
        return redirect(url_for("users.index"))
    return render_template("edit.html", user=user)

@bp.route("/delete/<int:user_id>")
def delete(user_id):
    user = User.query.get_or_404(user_id)
    delete_user(user)
    return redirect(url_for("users.index"))
