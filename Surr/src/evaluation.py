import pickle
import pandas as pd
from sklearn.metrics import (confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report)
import os

current_dir = os.path.dirname(__file__)

test_path = os.path.join(current_dir, "..", "data", "test", "test.csv")
stack_path = os.path.join(current_dir, "..", "models", "final_model_stacking.pkl")
scaler_path = os.path.join(current_dir, "..", "models", "scaler.pkl")

target = "equipo_ganador"


test_df = pd.read_csv(test_path)

X_test = test_df.drop(columns=[target])
y_test = test_df[target]


with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)

with open(stack_path, "rb") as f:
    model = pickle.load(f)

X_test_scal = scaler.transform(X_test)

y_pred = model.predict(X_test_scal)
y_pred_proba = model.predict_proba(X_test_scal)[:, 1]


cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc = roc_auc_score(y_test, y_pred_proba)


print("\n===== EVALUACIÓN MODELO STACKING =====\n")
print("Confusion Matrix:\n", cm)
print(f"Accuracy : {acc:.4f}")
print(f"Precision: {prec:.4f}")
print(f"Recall   : {rec:.4f}")
print(f"F1-score : {f1:.4f}")
print(f"ROC-AUC  : {roc:.4f}")

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
