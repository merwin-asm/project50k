import joblib
import numpy as np


model = joblib.load("wellbeing_model.pkl")
le = joblib.load("label_encoder.pkl")

def predict_wellbeing(employment_type, hours_worked):
    """

        employment_type (str): "Remote" or "In-Office"
        hours_worked (float): Hours worked per week
        productivity_score (float): Productivity score (0-100)
        

        float: Predicted Well-Being Score
    """

    employment_numeric = le.transform([employment_type])[0]
    
    features = np.array([[employment_numeric, hours_worked]])
    
    predicted_score = model.predict(features)[0]
    return predicted_score


if __name__ == "__main__":
    score = predict_wellbeing("Remote", 40,)
    print(f"Predicted Well-Being Score: {score:.2f}")

