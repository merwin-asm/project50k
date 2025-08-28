from flask import Flask, render_template, request, redirect, url_for
import mdb

app = Flask(__name__)

@app.route("/")
def index():
    with open("index.html", "r") as f:
        return f.read()
@app.route("/submit", methods=["POST"])
def submit():
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

    # You can save this data into a database or file
    print("Received: ", res)
    mdb.add_survey(res)
    return redirect(url_for("thankyou"))

@app.route("/thankyou")
def thankyou():
    with open("thankyou.html", "r") as f:
        return f.read()
if __name__ == "__main__":
    app.run()

