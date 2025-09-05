import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib  
import numpy as np

data = pd.read_csv("wellbeing.csv")

le = LabelEncoder()
data['Employment_Type'] = le.fit_transform(data['Employment_Type'])

X = data[['Employment_Type', 'Hours_Worked_Per_Week',]]
y = data['Well_Being_Score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(rmse)
r2 = r2_score(y_test, y_pred)
print(f"Model trained. RMSE: {rmse:.2f}, R^2: {r2:.2f}")


joblib.dump(model, "wellbeing_model.pkl")
joblib.dump(le, "label_encoder.pkl")
print("Model and encoder saved!")

