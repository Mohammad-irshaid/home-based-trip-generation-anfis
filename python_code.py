import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
from anfis_toolbox import ANFISRegressor


# 1. LOAD DATASET
df = pd.read_csv("data/salfit_trip_data.csv")

# DEFINE INPUTS / OUTPUT
X = df[['EMP', 'EDU', 'DRV']]
y = df['HBALL']

# TRAIN / TEST SPLIT (80% TRAIN, 20% TEST)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# SCALE INPUTS
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# 2. MODEL DEVELOPMENT USING MLR
mlr = LinearRegression()
mlr.fit(X_train, y_train)

# PREDICTIONS
y_train_pred_mlr = mlr.predict(X_train)
y_test_pred_mlr = mlr.predict(X_test)

# METRICS
rmse_train_mlr = np.sqrt(mean_squared_error(y_train, y_train_pred_mlr))
rmse_test_mlr = np.sqrt(mean_squared_error(y_test, y_test_pred_mlr))

mae_train_mlr = mean_absolute_error(y_train, y_train_pred_mlr)
mae_test_mlr = mean_absolute_error(y_test, y_test_pred_mlr)

r2_train_mlr = r2_score(y_train, y_train_pred_mlr)
r2_test_mlr = r2_score(y_test, y_test_pred_mlr)



# 3. MODEL DEVELOPMENT USING ANFIS
max_epochs = 1000

train_rmse_history = []
test_rmse_history = []

best_test_rmse = np.inf
best_epoch = 0
best_model = None

print("\nTraining ANFIS...\n")

for epoch in range(1, max_epochs + 1):

    # CREATE MODEL
    model = ANFISRegressor(
        n_mfs=3,
        mf_type='gaussian',
        optimizer='hybrid',
        epochs=epoch,
        verbose=False
    )

    # TRAIN
    model.fit(X_train, y_train)

    # TRAIN PREDICTIONS
    y_train_pred = model.predict(X_train)
    train_rmse = np.sqrt(
        mean_squared_error(y_train, y_train_pred)
    )

    # TEST PREDICTIONS
    y_test_pred = model.predict(X_test)
    test_rmse = np.sqrt(
        mean_squared_error(y_test, y_test_pred)
    )

    # STORE HISTORY
    train_rmse_history.append(train_rmse)
    test_rmse_history.append(test_rmse)

    print(
        f"Epoch {epoch:3d} | "
        f"Train RMSE: {train_rmse:.4f} | "
        f"Test RMSE: {test_rmse:.4f}"
    )

    # EARLY STOPPING CONDITION
    if test_rmse < best_test_rmse:

        best_test_rmse = test_rmse
        best_epoch = epoch
        best_model = model

    else:
        print("\nValidation error started increasing.")
        print("Stopping training to avoid overfitting.")
        break

# FINAL BEST MODEL
print("\nBEST ANFIS MODEL")
print(f"Best Epoch : {best_epoch}")
print(f"Best Test RMSE : {best_test_rmse:.4f}")

# FINAL EVALUATION
y_train_pred_final = best_model.predict(X_train)
y_test_pred_final = best_model.predict(X_test)

# TRAIN RMSE, MAE, R2
rmse_train = np.sqrt(
    mean_squared_error(y_train, y_train_pred_final)
)

mae_train = mean_absolute_error(
    y_train,
    y_train_pred_final
)

r2_train = r2_zero_intercept(
    y_train,
    y_train_pred_final
)

# TEST RMSE, MAE, R2
rmse_test = np.sqrt(
    mean_squared_error(y_test, y_test_pred_final)
)

mae_test = mean_absolute_error(
    y_test,
    y_test_pred_final
)

r2_test = r2_zero_intercept(
    y_test,
    y_test_pred_final
)


# 4. PERFORMANCE COMPARISON AND VALIDATION

print("\n Training Results")
comparison_training = pd.DataFrame({
    'Method': ['MLR', 'ANFIS'],
    'RMSE': [
        rmse_train_mlr,
        rmse_train
    ],
    'MAE': [
        mae_train_mlr,
        mae_train
    ],
    'R2': [
        r2_train_mlr,
        r2_train
    ]
})
print(comparison_training)

print("\n Testing Results")
comparison_testing = pd.DataFrame({
    'Method': ['MLR', 'ANFIS'],
    'RMSE': [
        rmse_test_mlr,
        rmse_test
    ],
    'MAE': [
        mae_test_mlr,
        mae_test
    ]
})
print(comparison_testing)
