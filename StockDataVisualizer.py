import requests
import pygal
from lxml import etree, html
from StockFunctions import *
from StockTime import *

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



    # STOCK VISUALIZATION
    # Get stock data from API
    api_key = 'AFWROUKTO2W1ZDY'
    url = f'https://www.alphavantage.co/query?function={time_series}&symbol={stock_symbol}&interval={interval}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()

    # Extract data for line chart
    line_dates = []
    line_prices = []
    line_open_prices = []
    line_high_prices = []
    line_low_prices = []
    line_close_prices = []
    for date, prices in data[f'Time Series ({interval or "daily"})'].items():
        line_dates.append(date)
        line_prices.append(float(prices['4. close']))
        line_open_prices.append(float(prices['1. open']))
        line_high_prices.append(float(prices['2. high']))
        line_low_prices.append(float(prices['3. low']))
        line_close_prices.append(float(prices['4. close']))

    # Extract data for bar chart
    bar_dates = []
    bar_volumes = []
    for date, volumes in data[f'Time Series ({interval or "daily"})'].items():
        bar_dates.append(date)
        bar_volumes.append(int(volumes['5. volume']))

    # Create line chart
    line_chart = pygal.Line(x_label_rotation=20)
    line_chart.title = f'{stock_symbol} Stock Prices'
    line_chart.x_labels = line_dates
    line_chart.add('Price', line_prices)
    line_chart.add('Open', line_open_prices)
    line_chart.add('High', line_high_prices)
    line_chart.add('Low', line_low_prices)
    line_chart.add('Close', line_close_prices)

    # Create bar chart
    bar_chart = pygal.Bar(x_label_rotation=20)
    bar_chart.title = f'{stock_symbol} Stock Volume'
    bar_chart.x_labels = bar_dates
    bar_chart.add('Volume', bar_volumes)

    # Render charts to SVG files
    line_chart.render_to_file('line_chart.svg')
    bar_chart.render_to_file('bar_chart.svg')

# Generate HTML page with embedded charts
    html_element = etree.Element('html')
    head = etree.SubElement(html_element, 'head')
    title = etree.SubElement(head, 'title')
    title.text = 'Stock Charts'
    body = etree.SubElement(html_element, 'body')

    if chart_type == '1':
        with open('bar_chart.svg', 'r') as f:
            bar_svg_data = f.read()
        bar_svg = etree.fromstring(bar_svg_data.encode())
        body.append(bar_svg)

    elif chart_type == '2':
        with open('line_chart.svg', 'r') as f:
            line_svg_data = f.read()
        line_svg = etree.fromstring(line_svg_data.encode())
        body.append(line_svg)

    else:
        # Throw error
        print("Invalid chart type selected.")

    # Output HTML
    with open('stock_charts.html', 'wb') as f:
        f.write(html.tostring(html_element, pretty_print=True))

    # Open HTML file in browser
    html.open_in_browser(html_element)

main()
