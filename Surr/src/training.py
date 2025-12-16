import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import StackingClassifier
from xgboost import XGBClassifier

current_dir = os.path.dirname(__file__)

df_path = os.path.join(current_dir, '..', 'data', 'processed', 'processed.csv')
train_path = os.path.join(current_dir, '..', 'data', 'train', 'train.csv')
test_path = os.path.join(current_dir, '..', 'data', 'test', 'test.csv')

df = pd.read_csv(df_path)
train = pd.read_csv(train_path)
test = pd.read_csv(test_path)

print('csv cargados')

X = df.drop(columns=['equipo_ganador'])
y = df['equipo_ganador']

print('X e y definidas')

X_train = train.drop(columns=['equipo_ganador'])
y_train = train['equipo_ganador']
X_test = test.drop(columns=['equipo_ganador'])
y_test = test['equipo_ganador']

scaler = StandardScaler()
scaler.fit(X_train)
X_train_scal = scaler.transform(X_train)
X_test_scal = scaler.transform(X_test)
X_scal = scaler.transform(X)

print('X escaladas')

scaler_path = os.path.join(current_dir, '..', 'models', 'scaler.pkl')

with open(scaler_path, "wb") as f:
    pickle.dump(scaler, f)

print('pickle scaler guardado')



lr = LogisticRegression(max_iter=1000)
svc = SVC(C=100, gamma=0.001, kernel="rbf", probability=True)
xgb = XGBClassifier(
colsample_bytree=0.8,
learning_rate=0.05,
max_depth=3,
n_estimators=150,
subsample=0.8,
objective="binary:logistic",
eval_metric="auc",
random_state=42
)

stack = StackingClassifier(
estimators=[
("lr", lr),
("svc", svc),
("xgb", xgb)
],
final_estimator=LogisticRegression(max_iter=1000),
cv=5,
n_jobs=-1
)

stack.fit(X_train_scal, y_train)

stack_path = os.path.join(current_dir, '..', 'models', 'final_model_stacking.pkl')

with open(stack_path, "wb") as f:
    pickle.dump(stack, f)

print('pickle Stacking Classifier guardado')

