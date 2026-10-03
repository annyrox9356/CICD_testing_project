# src/generate_data.py
import pandas as pd
import numpy as np
import os

# Ensure folder exists
os.makedirs("../data", exist_ok=True)

np.random.seed(42)
n = 100
age = np.random.randint(18, 60, n)
salary = np.random.randint(20000, 150000, n)
credit_score = np.random.randint(300, 850, n)

purchase_prob = (age/60) * 0.3 + (salary/150000) * 0.4 + (credit_score/850) * 0.3
purchased = [1 if p > 0.55 else 0 for p in purchase_prob]

df = pd.DataFrame({'Age': age, 'AnnualSalary': salary, 'CreditScore': credit_score, 'Purchased': purchased})
# Path updated
df.to_csv('../data/dataset.csv', index=False)