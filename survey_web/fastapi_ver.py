from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Surv(BaseModel):
    name: str
    age: int
    gender: str
    department: str
    job_role: str
    years_at_company: int
    work_hours: int
    performance: int
    job_satisfaction: int
    stress_level: int
    work_life_balance: int
    experienced_bias: int
    inclusion_score: int
    feedback: int

# List to store surveys in memory
surveys = []

@app.get("/")
def root():
    return {"hello": "myguy"}

@app.post("/submit")
def create_survery(surv: Surv):
    surveys.append(surv)
    return {
        "message": "Survey stored successfully",
        "survey": surv
    }

@app.get("/surveys")
def get_all_surveys():
    return surveys

@app.get("/surveys/{sn}")
def get_specific_survey(sn: str):
    for survey in surveys:
        if survey.name == sn:
            return survey
    return {"error": "Survey not found"}
