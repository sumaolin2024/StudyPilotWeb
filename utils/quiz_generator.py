import random


def generate_quiz(subject: str) -> list[dict]:
    subject = subject.strip() or "通用学习"
    subject = subject[:20]
    questions = []

    questions.append(
        {
            "type": "choice",
            "prompt": f"以下哪一项最有助于提高{subject}学习效率？",
            "options": [
                "制定学习计划",
                "随机浏览资料",
                "长期拖延",
                "避免复习",
            ],
            "answer": "制定学习计划",
        }
    )

    questions.append(
        {
            "type": "judge",
            "prompt": f"每天复习学习内容可以帮助巩固{subject}知识。",
            "answer": "正确",
        }
    )

    questions.append(
        {
            "type": "blank",
            "prompt": f"复习时使用{subject}笔记和概念图可以帮助_____记忆。",
            "answer": "长期",
        }
    )

    random.shuffle(questions)
    return questions


def score_quiz(questions: list[dict], answers: dict) -> tuple[int, int, list[dict]]:
    total = len(questions)
    score = 0
    results = []

    for idx, question in enumerate(questions, start=1):
        key = str(idx)
        user_answer = answers.get(key, "").strip()
        correct = question["answer"].strip()
        passed = user_answer == correct
        if passed:
            score += 1
        results.append(
            {
                "index": idx,
                "prompt": question["prompt"],
                "user_answer": user_answer or "未作答",
                "correct_answer": correct,
                "passed": passed,
            }
        )

    return score, total, results
