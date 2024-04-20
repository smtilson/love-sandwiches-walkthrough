# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    """
    Get sales figures input from user
    """
    while True:
        print("Please enter sales data for the last market")
        print("Sales data should be six numbers, separated by commas")
        print("Example: 10, 20, 30 ,40, 50, 60 \n")
    
        data_str = input("Enter your data here: ")
        print(f"The user provided: {data_str}")
    
        sales_data = data_str.split(",")
        if validate_data(sales_data):
            print("Data is valid")
            break
    return sales_data

def validate_data(values):
    """
    Inside try block, converts values to ints.
    Raises ValueError if strings can not be converted into ints, or if there are not exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please submit proper data\n")
        return False
    return True

def calculate_surplus(sales_row):
    """
    Compare sales with stock and calculate surplus as:
    stock - sales
    """
    print("Calculating surplus\n")
    stock = SHEET.worksheet('stock').get_all_values()
    stock_row = stock[-1]
    surplus_row = [int(stock_val)-sale_val for stock_val,sale_val in zip(stock_row,sales_row)]
    return surplus_row

def update_worksheet(row, worksheet):
    """
    Append row to end of worksheet specified.
    """
    print(f"Updating {worksheet} worksheet")
    target_worksheet = SHEET.worksheet(worksheet)
    target_worksheet.append_row(row)
    print(f'{worksheet} worksheet updated\n')

def main():
    """
    Run main program loop
    """
    data = get_sales_data()
    sales_data = [int(val) for val in data]
    update_worksheet(sales_data, 'sales')
    surplus_row = calculate_surplus(sales_data)
    update_worksheet(surplus_row, 'surplus')

if __name__ == "__main__":
    print("Welcome to Love Sandwiches data automation")
    main()