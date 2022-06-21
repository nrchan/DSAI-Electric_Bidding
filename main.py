import argparse
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import datetime

# You should not modify this part.
def config():

    parser = argparse.ArgumentParser()
    parser.add_argument("--consumption", default="./sample_data/consumption.csv", help="input the consumption data path")
    parser.add_argument("--generation", default="./sample_data/generation.csv", help="input the generation data path")
    parser.add_argument("--bidresult", default="./sample_data/bidresult.csv", help="input the bids result path")
    parser.add_argument("--output", default="output.csv", help="output the bids path")

    return parser.parse_args()


def output(path, data):

    df = pd.DataFrame(data, columns=["time", "action", "target_price", "target_volume"])
    df.to_csv(path, index=False)

    return


if __name__ == "__main__":
    args = config()

    generation = pd.read_csv(args.generation)
    consumption = pd.read_csv(args.consumption)

    diff = generation["generation"] - consumption["consumption"]

    train = diff[:-24]
    model = ARIMA(train, seasonal_order=(1,1,1,24), enforce_stationarity=False, enforce_invertibility=False)
    model = model.fit(method_kwargs={"warn_convergence": False})

    forecast = model.predict(start=len(train)+1, end=len(train)+24)

    """
    plt.figure(figsize = (10,6))
    plt.plot(diff, label = "true values", color = "cornflowerblue")
    plt.plot(forecast,label = "forecasts", color='darkorange')
    plt.title("SARIMA Model", size = 14)
    plt.show() 
    score = mean_squared_error(diff[-24:], forecast, squared = False)
    print('RMSE: {}'.format(round(score,4)))

    """
    lastday = pd.to_datetime(generation["time"][len(generation)-1])
    data = []

    for i in forecast:
        lastday += datetime.timedelta(hours=1)
        if i < 0:
            data.append([lastday.strftime("%Y-%m-%d %H:%M:%S"), "buy", 2, abs(i)/2])
            data.append([lastday.strftime("%Y-%m-%d %H:%M:%S"), "buy", 1.5, abs(i)/2])

    
    #data = [["2018-01-01 00:00:00", "buy", 2.5, 3],
    #        ["2018-01-01 01:00:00", "sell", 3, 5]]
    output(args.output, data)
