import { useState } from "react";
import { predictPrice } from "../../services/api";
import { type PredictionRequest } from "../../types/prediction";

export default function InputForm() {
  const featureNames = [
    "Annual Income",
    "House Age",
    "Number of Rooms Total",
    "Number of Bedrooms Total",
    "Population (Within Block)",
    "Number of Occupants",
    "Latitude",
    "Longitude",
  ];

  const [features, setFeatures] = useState<number[]>(Array(8).fill(0));
  const [prediction, setPrediction] = useState<number | null>(null);

  const handleChange = (index: number, value: string) => {
    const updated = [...features];
    updated[index] = Number(value);
    setFeatures(updated);
  };

  const handleSubmit = async () => {
    const request: PredictionRequest = {
      features: features,
    };

    try {
      const result = await predictPrice(request);
      setPrediction(result.prediction_usd_inflation_adjusted);
    } catch (error) {
      console.error("Prediction failed:", error);
    }
  };

  return (
    <div>
      {featureNames.map((name, index) => (
        <div key={index} style={{ marginBottom: "10px" }}>
          <label>{name}</label>
          <br />
          <input
            type="number"
            value={features[index]}
            onChange={(e) => handleChange(index, e.target.value)}
          />
        </div>
      ))}

      <button onClick={handleSubmit}>Predict Price</button>

      {prediction !== null && (
        <p>Predicted price adjusted for inflation: ${prediction.toLocaleString()}</p>
      )}
    </div>
  );
}
