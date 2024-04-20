# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")


def get_sales_data():
    """Get sales figures input from user"""
    print("Please enter sales data for the last market")
    print("Sales data should be six numbers, separated by commas")
    print("Example: 10, 20, 30 ,40, 50, 60 \n")
    
    data_str = input("Enter your data here: ")
    print(f"The user provided: {data_str}")
    
    sales_data = data_str.split(",")
    validate_data(sales_data)


def validate_data(values):
    """
    Inside try block, converts values to ints.
    Raises ValueError if strings can not be converted into ints, or if there are not exactly 6 values.
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}.w")
    except ValueError as e:
        print(f"Invalid data: {e}, please submit proper data\n")


get_sales_data()
