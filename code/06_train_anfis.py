from preprocessing import (
    load_data,
    split_and_scale
)

from anfis_model import ANFISModel

from metrics import evaluate_model


# LOAD DATA
X, y = load_data(
    "data/raw/salfit_trip_data.csv"
)

# SPLIT AND SCALE
(
    _,
    _,
    y_train,
    y_test,
    X_train_scaled,
    X_test_scaled,
    _
) = split_and_scale(X, y)

# CREATE MODEL
model = ANFISModel(
    n_mfs=3,
    mf_type="gaussian",
    optimizer="hybrid",
    max_epochs=1000
)

# TRAIN
model.train(
    X_train_scaled,
    y_train,
    X_test_scaled,
    y_test
)

# PREDICTIONS
train_pred = model.predict(
    X_train_scaled
)

test_pred = model.predict(
    X_test_scaled
)

# EVALUATION
train_metrics = evaluate_model(
    y_train,
    train_pred
)

test_metrics = evaluate_model(
    y_test,
    test_pred
)

print("\nANFIS TRAINING RESULTS")
print(train_metrics)

print("\nANFIS TESTING RESULTS")
print(test_metrics)
