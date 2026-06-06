import json

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from utils.auth import login_required
from utils.db import get_db
from utils.quiz_generator import generate_quiz, score_quiz

quiz_bp = Blueprint("quiz", __name__, template_folder="../templates")


@quiz_bp.route("/", methods=["GET", "POST"])
@login_required
def quiz():
    db = get_db()
    if request.method == "POST":
        mode = request.form.get("mode")
        if mode == "generate":
            subject = request.form.get("subject", "通用学习")
            questions = generate_quiz(subject)
            return render_template(
                "quiz.html",
                subject=subject,
                questions=questions,
                generated=True,
                serialized=questions,
            )

        if mode == "submit":
            raw_questions = request.form.get("questions")
            if not raw_questions:
                flash("无题目数据，请重新生成。", "danger")
                return redirect(url_for("quiz.quiz"))

            questions = json.loads(raw_questions)
            answers = {
                key.replace("answer_", ""): request.form.get(key, "").strip()
                for key in request.form
                if key.startswith("answer_")
            }
            score, total, results = score_quiz(questions, answers)
            db.execute(
                "INSERT INTO quiz_history (user_id, subject, score, total) VALUES (?, ?, ?, ?)",
                (session.get("user_id"), request.form.get("subject", "通用学习"), score, total),
            )
            db.commit()
            return render_template(
                "quiz.html",
                results=results,
                score=score,
                total=total,
                subject=request.form.get("subject", "通用学习"),
            )

    return render_template("quiz.html")
