import yfinance as yf
import datetime
from pandas_datareader import data as pdr
import pandas as pd


end_date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
start_date = "2017-01-01"

yf.pdr_override() # <== that's all it takes :-)


# download dataframe
data = pdr.get_data_yahoo("SPY", start=start_date, end=end_date)
days = data.axes[0]
days_data = []
for day in days:
    days_data.append(datetime.datetime.strftime(day, "%Y-%m-%d"))
days_df = pd.DataFrame(days_data)
days_df.to_csv('all_days.csv',mode = 'w', index=False, header=False)

# randomly select 30 days of data
import random
import numpy as np

random.seed(42)
random_dates = random.sample(sorted(days), 30)
random_dates = np.sort(random_dates)
random_df = pd.DataFrame(random_dates)
random_df.to_csv("random_days.csv", mode = 'w', index=False, header=False)

