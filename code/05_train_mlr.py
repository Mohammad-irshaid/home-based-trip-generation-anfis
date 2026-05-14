from preprocessing import (
    load_data,
    split_and_scale
)

from mlr_model import MLRModel

from metrics import evaluate_model


# LOAD DATA
X, y = load_data(
    "data/raw/salfit_trip_data.csv"
)

# SPLIT DATA
(
    X_train,
    X_test,
    y_train,
    y_test,
    _,
    _,
    _
) = split_and_scale(X, y)

# TRAIN MODEL
model = MLRModel()

model.train(X_train, y_train)

# PREDICTIONS
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

# EVALUATION
train_metrics = evaluate_model(
    y_train,
    train_pred
)

test_metrics = evaluate_model(
    y_test,
    test_pred
)

print("\nMLR TRAINING RESULTS")
print(train_metrics)

print("\nMLR TESTING RESULTS")
print(test_metrics)
