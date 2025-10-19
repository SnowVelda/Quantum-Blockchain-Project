# Simple Gemini memory store (JSON-backed)
import json
from pathlib import Path

MEM_FILE = Path(__file__).parent / "memory_log.json"

def load():
    if MEM_FILE.exists():
        return json.loads(MEM_FILE.read_text(encoding="utf-8"))
    return {"people": {}, "events": []}

def save(data):
    MEM_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")

def add_person(name, info):
    data = load()
    data["people"][name] = info
    save(data)

def add_event(event):
    data = load()
    data["events"].append(event)
    save(data)

if __name__ == "__main__":
    d = load()
    print("Memory keys:", list(d.keys()))
