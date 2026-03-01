from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import os

app = FastAPI()

model = joblib.load(os.path.join("models/model.joblib"))
scaler = joblib.load(os.path.join("models/scaler.joblib"))

class HouseFeatures(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: HouseFeatures):
    X = np.array(data.features).reshape(1, -1)
    X_scaled = scaler.transform(X)

    prediction = model.predict(X_scaled)[0]

    return {"prediction": float(prediction)}