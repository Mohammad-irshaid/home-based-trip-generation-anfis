import numpy as np

from sklearn.metrics import mean_squared_error

from anfis_toolbox import ANFISRegressor


class ANFISModel:

    def __init__(
        self,
        n_mfs=3,
        mf_type="gaussian",
        optimizer="hybrid",
        max_epochs=1000
    ):

        self.n_mfs = n_mfs
        self.mf_type = mf_type
        self.optimizer = optimizer
        self.max_epochs = max_epochs

        self.best_model = None
        self.best_epoch = 0
        self.best_test_rmse = np.inf

        self.train_rmse_history = []
        self.test_rmse_history = []

    def train(
        self,
        X_train,
        y_train,
        X_test,
        y_test
    ):

        print("\nTraining ANFIS...\n")

        for epoch in range(1, self.max_epochs + 1):

            model = ANFISRegressor(
                n_mfs=self.n_mfs,
                mf_type=self.mf_type,
                optimizer=self.optimizer,
                epochs=epoch,
                verbose=False
            )

            model.fit(X_train, y_train)

            train_pred = model.predict(X_train)
            test_pred = model.predict(X_test)

            train_rmse = np.sqrt(
                mean_squared_error(y_train, train_pred)
            )

            test_rmse = np.sqrt(
                mean_squared_error(y_test, test_pred)
            )

            self.train_rmse_history.append(train_rmse)
            self.test_rmse_history.append(test_rmse)

            print(
                f"Epoch {epoch:3d} | "
                f"Train RMSE: {train_rmse:.4f} | "
                f"Test RMSE: {test_rmse:.4f}"
            )

            # EARLY STOPPING
            if test_rmse < self.best_test_rmse:

                self.best_test_rmse = test_rmse
                self.best_epoch = epoch
                self.best_model = model

            else:

                print("\nValidation error increased.")
                print("Stopping training to avoid overfitting.")

                break

        print("\nBEST MODEL")
        print(f"Best Epoch: {self.best_epoch}")
        print(f"Best Test RMSE: {self.best_test_rmse:.4f}")

    def predict(self, X):

        return self.best_model.predict(X)
