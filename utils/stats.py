import os
from datetime import datetime

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def build_user_report(db, user_id: int) -> dict:
    completed_tasks = db.execute(
        "SELECT COUNT(*) AS count FROM tasks WHERE user_id = ? AND completed = 1", (user_id,)
    ).fetchone()["count"]
    pending_tasks = db.execute(
        "SELECT COUNT(*) AS count FROM tasks WHERE user_id = ? AND completed = 0", (user_id,)
    ).fetchone()["count"]

    rows = db.execute(
        "SELECT score, total, created_at FROM quiz_history WHERE user_id = ? ORDER BY created_at DESC LIMIT 7",
        (user_id,),
    ).fetchall()

    recent_scores = [row["score"] for row in rows][::-1]
    timestamps = [row["created_at"] for row in rows][::-1]
    average_score = int(sum(recent_scores) / len(recent_scores)) if recent_scores else 0

    plot_name = f"stats_{user_id}.png"
    output_path = os.path.join(os.path.dirname(__file__), "..", "static", "plots", plot_name)
    output_path = os.path.abspath(output_path)
    _create_plot(completed_tasks, pending_tasks, recent_scores, timestamps, output_path)

    return {
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "average_score": average_score,
        "recent_scores": recent_scores,
        "plot_name": plot_name,
    }


def _create_plot(completed, pending, scores, labels, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.figure(figsize=(9, 5))

    plt.subplot(1, 2, 1)
    plt.bar(["已完成", "未完成"], [completed, pending], color=["#28a745", "#ffc107"])
    plt.title("任务完成情况")
    plt.ylabel("数量")

    plt.subplot(1, 2, 2)
    if scores:
        plt.plot(labels, scores, marker="o", color="#007bff")
        plt.title("最近刷题成绩")
        plt.ylim(0, 100)
    else:
        plt.text(0.5, 0.5, "暂无刷题记录", ha="center", va="center")
        plt.title("最近刷题成绩")
        plt.xticks([])
        plt.yticks([])

    plt.tight_layout()
    plt.savefig(output_path, dpi=120)
    plt.close()
