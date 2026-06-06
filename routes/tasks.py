from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from utils.auth import login_required
from utils.db import get_db

tasks_bp = Blueprint("tasks", __name__, template_folder="../templates")


@tasks_bp.route("/", methods=["GET", "POST"])
@login_required
def task_list():
    db = get_db()
    if request.method == "POST":
        title = request.form["title"].strip()
        if title:
            db.execute(
                "INSERT INTO tasks (user_id, title) VALUES (?, ?)",
                (session.get("user_id"), title),
            )
            db.commit()
            flash("任务已添加。", "success")
        else:
            flash("任务内容不能为空。", "danger")

    tasks = db.execute(
        "SELECT id, title, completed FROM tasks WHERE user_id = ? ORDER BY created_at DESC",
        (session.get("user_id"),),
    ).fetchall()

    return render_template("tasks.html", tasks=tasks)


@tasks_bp.route("/complete/<int:task_id>")
@login_required
def complete_task(task_id):
    db = get_db()
    task = db.execute(
        "SELECT completed FROM tasks WHERE id = ? AND user_id = ?",
        (task_id, session.get("user_id")),
    ).fetchone()
    if task is not None:
        db.execute(
            "UPDATE tasks SET completed = ? WHERE id = ?",
            (0 if task["completed"] else 1, task_id),
        )
        db.commit()
        flash("任务状态已更新。", "success")
    else:
        flash("未找到该任务。", "danger")
    return redirect(url_for("tasks.task_list"))


@tasks_bp.route("/delete/<int:task_id>")
@login_required
def delete_task(task_id):
    db = get_db()
    db.execute(
        "DELETE FROM tasks WHERE id = ? AND user_id = ?",
        (task_id, session.get("user_id")),
    )
    db.commit()
    flash("任务已删除。", "info")
    return redirect(url_for("tasks.task_list"))
