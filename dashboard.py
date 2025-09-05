from flask import Flask, jsonify, request, render_template

from flask_cors import CORS
import db

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
    c, r, b, s = db.get_details()
    return jsonify({
        "satisfaction": s,
        "complaints": c,
        "survey_rating": r,
        "behavior": b
    })

@app.route('/api/surveys', methods=['GET'])
def get_surveys():
    search = request.args.get('search')
    if search:
        results = db.get_survey(search)
    else:
        results = db.get_all_survey()
        n_results = []
        # age	complain	date	employment_type	experience_bias	feedback	gender	inclusion_score	job_role	job_satisfaction	name	performance_rating	rate	stress_level	virtual_meetings	work_hours	work_life_balance	years_at_company
        for r in results:
            n_results.append({'name':r['name'], 'age':r['age'], 'date':r['date'], 'rate':r['rate'], 'EType':r['employment_type'], 'Stress':r['stress_level'], 'WLB':r['work_life_balance'], 'VM':r['virtual_meetings'], 'Feedback':r['feedback']})
    print(n_results)
    return jsonify(n_results)

@app.route('/api/simulations', methods=['GET'])
def get_simulations():
    search = request.args.get('search')
    if search:
        results = db.get_simulation(search)
    else:
        results = db.get_all_simulation()
    return jsonify(results)

@app.route('/api/conversations', methods=['GET'])
def get_conversations():
    search = request.args.get('search')
    if search:
        results = db.get_convo(search)
    else:
        results = db.get_all_convo()
    return jsonify(results)

@app.route('/api/critical', methods=['GET'])
def get_critical_situations():
    return jsonify(db.critical())

if __name__ == "__main__":
    app.run(debug=True)

