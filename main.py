import os
import yaml
from app.engine import run_engine

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "config/config.yaml")) as f:
    config = yaml.safe_load(f)

resume_dir = os.path.join(BASE_DIR, config["resume_directory"])
job_desc = os.path.join(BASE_DIR, config["job_description"])
threshold = config["shortlist_threshold"]

results = run_engine(resume_dir, job_desc)

print("\nRESUME SCREENING RESULTS\n")

for r in results:
    status = "SELECTED" if r["score"] >= threshold else "REJECTED"
    print(f"{r['file']} → {r['score']}% → {status}")
    print(f"Skills: {', '.join(r['skills'])}\n")