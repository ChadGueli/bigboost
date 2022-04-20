import xgboost as xgb
import numpy as np
from flask import Flask

from math import pi

app = Flask(__name__)

@app.route('/')
def hello_model():
    model = xgb.XGBRegressor()
    model.load_model("smallmodel.txt")
    
    rng = np.random.default_rng()
    x = rng.uniform(size=20)

    pred = model.predict(x[np.newaxis, ...])
    true = 2*np.sin(pi*x[0]*x[1]) + (2*x[2] - 1)**2 + 2*x[3] + x[4]
    true = 5*true + 0.1*rng.normal(size=1)

    return f'Prediction: {pred}\n Error: {(true-pred)**2}\n n.b. model suboptimal to save time'


if __name__ == "__main__":
  app.run(host ='0.0.0.0')