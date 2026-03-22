import re

# Example common skills
COMMON_SKILLS = [
    "python", "flask", "django", "sql", "javascript",
    "aws", "docker", "git", "rest api", "machine learning"
]

def extract_skills(cv_text):
    """
    Extracts skills present in the CV text from a predefined list.
    """
    cv_text_lower = cv_text.lower()
    return [skill for skill in COMMON_SKILLS if skill in cv_text_lower]

def extract_experience(cv_text):
    """
    Extracts years of experience from CV text.
    """
    matches = re.findall(r'(\d+)\+?\s+years', cv_text.lower())
    years = [int(m) for m in matches]
    return max(years) if years else 0

def semantic_similarity(cv_text, job_desc):
    """
    Simple keyword-based match percentage instead of embedding similarity.
    """
    cv_words = set(cv_text.lower().split())
    job_words = set(job_desc.lower().split())
    if not job_words:
        return 0
    match_count = len(cv_words & job_words)
    return round((match_count / len(job_words)) * 100, 2)

def missing_skills(cv_skills, job_skills):
    """
    Returns list of job skills missing from the CV.
    """
    return [skill for skill in job_skills if skill.lower() not in cv_skills]

def generate_feedback(cv_text, job_desc, cv_skills, missing):
    """
    Generates feedback based on missing skills and short sentences.
    """
    feedback = []

    if missing:
        feedback.append(f"Consider adding skills: {', '.join(missing[:5])}")

    sentences = re.split(r'\.|\n', cv_text)
    for s in sentences[:5]:
        s = s.strip()
        if s:
            if len(s.split()) < 5:
                feedback.append(f"Sentence too short: '{s}' → add more detail.")
            if any(skill.lower() in s.lower() for skill in missing):
                feedback.append(f"Skill mentioned incorrectly: '{s}' → rewrite clearly.")

    return feedback