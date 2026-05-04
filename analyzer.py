from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

def resume_analyzer(resume_sample, job_desc):

    response = client.responses.create(
        model = "gpt-5",
        input = f"""You are a resume analyzer. Analyze {resume_sample} against {job_desc}.
                    Reply in the following format:
                    ''Match Score: (out of 100)
                      Strengths:
                      Missing Skills:
                      Suggestions: ''
        """
    )

    for item in response.output:
        if item.type == "message":
            return item.content[0].text

    return "No analysis generated"        
