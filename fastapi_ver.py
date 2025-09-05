from fastapi import FastAPI, Request
from db import survey_entry, get_survey
from fastapi.middleware.cors import CORSMiddleware
import ai
import json
import uvicorn
app = FastAPI()

# Allow all origins (for dev). You can restrict in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] if frontend runs on port 3000
    allow_credentials=True,
    allow_methods=["*"],  # allows GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],
)

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

if __name__ == "__main__":
    uvicorn.run("fastapi_ver:app", host="0.0.0.0", port=8900, reload=True)

