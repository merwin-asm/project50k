import joblib
import pandas as pd

pipeline = joblib.load('wlb_model.pkl')

def predict_work_life_balance(employee_info):
    """
        employee_info (dict): keys should match features:
            'Age', 'Gender', 'Job_Role', 'Industry', 'Work_Location',
            'Stress_Level', 'Mental_Health_Condition',
            'Social_Isolation_Rating', 'Satisfaction_with_Remote_Work'
    
    float: predicted rating
    """
    df = pd.DataFrame([employee_info])
    predicted_rating = pipeline.predict(df)[0]
    return predicted_rating

if __name__ == "__main__":
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
    print(f"Predicted Work-Life Balance Rating: {rating:.2f}")

