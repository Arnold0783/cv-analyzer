from flask import Flask, render_template, request
from utils import extract_text_from_pdf
from model import extract_skills, extract_experience, semantic_similarity, missing_skills, generate_feedback
from rewrite_hf import rewrite_cv_hf
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    missing = []
    feedback = []
    cv_skills = []
    experience = 0
    highlighted_cv = None
    rewritten_cv = None

    if request.method == "POST":
        file = request.files.get("cv")
        job_desc = request.form.get("job", "")

        if file:
            # Extract CV text
            cv_text = extract_text_from_pdf(file)

            # Skills & experience
            cv_skills = extract_skills(cv_text)
            experience = extract_experience(cv_text)

            # Semantic match (keyword-based)
            score = semantic_similarity(cv_text, job_desc)

            # Job skills (split by commas)
            job_skills = [s.strip().lower() for s in job_desc.split(",") if s.strip()]
            missing = missing_skills(cv_skills, job_skills)

            # Feedback
            feedback = generate_feedback(cv_text, job_desc, cv_skills, missing)

            # Highlight missing skills in CV
            highlighted_cv = cv_text
            for skill in missing:
                highlighted_cv = highlighted_cv.replace(
                    skill,
                    f"<span class='bg-yellow-200 font-bold'>{skill}</span>"
                )

            # HuggingFace API rewrite
            rewritten_cv = rewrite_cv_hf(cv_text)

    return render_template(
        "index.html",
        score=score,
        missing=missing,
        feedback=feedback,
        cv_skills=cv_skills,
        experience=experience,
        highlighted_cv=highlighted_cv,
        rewritten_cv=rewritten_cv
    )

# ✅ Render compatibility: dynamic port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render provides PORT env variable
    app.run(host="0.0.0.0", port=port)