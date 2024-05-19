from waybackpy import WaybackMachineSaveAPI, WaybackMachineCDXServerAPI
import random
from datetime import datetime, timedelta
import pandas as pd
import pytz

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
# cdx_api = WaybackMachineCDXServerAPI(web_url, start_timestamp=2014, end_timestamp=2024)

pct_change = pd.read_csv("pct_change.csv")
pct_change["Date"] = pd.to_datetime(pct_change["Date"])
# convert 20140203164808 UTC to 
for date in pct_change["Date"]:
    start = date - pd.Timedelta(days=7)

    # start = start.strftime("%Y%m%d%H%M%S")
    # end = date.strftime("%Y%m%d%H%M%S")
    start = start.strftime("%Y%m%d")
    end = date.strftime("%Y%m%d")
    # news must end before the s&p 500 opens
    print("start", start, "end", end)

    # convert from utc to eastern time

    # cutoffs are 09:30 and 16:30 EST
    est_cutoff_start = datetime.strptime("09:30", "%H:%M")
    est_cutoff_end = datetime.strptime("16:30", "%H:%M")


    cdx_api = WaybackMachineCDXServerAPI(web_url, start_timestamp=start, end_timestamp=date)

    # convert to yyyymmdd format
    with open("finvizurls.txt", "w") as f:
        snaps = cdx_api.snapshots()
        for item in snaps:
            print("item", item)
            item_date = item.timestamp.astimezone(est).strftime("%Y%m%d")
            hour_date_min = item.timestamp.astimezone(est).strftime("%H:%M")
            print("dates", item_date, hour_date_min, est_cutoff_start, est_cutoff_end)            
            if hour_date_min < est_cutoff_start or hour_date_min > est_cutoff_end:
                print("breaking")
                break
            # only write if the news is before the market opens and after the market closes
            f.write(item.archive_url + "\n")

