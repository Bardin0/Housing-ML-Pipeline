from data_processing import preprocess_data
from train import (
    optimize_random_forest,
    evaluate_model, 
    save_model
)


def main():
    X_train, X_test, y_train, y_test, scaler = preprocess_data()

    print("Optimizing Random Forest...")
    best_rf, best_params = optimize_random_forest(X_train, y_train)
    rf_metrics = evaluate_model(best_rf, X_test, y_test)

    print("\n--- Optimized Random Forest ---")
    print("Best Parameters:", best_params)
    print(f"Optimized RF → RMSE: {rf_metrics[0]:.3f}, MAE: {rf_metrics[1]:.3f}, R²: {rf_metrics[2]:.3f}") 
    save_model(best_rf, scaler)

if __name__ == "__main__":
    main()