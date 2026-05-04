from analyzer import resume_analyzer

with open("sample_resume.txt", "r") as file1:
    resume_sample = file1.read()

with open("job_description.txt", "r") as file2:
    job_desc = file2.read()

result = resume_analyzer(resume_sample, job_desc)  
print(result)      
