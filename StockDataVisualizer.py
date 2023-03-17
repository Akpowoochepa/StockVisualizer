#import functions for the Stock Data Visualizer
from StockFunctions import *

def main():
    print("Stock Data Visualizer\n------------------------\n")
    stock_symbol = get_stock_symbol() #function to get the stock symbol from user
    print("\n\nChart Types\n--------------\n1. Bar\n2. Line\n")
    chart_type = get_chart_type() #function to get chart type from user

# Call the function to get the time series option from the user
time_series_option = get_time_series_option()

# Call the function to get the start date from the user
start_date = get_start_date()

# Call the function to get the end date from the user
end_date = get_end_date(start_date)

main()
