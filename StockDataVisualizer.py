#import functions for the Stock Data Visualizer
from StockFunctions import *

def main():
    print("Stock Data Visualizer\n------------------------\n")
    stock_symbol = get_stock_symbol() #function to get the stock symbol from user
    print("\n\nChart Types\n--------------\n1. Bar\n2. Line\n")
    chart_type = get_chart_type() #function to get chart type from user

main()