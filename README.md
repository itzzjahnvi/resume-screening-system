Resume Screening System

A Resume Screening System that evaluates candidate resumes against a job description using TF-IDF vectorization and cosine similarity.

This project is designed using a layered architecture with clear separation of concerns, making it suitable for internal HR tools, automation workflows, and further API/web integration.

# Features

- Supports multiple resume formats:
   PDF
   DOCX
   TXT
- Automatic text cleaning and normalization
- TF-IDF based similarity scoring
- Skill extraction
- Config-driven setup
- Error handling 
- Easily extendable to REST API or Web App

# Project Structure

RESUME-SCREENING-SYSTEM/
│
├── app/
│ ├── resume_reader.py
│ ├── similarity.py
│ ├── skill_extractor.py
│ └── engine.py
│
├── config/
│ └── config.yaml
│
├── resources/
│ ├── job_desc.txt
│ └── resumes/
│
├── tests/
│ └── test_engine.py
│
├── main.py # Entry point
├── requirements.txt
└── README.md

* Installation

1. Clone the repository:

git clone https://github.com/itzzjahnvi/resume-screening-system.git
cd resume-screening-system
Create virtual environment:

python -m venv venv
venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
# Configuration
Edit the file:
config/config.yaml

Example:
resume_directory: resources/resumes
job_description: resources/job_desc.txt
shortlist_threshold: 60
No changes in core code.

* For  Running from the project root directory:

python main.py
The system will:
Read all resumes from the configured directory
Compare them against the job description
Calculate similarity score
Extract relevant skills
Print shortlisted candidates

* Running Tests
From project root:

python -m tests.test_engine
How It Works
Resume Reader
Extracts text from PDF, DOCX, and TXT files
Cleans and normalizes content
Similarity Engine
Converts resume and job description to TF-IDF vectors
Skill Extractor
Detects predefined technical skills
Engine Layer
Ensures error isolation per resume

# Error Handling
Corrupted PDFs do not stop execution
Unsupported file formats are skipped
Empty resumes return zero similarity
System continues processing remaining files

# Dependencies
scikit-learn
pdfplumber
python-docx
pyyaml

# Future Improvements
REST API (FastAPI)
CSV/Excel export

