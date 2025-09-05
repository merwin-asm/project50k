import json
import ai
from flask import Flask, jsonify, request, render_template, send_from_directory, abort
from flask_cors import CORS
import db
import time
import random

import os


app = Flask(__name__)
CORS(app)  # enable CORS for all routes

chats = {}
condition = {}

def scenario():
    with open('seed.json', 'r') as f:
        return random.choice(json.loads(f.read()))
@app.route('/', methods=['GET'])
def index():
    with open("index.html", 'r') as f:
        return f.read()
@app.route('/<file>', methods=['GET'])
def index2(file):
    with open(file, 'r') as f:
        return f.read()

BASE_DIR = os.path.abspath("assets")  # or r"C:\path\to\assets"


@app.route('/<path:filename>')
def serve_file(filename):
    # Full path of the requested file
    full_path = os.path.abspath(os.path.join(BASE_DIR, filename))

    # Security check: ensure the requested path is inside BASE_DIR
    if os.path.isfile(full_path) and os.path.commonpath([BASE_DIR, full_path]) == BASE_DIR:
        return send_from_directory(BASE_DIR, filename)
    else:
        abort(404)
@app.route('/assets/<path:filename>')
def serve_asset2(filename):
    # Build absolute path for requested file
    full_path = os.path.abspath(os.path.join(BASE_DIR, filename))

    # Security check: ensure file is inside BASE_DIR
    if os.path.isfile(full_path) and os.path.commonpath([BASE_DIR, full_path]) == BASE_DIR:
        return send_from_directory(BASE_DIR, filename)
    else:
        abort(404)


@app.route('/bot_reply', methods=['GET'])
def bot_reply():
    global chats, condition
    name = request.headers.get('name')
     
    try:
        print("sdsd", chats[name])
        
        reply =  ai.ai(f"Continue this conversation , what will be the bot reply .  In this convo first bot asked {chats[name][0]} and the reply by user was {chats[name][1]} . so the bot reply should be positive if the user reply was similar to these '{condition[name]['pos']}' and the bot reply should be negative if the user reply was similar to these '{condition[name]['neg']}'. the bot reply should be like a short conclution reply. the reply should be json in format"+ "{'positive':True/False, 'reply':reply}. i dont want no other text generated.").replace('\n', '').replace("`", "").replace("json", "")      
        reply = json.loads(reply)
        pos = reply['positive']
        reply = reply['reply']
        print(reply)
        if pos:
            new_mark =  1
        else:
            new_mark = 0
        #if request.method != "OPTIONS":
        del chats[name]
        del condition[name]
        
        x = db.get_simulation(name)
        if not x:
            x = {
            'mark' :0 ,
            'total':0
                    }
        mark = int(x['mark'])
        total = int(x['total'])
        try:
            db.simulation_delete(name)
        except:
            pass
        db.simulation_entry({'name':name, 'mark': mark + new_mark, 'total':total+1, 'rate': (mark+new_mark)/(total+1)})
        return str( reply)
    except Exception as e:
        print(e)
        s = scenario()

        chats.setdefault(name, [s['Scenario']])
        condition.setdefault(name, s['actions'])
        return  str( s['Scenario'])

@app.route('/bot_reply2', methods=['GET'])
def bot_reply2(): 
    pass
@app.route('/user_reply', methods=['GET'])
def user_reply():
    global chats, condition
    name = request.headers.get('name')
    text = request.headers.get('text')
    print(name)
    chats[name].append(text)
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
