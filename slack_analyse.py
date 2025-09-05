from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime
import ai
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
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
slack_token = ""
client = WebClient(token=slack_token)

channel_id = "C09CEFTF4Q2"

def get_user_name(user_id):
    try:
        response = client.users_info(user=user_id)
        return response["user"]["real_name"]
    except:
        return user_id  


def fetch_slack_messages(channel_id, limit=60):
    try:
        response = client.conversations_history(channel=channel_id, limit=limit)
        messages = response.get("messages", [])

        formatted = []
        for msg in messages:
            ts = float(msg["ts"])
            dt = datetime.fromtimestamp(ts)
            sender = get_user_name(msg.get("user", "unknown"))
            if not sender.startswith('U0'):
                formatted.append({
                "date": dt.strftime("%Y-%m-%d"),
                "time": dt.strftime("%H:%M:%S"),
                "sender": sender,
                "msg": msg.get("text", "")
                })
        
        return formatted
    except SlackApiError as e:
        print("Error fetching messages:", e)
        return []

def chat_analysis():
    chats = fetch_slack_messages(channel_id)

    return json.loads(ai.ai("So this is a company group chat data, analayse it and give people score based on their engagement and readiness. the output format should be in json only and no additional data, the formate is [{name:name, score:score, ...}], score should be out of 10.: " + str(chats)).replace("```json","").replace("\n", "").replace("```", ""))
def to_name(user_id):
    try:
        response = client.users_info(user=user_id)
        user = response["user"]

        # Options you can use:
        username = user["name"]             
        display_name = user["profile"]["display_name"] or user["real_name"]
        real_name = user["profile"]["real_name"]

        return real_name

    except SlackApiError as e:
        print(f"Error fetching user info: {e.response['error']}")

def upload_analysis():
    data =chat_analysis()
    print(data)
    convo.insert_many(data)

if __name__ == '__main__':
    upload_analysis()
