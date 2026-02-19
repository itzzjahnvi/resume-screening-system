import os
from app.resume_reader import extract_text
from app.similarity import calc_similar
from app.skill_extractor import extract_skills

def run_engine(resume_dir, job_desc_path):
    with open(job_desc_path, "r", encoding="utf-8") as f:
        jd_text = f.read().lower()

    results = []

    for file in os.listdir(resume_dir):
        path = os.path.join(resume_dir, file)

        resume_text = extract_text(path)
        if not resume_text:
            continue

        score = calc_similar(resume_text, jd_text)
        skills = extract_skills(resume_text)

        results.append({
            "file": file,
            "score": round(score * 100, 2),
            "skills": skills
        })

    return results