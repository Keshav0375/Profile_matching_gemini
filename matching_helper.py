from fastapi import FastAPI, Form
import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

app = FastAPI()


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_repsonse(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text


@app.post("/evaluate_resume")
async def evaluate_resume(resume_text: str = Form(...), job_description: str = Form(...)):
    # Call the Gemini model with the formatted input
    input = f"""
    Hey Act Like a skilled or very experience ATS(Application Tracking System)
    with a deep understanding of tech field,software engineering,data science ,data analyst
    and big data engineer. Your task is to evaluate the resume based on the given job description.
    You must consider the job market is very competitive and you should provide 
    best assistance for improving thr resumes. Assign the percentage Matching based 
    on Jd and
    the missing keywords with high accuracy
    resume:{resume_text}
    description:{job_description}

    I want the response in one single string having the structure
    {{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
    """
    response = get_gemini_repsonse(input)

    # Parse the response string into a dictionary
    response_dict = json.loads(response)

    return response_dict
