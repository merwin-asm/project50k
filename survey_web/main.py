from flask import Flask, request, jsonify
import mdb  # your custom database module

app = Flask(__name__)

@app.route("/")
def index():
    # Serve the HTML file directly
    with open("index.html", "r") as f:
        return f.read()

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json  # get JSON from JS
    res = {
        "name": data.get("name"),
        "age": data.get("age"),
        "gender": data.get("gender"),
        "department": data.get("department"),
        "job_role": data.get("job_role"),
        "years_at_company": data.get("years_at_company"),
        "work_hours": data.get("work_hours"),
        "performance": data.get("performance"),
        "job_satisfaction": data.get("job_satisfaction"),
        "stress_level": data.get("stress_level"),
        "work_life_balance": data.get("work_life_balance"),
        "experienced_bias": data.get("experienced_bias"),
        "inclusion_score": data.get("inclusion_score"),
        "feedback": data.get("feedback"),
    }

    # Save to your database
    print("Received: ", res)
    mdb.add_survey(res)

    return jsonify({"message": "Survey submitted successfully!"})

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)

