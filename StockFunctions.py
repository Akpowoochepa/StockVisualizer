#Functions to get stock information from user

#function to get stock symbol from user as user input
def get_stock_symbol():
    stock_symbol = input("Enter the stock symbol you are looking for: ")
    return stock_symbol

#function to get chart type from user as user input
def get_chart_type():
    i = True
    while i is True:
        try:
            chart_type = int(input("Enter the chart type you want (1,2): "))
            i = False
        except ValueError:
            print('Please enter an integer')
            i = True
        if chart_type <= 0 or chart_type > 2:
            print("Please choose option 1 or 2")
            i = True
        
    return chart_type