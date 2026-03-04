export interface PredictionRequest {
  features: number[];
}

export interface PredictionResponse {
  prediction: number;
  prediction_usd: number;
  prediction_usd_inflation_adjusted: number;
}
