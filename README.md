# Smart CV Analyzer – AI + ATS Powered Resume Optimizer

**Smart CV Analyzer** is a cutting-edge tool designed for job seekers who want their CVs to stand out. Combining **NLP, machine learning, and AI-driven rewrite suggestions**, this tool analyzes a CV against a target job description, calculates an ATS-style match score, highlights missing skills, and provides actionable feedback to improve your chances of landing interviews. It’s a **portfolio-ready project that demonstrates real-world AI and web development skills**.

## 🚀 Key Features

- **ATS Keyword Match Score:** Compares CV content with job descriptions to compute a relevance score (%) — just like real applicant tracking systems used by recruiters.  
- **Missing Skills Detection:** Automatically identifies skills present in the job description but absent in the CV, helping users tailor their resumes effectively.  
- **AI-Powered CV Rewrite:** Uses HuggingFace’s **tiny-t5** model to professionally rewrite CV sentences, improving clarity, impact, and readability.  
- **PDF Upload & Parsing:** Extracts text seamlessly from PDF resumes using **PyMuPDF**, ensuring compatibility with real-world CV formats.  
- **Clean, Interactive UI:** Displays match scores, missing skills, and AI rewrite suggestions in a user-friendly dashboard for quick insights.  

## 💻 Technology Stack

- **Python 3.x** – core programming  
- **Flask** – lightweight web server and backend  
- **PyMuPDF (fitz)** – PDF parsing and text extraction  
- **Transformers (HuggingFace tiny-t5)** – AI-powered CV rewrite  
- **scikit-learn / NLP** – keyword extraction and similarity scoring  

## 🧠 How It Works

1. **CV Upload:** Users upload their resume in PDF format.  
2. **Text Extraction:** PyMuPDF parses the PDF to extract raw text.  
3. **Keyword Matching:** The system analyzes the CV against a job description, calculates a match score, and lists missing skills.  
4. **AI Rewrite:** Sentences in the CV are professionally rewritten using the tiny-t5 model for maximum clarity and impact.  
5. **Results Display:** Users see a **visual match score**, missing keywords, and AI-enhanced CV suggestions all in one dashboard.  

## ⚡ Usage

1. Clone the repository.  
2. Install dependencies:  
```bash
pip install flask pymupdf transformers torch

Run the Flask app:

python app.py


4.	Open your browser at http://127.0.0.1:5000/.
	5.	Upload your CV and target job description to see instant analysis and AI rewrite suggestions.

🌟 Why This Project Stands Out
	•	Demonstrates real NLP & AI integration in a functional application.
	•	Mirrors industry-standard ATS systems, showing practical knowledge of hiring technologies.
	•	Provides hands-on experience with PDF parsing, Python web development, and HuggingFace models.
	•	Lightweight, fast, and fully functional for portfolio demonstrations.

🔮 Potential Enhancements
	•	Download AI-enhanced CV as PDF.
	•	Track historical CV uploads and improvements.
	•	Visual dashboards for match scores and skill gaps.

⸻

## AUTHOR: ARNOLD NDLOVU

This project is a perfect showcase of combining AI, NLP, and web development to solve a real-world problem for job seekers.