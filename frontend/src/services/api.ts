import axios from "axios";
import { type PredictionRequest, type PredictionResponse } from "../types/prediction";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export const predictPrice = async (
    data: PredictionRequest,
): 
Promise<PredictionResponse> => {
  const response = await api.post<PredictionResponse>("/predict", data);
  return response.data;
};
