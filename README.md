# Profile_matching_gemini
Matching resume and job description

 **# Resume Evaluation API**

**## Description**

This API leverages Google's Gemini model to evaluate resumes for key technical roles. It assesses resume-job description (JD) matching scores, identifies missing keywords, and provides a concise profile summary.

**## Endpoints**

* **POST /evaluate_resume**
    Evaluates a resume against a given job description.

**## Request Data**

**Parameters:**

- **resume_text** (str, required): The text content of the resume to evaluate.
- **job_description** (str, required): The text content of the job description to compare against.

**Format:**

```json
{
    "resume_text": "(resume content here)",
    "job_description": "(job description content here)"
}
```

**## Response Data**

**Data Structure:**

```json
{
    "JD Match": "%",   // Percentage of JD match
    "MissingKeywords": [],   // List of missing keywords
    "Profile Summary": "(profile summary text here)"
}
```

**Example:**

```json
{
    "JD Match": "85%",
    "MissingKeywords": ["Python", "Machine Learning"],
    "Profile Summary": "Candidate has strong experience in data analysis and SQL, but lacks depth in Python and machine learning."
}
```

**## Required Packages:**
- Download requirements.txt using pip install -r requirements.txt
  * `fastapi`
  * `python-dotenv`
  * `google-generativeai`

**## Additional Notes**

* Ensure you have a valid Google API key configured in your environment variable `GOOGLE_API_KEY`.

