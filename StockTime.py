import requests
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

#This functions asks the user for the time series option and returns the user's input.
def get_user_time_series():
    while True:
        print("Enter the time series option:")
        print("1. Intraday")
        print("2. Daily")
        print("3. Weekly")
        print("4. Monthly")
        time_series_option = input("Option: ")
        if time_series_option not in ["1", "2", "3", "4"]:
            print("Invalid option. Please enter either 1, 2, 3, or 4.")
        else:
            return time_series_option
        
#This function asks the user for the start date and returns the user's input.
def get_user_start_date():
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    return start_date

#This function asks the user for the end date and validates that the end date is not before the start date. It returns the user's input if it is valid.
def get_user_end_date(start_date):
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    try:
        start_timestamp = int(pd.Timestamp(start_date).timestamp())
        end_timestamp = int(pd.Timestamp(end_date).timestamp())
        if end_timestamp < start_timestamp:
            raise ValueError("End date must be after start date.")
    except ValueError as e:
        print("Invalid date input:", e)
        exit(1)
    return end_date
