import re
from sentence_transformers import SentenceTransformer, util

# Load small embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Example skills
COMMON_SKILLS = [
    "python", "flask", "django", "sql", "javascript",
    "aws", "docker", "git", "rest api", "machine learning"
]

def extract_skills(cv_text):
    cv_text_lower = cv_text.lower()
    return [skill for skill in COMMON_SKILLS if skill in cv_text_lower]

def extract_experience(cv_text):
    matches = re.findall(r'(\d+)\+?\s+years', cv_text.lower())
    years = [int(m) for m in matches]
    return max(years) if years else 0

def semantic_similarity(cv_text, job_desc):
    embeddings = model.encode([cv_text, job_desc], convert_to_tensor=True)
    similarity = util.cos_sim(embeddings[0], embeddings[1])
    return float(similarity) * 100

def missing_skills(cv_skills, job_skills):
    return [skill for skill in job_skills if skill.lower() not in cv_skills]

def generate_feedback(cv_text, job_desc, cv_skills, missing):
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