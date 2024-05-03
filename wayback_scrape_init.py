from waybackpy import WaybackMachineSaveAPI, WaybackMachineCDXServerAPI

# https://web.archive.org/web/20240000000000*/finviz.com
tickers = ["MSFT"]
web_url = "https://finviz.com" # /quote.ashx?t=
# user_agent = "my new app's user agent"
# start timestamp is 2 years ago
cdx_api = WaybackMachineCDXServerAPI(web_url, start_timestamp=2021, end_timestamp=2023)


# for item in cdx_api.snapshots():
#     print(item.archive_url) # I just copied and pasted into finvizurls.txt

with open("finvizurls.txt", "w") as f:
    for item in cdx_api.snapshots():
        f.write(item.archive_url + "\n")