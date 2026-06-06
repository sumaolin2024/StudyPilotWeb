import os
from datetime import datetime

from flask import Blueprint, render_template, session

from utils.auth import login_required
from utils.db import get_db
from utils.stats import build_user_report

stats_bp = Blueprint("stats", __name__, template_folder="../templates")


@stats_bp.route("/")
@login_required
def statistics():
    db = get_db()
    user_id = session.get("user_id")
    report = build_user_report(db, user_id)
    image_name = report["plot_name"]
    return render_template(
        "stats.html",
        completed_tasks=report["completed_tasks"],
        pending_tasks=report["pending_tasks"],
        average_score=report["average_score"],
        recent_scores=report["recent_scores"],
        plot_url=f"/static/plots/{image_name}",
    )
