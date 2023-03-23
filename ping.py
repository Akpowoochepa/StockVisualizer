import requests
import csv
from datetime import datetime

#test dates: 2022-03-01 -> 2022-03-31
def pingAPI(func, symbol, lowerDateStr, upperDateStr):
#MUQCQXXUYY3U4KUE
    # lowerDate = datetime.strptime(lowerDateStr, "%Y-%m-%d")
    # upperDate = datetime.strptime(upperDateStr, "%Y-%m-%d")
    if(func == 1):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=30min&apikey=MUQCQXXUYY3U4KUE&datatype=csv".format(symbol)
        lowerDate = datetime.strptime(lowerDateStr, "%Y-%m-%d %H:%M:%S")
        upperDate = datetime.strptime(upperDateStr, "%Y-%m-%d %H:%M:%S")
    elif(func == 2):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey=MUQCQXXUYY3U4KUE&datatype=csv".format(symbol)
        lowerDate = datetime.strptime(lowerDateStr, "%Y-%m-%d")
        upperDate = datetime.strptime(upperDateStr, "%Y-%m-%d")
    elif(func == 3):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={}&apikey=MUQCQXXUYY3U4KUE&datatype=csv".format(symbol)
        lowerDate = datetime.strptime(lowerDateStr, "%Y-%m-%d").date
        upperDate = datetime.strptime(upperDateStr, "%Y-%m-%d").date
    elif(func == 4):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={}&apikey=MUQCQXXUYY3U4KUE&datatype=csv".format(symbol)
        lowerDate = datetime.strptime(lowerDateStr, "%Y-%m-%d").date
        upperDate = datetime.strptime(upperDateStr, "%Y-%m-%d").date


    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=",")
        results = list(cr)
        dates = []
        for row in results:
            if(row[0] == "timestamp"):
                continue
            apiDate = datetime.strptime(row[0], "%Y-%m-%d")
            if(apiDate >= lowerDate and apiDate <= upperDate):
                dates.append(row)
       
    
    return dates

def main():
    results = pingAPI(2, "IBM", "2022-01-01", "2022-12-31")

    for result in results:
        print(result)

main()