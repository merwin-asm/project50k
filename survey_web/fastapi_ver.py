from fastapi import FastAPI, Request
from pydantic import BaseModel
from database import survey_entry, get_survey
from fastapi.middleware.cors import CORSMiddleware
import ai
import json
app = FastAPI()

# Allow all origins (for dev). You can restrict in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] if frontend runs on port 3000
    allow_credentials=True,
    allow_methods=["*"],  # allows GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],
)

class Surv(BaseModel):
    name: str
    age: str
    gender: str
    virtual_meetings: str
    job_role: str
    years_at_company: str
    employment_type: str
    work_hours: str
    performance_rating: str
    job_satisfaction: str
    stress_level: str
    work_life_balance: str
    experienced_bias: str
    inclusion_score: str
    feedback: str

surveys = []

@app.get("/")

def root():
    return {"hello": "myguy"}

@app.post("/survey")
async def create_survery(request: Request):
    data = await request.json()  # parse raw JSON
    surv = dict(data)

    surv.setdefault('complain', int(
        ai.ai(f"Does this seem like a negative or possitive feedback. if it is a possitive one return 0 and if it is a negative one return 1. dont return nothing else. this is the text ''{surv['feedback']}''.").replace("\n","").replace(" ", "")
        )
                    )

    survey_entry(surv)

@app.get("/surveys")
def get_all_surveys():
    return surveys

@app.get("/surveys/{sn}")
def get_specific_survey(sn: str):
    try:
          return get_survey(sn)
    except:
        return {"error": "Survey not found"}
