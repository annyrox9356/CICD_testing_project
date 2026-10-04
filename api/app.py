from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Load the saved model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Input data schema validator (Ab 3 features ke sath)
class CustomerData(BaseModel):
    Age: int
    AnnualSalary: int
    CreditScore: int

@app.post("/predict")
def predict_purchase(data: CustomerData):
    # Model ko 2D array me data chahiye
    input_data = [[data.Age, data.AnnualSalary, data.CreditScore]]
    prediction = model.predict(input_data)
    
    result = "Tiwari ji Kharid lenge " if prediction[0] == 1 else "Tiwari ji nahi kharidenge"
    return {"prediction": result}