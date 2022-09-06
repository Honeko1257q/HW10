import json


def load_candidates() -> list[dict]:
    with open("candidates.json", "r", encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


def format_candidates(candidates: list[dict]) -> str:
    result = '<pre>'
    for candidate in candidates:
        result += f"{candidate['name']}\n {candidate['position']}\n {candidate['skills']}\n"
        result += '/<pre>'
        return result


def get_all() -> list[dict]:
    return load_candidates()


def get_candidate_id(uid: int) -> dict | None:
    candidates = get_all()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate
        return None


def get_candidate_skill(skill: str) -> list[dict]:
    candidates = get_all()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result
