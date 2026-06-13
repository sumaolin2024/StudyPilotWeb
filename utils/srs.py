# -*- coding: utf-8 -*-
"""Spaced Repetition System (SM-2) - StudyPilot"""

import json
import os
from datetime import date, datetime, timedelta
from pathlib import Path

SRS_FILE = Path(__file__).parent.parent / "data" / "srs_state.json"

# Default SRS values for new cards
DEFAULT_SRS = {
    "ease": 2.5,
    "interval": 1,
    "repetitions": 0,
    "due_date": date.today().isoformat(),
    "last_reviewed": None
}


def _ensure_data_dir():
    os.makedirs(SRS_FILE.parent, exist_ok=True)


def load_srs_state() -> dict:
    """Load SRS state from JSON file. Returns {card_id_str: srs_dict}."""
    _ensure_data_dir()
    if SRS_FILE.exists():
        try:
            return json.loads(SRS_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, ValueError):
            return {}
    return {}


def save_srs_state(state: dict):
    """Save SRS state to JSON file."""
    _ensure_data_dir()
    SRS_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def get_srs_for_card(card_id: int, state: dict = None) -> dict:
    """Get SRS state for a card, with defaults if not found."""
    if state is None:
        state = load_srs_state()
    key = str(card_id)
    if key in state:
        srs = state[key].copy()
        # Ensure all fields exist
        for field, default in DEFAULT_SRS.items():
            if field not in srs:
                srs[field] = default
        return srs
    return DEFAULT_SRS.copy()


def review_card(card_id: int, rating: str) -> dict:
    """Review a card with rating: 'again', 'hard', or 'good'.
    Updates SRS state using SM-2 algorithm and returns new state."""
    state = load_srs_state()
    key = str(card_id)
    srs = get_srs_for_card(card_id, state)

    today = date.today()

    if rating == "again":
        srs["repetitions"] = 0
        srs["interval"] = 1
        srs["ease"] = max(1.3, srs["ease"] - 0.2)
    elif rating == "hard":
        srs["interval"] = max(1, int(srs["interval"] * 1.2))
        srs["ease"] = max(1.3, srs["ease"] - 0.05)
    elif rating == "good":
        reps = srs["repetitions"]
        srs["repetitions"] = reps + 1
        if reps == 0:
            srs["interval"] = 1
        elif reps == 1:
            srs["interval"] = 3
        else:
            srs["interval"] = int(round(srs["interval"] * srs["ease"]))
        srs["ease"] = round(srs["ease"] + 0.05, 2)

    srs["due_date"] = (today + timedelta(days=srs["interval"])).isoformat()
    srs["last_reviewed"] = today.isoformat()

    state[key] = srs
    save_srs_state(state)
    return srs


def get_due_cards(all_cards: list) -> list:
    """Filter cards to only those with due_date <= today."""
    state = load_srs_state()
    today = date.today()
    due = []
    for card in all_cards:
        srs = get_srs_for_card(card["id"], state)
        due_date = date.fromisoformat(srs["due_date"])
        if due_date <= today:
            card_with_srs = card.copy()
            card_with_srs.update(srs)
            due.append(card_with_srs)
    return due


def get_srs_stats(all_cards: list) -> dict:
    """Get SRS statistics for display."""
    state = load_srs_state()
    today = date.today()
    total = len(all_cards)
    new = 0
    learning = 0
    mature = 0
    due_count = 0

    for card in all_cards:
        srs = get_srs_for_card(card["id"], state)
        if srs["last_reviewed"] is None:
            new += 1
        elif srs["interval"] >= 21:
            mature += 1
        else:
            learning += 1

        due_date = date.fromisoformat(srs["due_date"])
        if due_date <= today:
            due_count += 1

    return {
        "total": total,
        "new": new,
        "learning": learning,
        "mature": mature,
        "due": due_count
    }


def reset_all_srs():
    """Reset all SRS state (for testing)."""
    _ensure_data_dir()
    SRS_FILE.write_text("{}", encoding="utf-8")

print("utils/srs.py created OK")
