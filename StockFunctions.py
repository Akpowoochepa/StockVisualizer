#function to get stock symbol from user as user input
def get_stock_symbol():
    stock_symbol = input("Enter the stock symbol you are looking for: ")
    return stock_symbol

#function to get chart type from user as user input
def get_chart_type():
    chart_type = input("Enter the chart type you want (1,2): ")
    return 