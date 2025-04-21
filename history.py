import json
from datetime import datetime
from uuid import uuid4

HISTORY_FILE = "summary_history.json"

def save_summary(content: str, summary: str, mode: str):
    data = {
        "id": str(uuid4())[:6],
        "timestamp": datetime.utcnow().isoformat(),
        "mode": mode,
        "summary": summary,
        "original_excerpt": content[:200]
    }

    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

    history.append(data)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def get_summary_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
