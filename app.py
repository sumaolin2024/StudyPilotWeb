from flask import Flask, render_template

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

# 任务页
@app.route("/tasks")
def tasks():
    return render_template("tasks.html")

# 刷题页
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

# 统计页
@app.route("/statistics")
def statistics():
    return render_template("statistics.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)