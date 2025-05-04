# Example training script
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv('training.csv')
X = df[['voltage', 'current', 'temperature', 'soc']]
y = df['soh']

model = LinearRegression().fit(X, y)
joblib.dump(model, 'model.joblib')
