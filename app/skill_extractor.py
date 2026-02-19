def extract_skills(text):
    skills = [
        "python", "java", "c++", "machine learning",
        "data science", "sql", "git", "docker"
    ]

    found = []
    for skill in skills:
        if skill in text:
            found.append(skill)

    return found
