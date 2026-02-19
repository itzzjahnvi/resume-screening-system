Resume Screening System

A Python-based Resume Screening System that automates resume parsing, skill extraction, and candidate ranking.
This system calculates a match score for each candidate against a job description and identifies skill gaps, helping recruiters and hiring managers save time and make data-driven decisions.

Table of Contents

Features
Project Structure
Installation
Usage
Future Enhancements
Notes

*Features

Automatically parses multiple resumes from a folder
Extracts skills from resumes
Compares resumes to job descriptions using TF-IDF similarity
Shows skills found and missing skills (skill gap)
Ranks resumes based on match score
Supports TXT resumes (PDF/DOCX optional)

*Project Structure

RESUME-SCREENING-SYSTEM/
├── data/
│   ├── job_description.txt          # Job description file
│   └── resumes/
│       ├── sample_resume.txt        # Example resumes
│       └── candidate1.txt
├── src/
│   ├── main.py                      # Main script
│   ├── matcher.py                   # TF-IDF similarity functions
│   ├── resume_parser.py             # Extracts text from resumes
│   ├── skill_extractor.py           # Extracts skills from text
│   └── test_run.py                  # Script to run resume screening
├── .gitignore
├── requirements.txt
└── README.md

*Installation

Clone the repository:

git clone <YOUR_GITHUB_REPO_URL>
cd RESUME-SCREENING-SYSTEM


Install dependencies:

pip install -r requirements.txt

Requirements (requirements.txt):

pdfplumber
python-docx
scikit-learn
nltk


Note: Currently, TXT resumes are fully supported. PDF/DOCX support works with valid files.

*Usage

Place your job description in data/job_description.txt.
Add resumes in data/resumes/ (TXT format recommended).
Run the test script:
python src/test_run.py

*The script outputs:

Resume name
Match score (%)
Skills found
Missing skills (skill gap)

*Future Enhancements

Add full PDF/DOCX support
GUI interface for non-technical users
Save results to CSV or Excel for reporting
Enhance skill extraction with NLP and synonyms
Add weighting for critical vs optional skills

Notes

Ensure that skills in resumes match the SKILLS list in skill_extractor.py.

Multi-word skills like "machine learning" must be written with a space.