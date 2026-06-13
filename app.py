from flask import Flask, render_template, request, redirect, url_for, flash
from utils.flashcard import get_cards_by_category, get_categories
from utils.quiz_generator import QuizGenerator

app = Flask(__name__)
app.secret_key = "studypilot_secret_key"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        course = request.form.get("course", "").strip()
        if course:
            qg = QuizGenerator()
            try:
                qg.generate_quiz(course)
                flash(f"已生成 {course} 的刷题！", "success")
            except Exception as e:
                flash(f"生成失败: {e}", "danger")
            return redirect(url_for("quiz"))
    return render_template("quiz.html")

@app.route("/flashcard")
@app.route("/flashcard/<category>")
def flashcard(category=None):
    cards = get_cards_by_category(category)
    categories = get_categories()
    return render_template("flashcard.html", cards=cards, categories=categories)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)