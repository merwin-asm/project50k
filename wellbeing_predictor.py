import joblib
import numpy as np

# Load model and encoder
model = joblib.load("wellbeing_model.pkl")
le = joblib.load("label_encoder.pkl")

def predict_wellbeing(employment_type, hours_worked, productivity_score):
    """
    Predict Well-Being Score for an employee.
    
    Parameters:
        employment_type (str): "Remote" or "In-Office"
        hours_worked (float): Hours worked per week
        productivity_score (float): Productivity score (0-100)
        
    Returns:
        float: Predicted Well-Being Score
    """
    # Convert employment_type to numeric
    employment_numeric = le.transform([employment_type])[0]
    
    # Prepare features
    features = np.array([[employment_numeric, hours_worked, productivity_score]])
    
    # Predict
    predicted_score = model.predict(features)[0]
    return predicted_score

# Example usage
if __name__ == "__main__":
    score = predict_wellbeing("Remote", 40, 80)
    print(f"Predicted Well-Being Score: {score:.2f}")

