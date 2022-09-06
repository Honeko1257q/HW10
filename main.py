from flask import Flask

from utils import get_all, format_candidates, get_candidate_id, get_candidate_skill

app = Flask(__name__)


@app.route('/')
def main():
    candidates: list[dict] = get_all()
    result: str = format_candidates(candidates)
    return result


@app.route('/candidate/int:uid')
def page_candidate(uid):
    candidate: dict = get_candidate_id(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result


@app.route('/skills/<skill>')
def page_skils(skill):
    skill_lower = skill.lower()
    candidates: list[dict] = get_candidate_skill(skill_lower)
    result = format_candidates(candidates)
    return result


app.run()
