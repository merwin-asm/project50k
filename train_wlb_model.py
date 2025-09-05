import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib


data = pd.read_csv("work_life_balance.csv")


X = data[['Age', 'Gender', 'Job_Role', 
            "Number_of_Virtual_Meetings",
          'Hours_Worked_Per_Week']]
y = data['Work_Life_Balance_Rating']


categorical_cols = ['Gender', 'Job_Role', 'Industry',
            ]

numeric_cols = ['Age',  "Number_of_Virtual_Meetings",
          'Hours_Worked_Per_Week',"Work_Life_Balance_Rating"]

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ],
    remainder='passthrough'  # numeric columns stay as is
)

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


pipeline.fit(X_train, y_train)


y_pred = pipeline.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.2f}, R^2: {r2:.2f}")


joblib.dump(pipeline, 'wlb_model.pkl')
print("Model saved as wlb_model.pkl")

