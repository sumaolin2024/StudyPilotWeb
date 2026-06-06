from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from utils.db import get_db

auth_bp = Blueprint("auth", __name__, template_folder="../templates")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()
        db = get_db()
        error = None

        if not username or not password:
            error = "用户名和密码不能为空。"
        elif db.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone() is not None:
            error = "用户名已存在，请换一个。"

        if error is None:
            db.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, generate_password_hash(password)),
            )
            db.commit()
            flash("注册成功，请登录。", "success")
            return redirect(url_for("auth.login"))

        flash(error, "danger")

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()
        db = get_db()
        error = None
        user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

        if user is None:
            error = "用户名不存在。"
        elif not check_password_hash(user["password_hash"], password):
            error = "密码错误。"

        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            flash("登录成功。", "success")
            return redirect(url_for("index"))

        flash(error, "danger")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("您已退出登录。", "info")
    return redirect(url_for("index"))
