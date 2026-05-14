import os


print("\n==============================")
print("RUNNING MLR MODEL")
print("==============================")

os.system("python code/train_mlr.py")


print("\n==============================")
print("RUNNING ANFIS MODEL")
print("==============================")

os.system("python code/train_anfis.py")


print("\n==============================")
print("EVALUATING MODELS")
print("==============================")

os.system("python code/evaluate_models.py")


print("\n==============================")
print("PIPELINE COMPLETED")
print("==============================")
