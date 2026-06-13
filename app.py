from flask import Flask, render_template
from utils.flashcard import get_cards_by_category, get_categories

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/flashcard")
@app.route("/flashcard/<category>")
def flashcard(category=None):
    cards = get_cards_by_category(category)
    categories = get_categories()
    return render_template("flashcard.html", cards=cards, categories=categories)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)