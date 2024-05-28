import csv
import requests
from datetime import datetime, timedelta
def fetch_and_paginate_news(date):
    all_news_data = []
    next_page_token = None

    while True:
        headers = {
            "accept": "application/json",
            "APCA-API-KEY-ID": "PKCWWRQXRDUHA39IOI8N",
            "APCA-API-SECRET-KEY": "5kSov913hC4g1U0YZxBwUrNf98vO4lKMlcrlqavv"
        }

        url = "https://data.alpaca.markets/v1beta1/news"
        # actual_end_date is 1 day back from date
        actual_end_date = datetime.strptime(date, "%Y-%m-%d") - timedelta(days=1)
        actual_end_date = actual_end_date.strftime("%Y-%m-%d")

        actual_start_date = datetime.strptime(date, "%Y-%m-%d") - timedelta(days=7)
        actual_start_date = actual_start_date.strftime("%Y-%m-%d")
        
        params = {
            "start": actual_start_date,
            "end": actual_end_date,
            "limit": 50,
            "include_content": True,
            "exclude_contentless": False,
            "sort" : "asc",
            "symbols" : "MSFT,AAPL,NVDA,GOOG,GOOGL,AMZN,META,BRK-B,LLY,AVGO,JPM,TSLA,V,WMT,XOM,UNH,MA,PG,COST,JNJ,ORCL,MRK,HD,BAC,CVX,NFLX,ABBV,AMD,KO,CRM,PEP,QCOM,TMO,ADBE,WFC,LIN,DHR,TMUS,ACN,CSCO,MCD,DIS,GE,AMAT,TXN,ABT,AXP,CAT,INTU,VZ,AMGN,PFE,MS,NEE,IBM,PM,NOW,CMCSA,BX,GS,ISRG,MU,UNP,RTX,NKE,COP,SPGI,ETN,UBER,SCHW,INTC,HON,BKNG,SYK,LRCX,T,LOW,C,ELV,PGR,UPS,VRTX,BLK,TJX,ADI,LMT,BSX,REGN,MDT,CB,BA,KLAC,DE,PANW,MMC,ADP,PLD,ANET,CI,ABNB,MDLZ,SNPS,SBUX,FI,AMT,CMG,SO,WM,BMY,HCA,GD,GILD,APH,CDNS,DUK,ICE,MO,ZTS,CME,SHW,CL,TT,TDG,MCO,FCX,MCK,EQIX,CEG,ITW,NXPI,EOG,CVS,CTAS,NOC,PH,MAR,TGT,ECL,BDX,SLB,CSX,EMR,PYPL,MRNA,USB,MPC,PNC,AON,FDX,MSI,PSX,WELL,CARR,RSG,APD,ROP,ORLY,PCAR,SPG,MNST,MMM,AJG,OXY,VLO,EW,MCHP,COF,CPRT,AIG,SMCI,MET,TFC,NSC,HLT,DXCM,GM,AFL,JCI,WMB,TRV,GEV,NEM,F,PCG,SRE,AZO,PSA,ROST,DHI,GWW,DLR,OKE,AEP,FTNT,HES,KDP,TEL,ADSK,STZ,O,URI,EL,PAYX,KMB,D,BK,A,AMP,COR,KHC,ALL,FIS,LEN,PRU,IDXX,CCI,LHX,KMI,HUM,IQV,PWR,NUE,DOW,AME,HSY,CNC,OTIS,CHTR,MSCI,CMI,ACGL,YUM,CTVA,GIS,KR,IR,RCL,LULU,FAST,ODFL,PEG,KVUE,EXC,MPWR,GEHC,SYY,EA,VRSK,NDAQ,MLM,VST,CSGP,XYL,HWM,FANG,VMC,FICO,IT,CTSH,DD,DAL,LVS,ED,BKR,LYB,HPQ,HAL,DG,BIIB,MTD,GRMN,EXR,RMD,ON,GLW,CDW,DFS,PPG,DVN,TSCO,ROK,HIG,WAB,ADM,XEL,EFX,FSLR,VICI,ANSS,EIX,AVB,EBAY,CBRE,FTV,DECK,TTWO,TROW,GPN,RJF,CHD,WTW,BRO,WEC,FITB,TRGP,DOV,VLTO,DLTR,KEYS,MTB,AWK,EQR,IFF,WDC,WST,PHM,ZBH,HPE,NTAP,BR,IRM,CAH,DTE,ETR,NVR,STT,STE,TER,APTV,FE,ROL,LYV,HUBB,WY,PTC,BF-B,AXON,BALL,TSN,PPL,INVH,STLD,TYL,BLDR,K,ARE,LDOS,WRB,ES,GPC,SBAC,CTRA,WAT,HBAN,CCL,STX,MOH,MKC,PFG,ALGN,HRL,VTR,CBOE,TDY,AEE,WBD,CNP,COO,CPAY,OMC,CINF,ULTA,CMS,AVY,NRG,EQT,DRI,J,DPZ,RF,SYF,BAX,ESS,HOLX,VRSN,NTRS,ENPH,EG,UAL,ATO,ILMN,TXT,LH,ZBRA,CE,EXPD,FDS,L,PKG,CLX,IEX,JBHT,CFG,LUV,MAA,IP,DGX,GEN,BBY,NWS,NWSA,MAS,FOX,FOXA,ALB,AES,SWKS,BG,UDR,EXPE,CAG,JBL,MRO,AMCR,AKAM,SNA,CF,WRK,RVTY,POOL,\
                    TRMB,WBA,PNR,KEY,NDSN,CPB,DOC,SWK,HST,INCY,LW,LNT,TECH,PODD,NI,MGM,KIM,AOS,VTRS,JKHY,EVRG,BEN,DVA,IPG,UHS,EMN,SJM,LKQ,TAP,JNPR,CRL,CPT,REG,KMX,APA,RL,BBWI,ALLE,WYNN,BXP,EPAM,SOLV,CHRW,HII,FFIV,MOS,CTLT,PAYC,TFX,TPR,QRVO,HSIC,AAL,GNRC,DAY,AIZ,PNW,HAS,PARA,MKTX,FRT,BIO,BWA,MTCH,FMC,GL,MHK,CZR,ETSY,IVZ"
        }
        
        if next_page_token:
            url += "&page_token=" + next_page_token

        response = requests.get(url, params=params, headers=headers)
        print(url)
        data = response.json()

        # if 'news' not in data:
        #     print("error1")
        #     break
        print(data)

        all_news_data.extend(data['news'])
        next_page_token = data.get('next_page_token')

        if not next_page_token:
            print("error2")
            break

        break

    return all_news_data

# Read start dates from CSV
dates = []
with open('random_days.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        dates.extend(row)

# Fetch and paginate news for each start date
for date in dates:
    print("Fetching news for start date:", date)
    news_data = fetch_and_paginate_news(date)
    # Print a summary of the news data
    print("Number of news articles:", len(news_data))
    if len(news_data) > 0:
        print("First headline:", news_data[0]['headline'])
