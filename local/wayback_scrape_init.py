from waybackpy import WaybackMachineSaveAPI, WaybackMachineCDXServerAPI
import random
from datetime import datetime, timedelta
import pandas as pd
import pytz
import time
from tqdm import tqdm
random.seed(0)
est = pytz.timezone('US/Eastern')
utc = pytz.utc

# https://web.archive.org/web/20240000000000*/finviz.com
web_url = "https://finviz.com" # /quote.ashx?t=
# user_agent = "my new app's user agent"
# start timestamp is 2 years ago

# randomly select 40 dates between 2014 and 2024

# for item in cdx_api.snapshots():
#     print(item.archive_url) # I just copied and pasted into finvizurls.txt
# cdx_api = WaybackMachineCDXServerAPI(web_url, start_timestamp=2014, end=2024)

pct_change = pd.read_csv("pct_change.csv")
dates = pd.read_csv("pct_change.csv")['Date']
# convert 20140203164808 UTC to 

num_segments = 10
scaler = len(dates) // num_segments # 15 per segment (rate limit)

print("num of segments", num_segments, "length", len(dates), "scaler", scaler)

for segment in range(1, num_segments + 1): # 1 to 15 inclusive
  indexed_dates = dates[(segment-1)*scaler:segment*scaler] if segment > 1 else dates[:segment*scaler] # dates[:index] gets everything exclusive that index
  
  print("segment", segment, "length", len(indexed_dates))

  for timestamp in indexed_dates: # includes segment so -1
      start = datetime.strptime(str(timestamp), "%Y-%m-%d") - timedelta(days=7) # 8 days back?
      start = start.strftime("%Y%m%d")
      end = datetime.strptime(str(timestamp), "%Y-%m-%d") - timedelta(days=1) # 1 day back so you avoid using news on the day of the prediction
      end = end.strftime("%Y%m%d")
      # news must end before the s&p 500 opens
      # print("start", start, "end", end)

      cdx_api = WaybackMachineCDXServerAPI(web_url, start_timestamp=start, end_timestamp=end)

      # convert to yyyymmdd format
      with open("finvizurls_dates.txt", "a") as f:
          snaps = cdx_api.snapshots()
          dates_seen = set()
          for item in snaps:
              if item.timestamp[:8] in dates_seen: # if you have already seen the data for this day, skip
                  continue
              # print("item", item)
              item_date = datetime.strptime(item.timestamp, "%Y%m%d%H%M%S").astimezone(est).strftime("%Y%m%d")
              hour_date_min = datetime.strptime(item.timestamp, "%Y%m%d%H%M%S").astimezone(est).strftime("%H:%M")
              # print("dates", item_date, hour_date_min)
              # only write if the news is before the market opens and after the market closes
              f.write(item.archive_url + "\n")
              dates_seen.add(item.timestamp[:8]) # only add one website snapshot for each day
              time.sleep(1)

          print("added", len(dates_seen), "snapshots of the website for date", start)

  print("TAKING A BREAK")
  for i in tqdm(range(150)):
    time.sleep(1)

  # time.sleep(150) # sleep for 60 min to get past rate limit?