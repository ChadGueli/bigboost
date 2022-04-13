import xgboost as xgb
import numpy as np

model = xgb.XGBRegressor()
model.load_model("smallmodel.txt")
rng = np.random.default_rng()
X_deploy = rng.uniform(size=(10, 20))
print(model.predict(X_deploy))