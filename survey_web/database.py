from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import date

uri = "mongodb+srv://bringitvit_db_user:UDu8nkyHq6zmXjtR@cluster0.moiglwg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


db = client["workspace"]
collection = db["employeesdata"]


def survey_entry(data):
    data.setdefault('date',str(date.today()))
    data.setdefault('rate', (predict_wellbeing(data['employement_type'], data['work_hours'])/100)*5)
    collection.insert_one(data)
def get_survey(name):
    return collection.find_one({"name":name})
def get_all_survey():
    return list(collection.find())
if '__main__' == __name__:
    survey_entry({'name': 'ihsaan',
    'age': 10,
    'gender': 'male',
    'department': 'pari',
    'job_role': 'owner',
    'years_at_company': 2,
    'work_hours': 1,
    'performance': 3,
    'job_satisfaction': 4,
    'stress_level': 2,
    'work_life_balance': 1,
    'experienced_bias': 0,
    'inclusion_score': 0,
    'feedback': 0})
