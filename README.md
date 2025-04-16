# Automated CV Scoring and Feedback AI Agent

## Objective

The goal of this project is to design and implement an **AI Agent** that automates the process of scoring and providing feedback for resumes (CVs). The agent will:

1. Collect resumes from a designated folder or email inbox.
2. Process and score each resume based on its content (work experience, education, skills, etc.).
3. Send personalized emails to candidates with their score and feedback.

## Scope of Work

### Step 1: Resume Collection
- Monitor or manually collect resumes (PDF/DOCX format) from an email inbox.
- Ensure that resumes are uniquely named and organized for tracking purposes.

**Expected Output:**
- Masked name and email.
- Job Description (JD) - CV match score.
- Batch years.
- Relevant AI experience.
- Resume scoring.

### Step 2: Resume Scoring
- Develop or integrate an algorithm to evaluate resumes based on the following:
  - Work experience
  - Education
  - Skills
  - Relevant keywords
  - Formatting and clarity

- Assign a CV Score based on predefined criteria and weights.
- Optionally, include additional tags or metrics such as:
  - Years of experience
  - Technical fit score
  - Soft skills

### Step 3: Email Feedback to Candidates
- Extract the contact information (preferably email address) from the CV or external source.
- Compose a personalized email template that includes:
  - CV Score
  - Breakdown of score components
  - Notable feedback (strengths and weaknesses)
  - Optional: Next steps or encouragement message

- Automatically send the email to each candidate using a secure mail server or email API (e.g., Gmail API or SMTP server).

## Deliverables
- **Script or pipeline**: A script that processes resumes from an email server.
- **Scoring model**: A resume evaluation algorithm with documented scoring logic.
- **Email automation script**: A script that automates feedback email sending.
- **Log system**: A log system to track which resumes have been processed and emailed.
- **Code repository**: Code will be pushed to **Elint’s GitLab** public repository.

## Dependencies & Tools

### Programming Language:
- Python (Preferred)

### Important Libraries:
- `os`
- `pandas`
- `sklearn`
- `docx`
- `PyPDF2`
- `smtplib`

### Email Servers:
- Gmail API / SMTP server (or any other preferred mail server)

### Optional Tools:
- Frontend dashboard for manual review.

## Annexure
- **Bonus Points**: Using agentic frameworks like **CrewAI** or similar solutions.
- **Key Considerations**: Solutions should be simple, efficient, and optimized.
- **Open Source Contribution**: All solutions will be submitted to our **GitLab** public repository and made available to the Open Source community.

---

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/Hero-Reborn/Automated-CV-Scoring-and-Feedback-AI-Agent.git
