from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load(os.path.join("../../models/model.joblib"))
scaler = joblib.load(os.path.join("../../models/scaler.joblib"))

class HouseFeatures(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: HouseFeatures):
    X = np.array(data.features).reshape(1, -1)
    X_scaled = scaler.transform(X)

    prediction = model.predict(X_scaled)[0]

    return {
            "prediction_raw": float(prediction),
            "prediction_usd": float(prediction) * 100000,
            "prediction_usd_inflation_adjusted": float(prediction) * 100000 * 2.46
            }
