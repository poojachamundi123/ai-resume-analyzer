from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Sample skill database
SKILLS = ["python", "java", "c", "c++", "html", "css", "javascript", "sql", "react", "node"]

def extract_skills(text):
    text = text.lower()
    found = []
    for skill in SKILLS:
        if skill in text:
            found.append(skill)
    return found

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    resume_text = request.form["resume"]
    job_text = request.form["job"]

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    if len(job_skills) == 0:
        match = 0
    else:
        match = len(set(resume_skills) & set(job_skills)) / len(job_skills) * 100

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "match": round(match, 2)
    }

if __name__ == "__main__":
    app.run(debug=True)
