from flask import Flask, render_template
from utils.flashcard import get_cards_by_category, get_categories

app = Flask(__name__)

# 首页
@app.route("/")
def home():
    return render_template("index.html")

# 登录页
@app.route("/login")
def login():
    return render_template("login.html")

# 注册页
@app.route("/register")
def register():
    return render_template("register.html")

# 刷题页
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

# 背诵卡片页
@app.route("/flashcard")
@app.route("/flashcard/<category>")
def flashcard(category=None):
    cards = get_cards_by_category(category)
    categories = get_categories()
    return render_template("flashcard.html", cards=cards, categories=categories)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)