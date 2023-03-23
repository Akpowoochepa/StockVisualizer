# import functions for the Stock Data Visualizer
from StockFunctions import *
from StockVisualizer.StockVisualizer.StockTime import *

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

    # Call the function to plot the stock data
    plot_stock_data(stock_symbol, time_series, interval, start_date, 
end_date, chart_type)


# def visualization():
#     line_chart = pygal.Line()
#     line_chart.title = 'Browser usage evolution (in %)'
#     line_chart.x_labels = map(str, range(2002, 2013))
#     line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
#     line_chart.render()

main()

