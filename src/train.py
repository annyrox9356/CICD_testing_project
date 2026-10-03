import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# 1. Load Data
df = pd.read_csv("data/dataset.csv")

# 3 independent features
X = df[['Age', 'AnnualSalary', 'CreditScore']]
y = df['Purchased']

# 2. Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# 3. Save Model
with open("models/model.pkl", "wb") as f:
    pickle.dump(model,f)

print("Model trained on 3 features and saved as model.pkl successfully!")
