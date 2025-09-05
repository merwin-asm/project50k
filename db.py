"""
bringitvit_db_user
UDu8nkyHq6zmXjtR
"""


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from wellbeing_predictor import predict_wellbeing
from wlb_predictor import predict_work_life_balance
from slack_analyse import chat_analysis
from datetime import date
#predict_work_life_balance(employee_info)
#predict_wellbeing(employment_type, hours_worked, productivity_score)
"""

    example_employee = {
        'Age': 30,
        'Gender': 'Female',
        'Job_Role': 'Software Engineer',
        'Industry': 'IT',
        'Work_Location': 'Remote',
        'Stress_Level': 3,
        'Mental_Health_Condition': 'None',
        'Social_Isolation_Rating': 2,
        'Satisfaction_with_Remote_Work': 'Satisfied',
        'Hours_Worked_Per_Week':10, 'Number_of_Virtual_Meetings':3
    }
    rating = predict_work_life_balance(example_employee)
"""

uri = "mongodb+srv://bringitvit_db_user:UDu8nkyHq6zmXjtR@cluster0.moiglwg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["workspace"]
collection = db["employeesdata"]
behavior = db['behavior'] 
convo = db['convo']
def survey_entry(data):
    data.setdefault('date',str(date.today()))
    print(data)
    data.setdefault('rate', (predict_wellbeing(data['employment_type'], data['work_hours'])/100)*5)
    collection.insert_one(data)

def simulation_entry(data):
    behavior.insert_one(data)
def get_survey(name):
    return collection.find_one({"name":name}, {"_id": 0})
def simulation_delete(name):
    behavior.delete_one({'name':name})
def get_details():  
    c = 0
    for doc in collection.find():
        c += int(doc['complain'])
    r = 0
    for doc in collection.find():
        r += int(doc['rate'])
        print(r)
    b = 0
    for doc in behavior.find():
        b += int(doc['rate'])
     
    #print( c/collection.count_documents({}) , r/collection.count_documents({}), 10, (-c/collection.count_documents({}) + r/collection.count_documents({}) + 10) )
    # scale z (1-5) → (0-100)
    z_scaled = ((r/collection.count_documents({})) - 1) / 4 * 100  # 1→0%, 5→100%

    # formula: x + z - y
    raw_score = b + z_scaled - (c/collection.count_documents({}))

    # clamp result to [0, 100]
    final_score = max(0, min(100, raw_score))

    return (c/collection.count_documents({}))*100 , (r/collection.count_documents({})), b, final_score
def get_all_survey():
    return list(collection.find({}, {"_id": 0}))
def get_all_simulation():
    return list(behavior.find({}, {"_id": 0}))
def get_simulation(name):
    return behavior.find_one({"name":name},  {"_id": 0})

def convo_entry(data):
    convo.insert_one(data)
def get_all_convo():
    x =  list(convo.find({}, {"_id": 0}))
    for e in x:
        if e['name'] == 'Demo App2':
            x.remove(e)
            break
    return x
def get_convo(name):
    return convo.find_one({"name":name}, {"_id": 0})
def critical():
    critical = []
    for e in get_all_survey():
        if int(e['rate']) < 2:
            if e['name'] != 'Demo App2':
                critical.append({'name': e['name'], "situation": "Very low score in survey"})
    for e in get_all_simulation():
        if int(e['rate']) < 2:
            if e['name'] != 'Demo App2':
                critical.append({'name': e['name'], "situation": "Very low score in behavior analysis"})
    for e in get_all_convo():
        if int(e['score']) < 2:
            if e['name'] != 'Demo App2':
                critical.append({'name': e['name'], "situation": "Very low score in conversation analysis"})
    return critical
