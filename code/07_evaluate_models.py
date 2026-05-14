import pandas as pd

from preprocessing import (
    load_data,
    split_and_scale
)

from mlr_model import MLRModel
from anfis_model import ANFISModel

from metrics import evaluate_model


# LOAD DATA
X, y = load_data(
    "data/raw/salfit_trip_data.csv"
)

(
    X_train,
    X_test,
    y_train,
    y_test,
    X_train_scaled,
    X_test_scaled,
    _
) = split_and_scale(X, y)

# =========================
# TRAIN MLR
# =========================

mlr = MLRModel()

mlr.train(X_train, y_train)

mlr_pred = mlr.predict(X_test)

mlr_metrics = evaluate_model(
    y_test,
    mlr_pred
)

# =========================
# TRAIN ANFIS
# =========================

anfis = ANFISModel()

anfis.train(
    X_train_scaled,
    y_train,
    X_test_scaled,
    y_test
)

anfis_pred = anfis.predict(
    X_test_scaled
)

anfis_metrics = evaluate_model(
    y_test,
    anfis_pred
)

# =========================
# COMPARISON TABLE
# =========================

comparison = pd.DataFrame({

    "Method": ["MLR", "ANFIS"],

    "RMSE": [
        mlr_metrics["RMSE"],
        anfis_metrics["RMSE"]
    ],

    "MAE": [
        mlr_metrics["MAE"],
        anfis_metrics["MAE"]
    ],

    "R2": [
        mlr_metrics["R2"],
        anfis_metrics["R2"]
    ]
})

print("\nMODEL PERFORMANCE COMPARISON\n")

print(comparison)

# SAVE RESULTS
comparison.to_csv(
    "results/model_comparison.csv",
    index=False
)

print("\nResults saved to:")
print("results/model_comparison.csv")
