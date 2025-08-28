import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://abd:FZQ6qrHpmeWqIDfk@cluster0.dl0lc2h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster["workspace"]
collection = db["employeesdata"]


def survey_entry(data):
    collection.insert_one(data)
def get_survey(name):
    return collection.find_one({"name":name})
