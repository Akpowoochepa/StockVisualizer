import requests
import pygal
from lxml import etree, html
from StockFunctions import *
from StockTime import *
from ping import *
import pandas

def main():
    print("Stock Data Visualizer\n------------------------\n")

    # function to get the stock symbol from user
    stock_symbol = get_stock_symbol()

    print("\n\nChart Types\n--------------\n1. Bar\n2. Line\n")

    # function to get chart type from user
    chart_type = get_chart_type()

    # Call the function to get the time series option from the user
    time_series_option = get_time_series_option()

    # If time series option is Intraday, get the interval from the user
    if time_series_option == "1":
        time_series = "TIME_SERIES_INTRADAY"
        interval = input("Enter the interval (1min, 5min, 15min, 30min, 60min): ")
    else:
        interval = None

        # Determine the time series based on user's input
        if time_series_option == "2":
            time_series = "TIME_SERIES_DAILY"
        elif time_series_option == "3":
            time_series = "TIME_SERIES_WEEKLY"
        elif time_series_option == "4":
            time_series = "TIME_SERIES_MONTHLY"

    # Call the function to get the start date from the user
    start_date = get_start_date()

    # Call the function to get the end date from the user
    end_date = get_end_date(start_date)
    
    
    def DictionaryIterator(dict_obj):
        stack = [(k, v) for k, v in dict_obj.items()]
        while stack:
            k, v = stack.pop()
            if isinstance(v, dict):
                stack.extend([(k + '.' + k2, v2) for k2, v2 in v.items()])
            else:
                yield (k, v)


    def dataSeperator(valueKey):
        result = []
        for dictValues in DictionaryIterator(data):
            if dictValues[1] in inputRange and dictValues[2] == valueKey:
                result.append(eval(dictValues[3]))
        return list(reversed(result))

    def dateChecker():
        unique_values = set()
        result = []
        for dictValues in DictionaryIterator(data):
            value = dictValues[1]
            if value in inputRange and value not in unique_values:
                unique_values.add(value)
                result.append(value)
        return result[::-1]

   # pingAPI(time_series, stock_symbol, start_date, end_date)
    
    if time_series == 1:
        url = f'https://www.alphavantage.co/query?function={time_series}&symbol=' + stock_symbol + '&outputsize=full&interval=60min&outputsize=full&apikey=GIW0WKEDYCA4NMCQ'
        r = requests.get(url)
        data = r.json()
        inputRange = pandas.date_range(start_date, end_date, freq='H').strftime('%Y-%m-%d %h:%m:%s')
    elif time_series == 2:
        url = f'https://www.alphavantage.co/query?function={time_series}&symbol=' + stock_symbol + '&outputsize=full&apikey=GIW0WKEDYCA4NMCQ'
        r = requests.get(url)
        data = r.json()
        inputRange = pandas.date_range(start_date, end_date, freq='D').strftime('%Y-%m-%d')
    elif time_series == 3:
        url = f'https://www.alphavantage.co/query?function={time_series}&symbol=' + stock_symbol + '&outputsize=full&apikey=GIW0WKEDYCA4NMCQ'
        r = requests.get(url)
        data = r.json()
        inputRange = pandas.date_range(start_date, end_date, freq='D').strftime('%Y-%m-%d')
    else:
        url = f'https://www.alphavantage.co/query?function={time_series}&symbol=' + stock_symbol + '&outputsize=full&apikey=GIW0WKEDYCA4NMCQ'
        r = requests.get(url)
        data = r.json()
        inputRange = pandas.date_range(start_date, end_date, freq='D').strftime('%Y-%m-%d')

    #dataSeperator calls
    openData = dataSeperator("1. open")
    highData = dataSeperator("2. high")
    lowData = dataSeperator("3. low")
    closeData = dataSeperator("4. close")
    xAxisDate = dateChecker()
    
    if chart_type == 2:
       line_chart = pygal.Line(x_label_rotation=45)
       line_chart.title = 'Stock Data for ' + stock_symbol + ': ' + start_date + ' to ' + end_date
       line_chart.x_labels = xAxisDate
       line_chart.add('Open', openData)
       line_chart.add('High', highData)
       line_chart.add('Low',  lowData)
       line_chart.add('Close', closeData)
       line_chart.render_in_browser()
    else:
       bar_chart = pygal.Bar(x_label_rotation=45)
       bar_chart.title = 'Stock Data for ' + stock_symbol + ': ' + start_date + ' ' + end_date
       bar_chart.x_labels = xAxisDate
       bar_chart.add('Open', openData)
       bar_chart.add('High', highData)
       bar_chart.add('Low',  lowData)
       bar_chart.add('Close', closeData)
       bar_chart.render_in_browser()

    #print(f"Data = {data}")
        
main()
