
# A program which enable the user to enter data to track expenses
#
# An expense includes the following properties
#
# - Name
# - Price
# - Quantity
# - Category
# - Date
#
# The program is able to search the expenses and return various information
# such as:
#
# - Total expenses in a given time period
# - Total expenses for a given category
# -
#
# The program is able to exept an income and set a budget
# based on total expenditure or by seting goals in particular categories
from datetime import date
import ast

def create_id(data_dict):
    id_num = 0
    if data_dict:
        max_id = max(k for k, v in data_dict.items())
        print(max_id)
        id_num = max_id
        return id_num
    else:
        return id_num

def add_item():
    name = input('Please enter item name: ')
    return name

def add_price():
    price = input('Please enter price: ')
    return price

def add_category():
    category = input('Please enter category: ')
    return category

def add_date():
    return date.today().strftime('%Y-%m-%d')

data_dict = {}

def read_data(file_written):

    if file_written == True:
        with open('expense_data.txt', 'r') as f:
            data = f.read()
        data_dict = ast.literal_eval(data)
        print(data_dict)
        print(type(data_dict))
        return data_dict
    else:
        print('Empty')

def create_entry(create_id, data_dict):
    
    new_id = create_id(data_dict)
    entry_list = [add_item(), add_price(), add_category(), add_date()]
    data_dict[new_id + 1] = entry_list
    
file_written = False
def write_dict(data_dict):

    data_file = open('expense_data.txt', 'a')
    data_file.write(str(data_dict))
    file_written = True
    print('Data written to file.')
    data_file.close()
    return file_written

        

def session_on(create_id, data_dict):

    new_id = create_id(data_dict)
    while True:

        session = input("To enter a new expense please type 'e' or to quit type 'q': ")
        if session == 'q':
            write_dict(data_dict)
            print('Session ended. Goodbye!')
            break
        else:
            create_entry(create_id, data_dict)
            #create_id(data_dict)
            read_data(file_written)
read_data(file_written)
session_on(create_id, data_dict)

# def store_date(create):







#class Expense:
#
#    def __init__(self, name, price, category, date):
#
#        self.name = name
#        self.price = price
#        self.category = category
#        self.date = date
#
#    def new():
#
#        name = input('Please enter item name: ')
#        price = input('Please enter price: ')
#        category = input('Please enter category: ')
#        date = input('Please enter date: ')
#
#    def __str__(self):
#
#        print(f'Item: {self.name}\nDebit: {self.price}\nCategory: {self.category}\nDate: {self.date}')
#
## item1 = Expense('Electricity', '100', 'Bill', '01/01/2020')
#
## print(item1)
## new_item = Expense()
#
#expense1 = Expense.new()
#
#print(expense1)
