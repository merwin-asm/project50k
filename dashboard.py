from flask import Flask, jsonify, request, render_template

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # enable CORS for all routes


# Sample data (as you already had) ...
employee_satisfaction = 5
employee_complaints = 15
survey_rating = 4.2
behavior_score = 90

employee_surveys = [
    {"name": "Alice Smith", "date": "2025-07-15", "rating": 4.5, "comments": "Good work environment"},
    {"name": "Bob Johnson", "date": "2025-07-20", "rating": 3.8, "comments": "Need more training"},
    {"name": "Charlie Brown", "date": "2025-07-25", "rating": 4.7, "comments": "Great team support"}
]

simulations = [
    {"NAME": "SIM-123", "typ": "Performance", "date": "2025-08-01", "result": "Passed"},
    {"NAME": "SIM-456", "typ": "Compliance", "date": "2025-08-05", "result": "Failed"}
]

conversations = [
    {"id": "CONV-789", "topic": "Project feedback", "date": "2025-08-10", "participants": "4"},
    {"id": "CONV-101", "topic": "Team meeting", "date": "2025-08-12", "participants": "8"}
]

critical_situations = [
    {"name": "Sarah Lee", "situation": "Low performance in last quarter"},
    {"name": "Michael Chen", "situation": "High employee complaints"},
    {"name": "Emily White", "situation": "Low survey rating"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    return jsonify({
        "satisfaction": employee_satisfaction,
        "complaints": employee_complaints,
        "survey_rating": survey_rating,
        "behavior": behavior_score
    })

@app.route('/api/surveys', methods=['GET'])
def get_surveys():
    search = request.args.get('search')
    if search:
        results = [s for s in employee_surveys if search.lower() in s['name'].lower()]
    else:
        results = employee_surveys
    return jsonify(results)

@app.route('/api/simulations', methods=['GET'])
def get_simulations():
    search = request.args.get('search')
    if search:
        results = [s for s in simulations if search.lower() in s['id'].lower()]
    else:
        results = simulations
    return jsonify(results)

@app.route('/api/conversations', methods=['GET'])
def get_conversations():
    search = request.args.get('search')
    if search:
        results = [c for c in conversations if search.lower() in c['id'].lower()]
    else:
        results = conversations
    return jsonify(results)

@app.route('/api/critical', methods=['GET'])
def get_critical_situations():
    return jsonify(critical_situations)

if __name__ == "__main__":
    app.run(debug=True)

