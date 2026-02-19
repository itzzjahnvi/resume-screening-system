from app.engine import run_engine

results = run_engine("resources/resumes", "resources/job_desc.txt")

assert isinstance(results, list)
print("Engine working correctly ✅")