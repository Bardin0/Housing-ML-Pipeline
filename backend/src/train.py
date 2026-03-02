import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import RandomizedSearchCV
import joblib
import os

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, preds))
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    return rmse, mae, r2

def optimize_random_forest(X_train, y_train):
    param_dist = {
        "n_estimators": [200, 300, 400],
        "max_depth": [10, 15, 20, 25, None],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "max_features": ["sqrt", "log2"]
    }

    base_model = RandomForestRegressor(random_state=42, n_jobs=-1)

    search = RandomizedSearchCV(
        base_model,
        param_distributions=param_dist,
        n_iter=25,
        cv=5,
        scoring="neg_root_mean_squared_error",
        verbose=2,
        random_state=42,
        n_jobs=-1
    )

    search.fit(X_train, y_train)

    return search.best_estimator_, search.best_params_

def save_model(model, scaler, path="models"):
    os.makedirs(path, exist_ok=True)

    joblib.dump(model, f"{path}/model.joblib")
    joblib.dump(scaler, f"{path}/scaler.joblib")

    print("Model and scaler saved.")