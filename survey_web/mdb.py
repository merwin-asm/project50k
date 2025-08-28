from pymongo import MongoClient

port = "27017"
client = MongoClient("mongodb://localhost:"+port+"/")

db = client["employees"]

survey = db["survey"]

def add_survey(data):
    global survey
    survey.insert_one(data)

def get_survey(name):
    return survey.find_one({"employee":name}):
        

