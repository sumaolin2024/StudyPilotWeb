from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from utils.flashcard import get_cards_by_category, get_categories
from utils.quiz_generator import QuizGenerator
from utils.srs import get_due_cards, get_srs_stats, review_card, get_srs_for_card, reset_all_srs

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
                questions = qg.get_quiz_data(course)
                # Also save text output for backward compatibility
                qg.generate_quiz(course)
                flash(f"已生成 {course} 的刷题！共 {len(questions)} 题", "success")
                import json
                return render_template(
                    "quiz.html",
                    generated=True,
                    course=course,
                    questions=questions,
                    questions_json=json.dumps(questions, ensure_ascii=False)
                )
            except Exception as e:
                flash(f"生成失败: {e}", "danger")
    return render_template("quiz.html")

@app.route("/flashcard")
@app.route("/flashcard/<category>")
def flashcard(category=None):
    all_cards = get_cards_by_category(category)
    all_categories = get_categories()
    import json

    # Get due cards using SRS
    due_cards = get_due_cards(all_cards)
    stats = get_srs_stats(all_cards)

    return render_template(
        "flashcard.html",
        cards=all_cards,
        due_cards=due_cards,
        categories=all_categories,
        stats=stats,
        cards_json=json.dumps(all_cards, ensure_ascii=False),
        due_cards_json=json.dumps(due_cards, ensure_ascii=False),
        stats_json=json.dumps(stats, ensure_ascii=False)
    )


@app.route("/api/srs/review", methods=["POST"])
def srs_review():
    data = request.get_json()
    card_id = data.get("card_id")
    rating = data.get("rating")
    if card_id is None or rating not in ("again", "hard", "good"):
        return jsonify({"error": "invalid request"}), 400
    new_srs = review_card(card_id, rating)
    return jsonify(new_srs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)