from datetime import date
import ast

def create_id(data):
    id_num = 0
    if data:
        max_id = max(k for k, v in data.items())
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

# data_dict = {}

def read_data():

    try:
        with open('expense_data.txt', 'r') as f:
            data = f.read()
        data_dict = ast.literal_eval(data)
        print(data_dict)
        print(type(data_dict))
        return data_dict
    except SyntaxError:
        print('Dictionary is empty!')
        data_dict = {}
        print(data_dict)
        print(type(data_dict))
        return data_dict

def create_entry(data):
    
    new_id = create_id(data)
    entry_list = [add_item(), add_price(), add_category(), add_date()]
    data[new_id + 1] = entry_list
    
def write_dict(data_dict):

    data_file = open('expense_data.txt', 'w')
    data_file.write(str(data_dict))
    print('Data written to file.')
    data_file.close()

def session_on(data):
    
    while True:

        session = input("To enter a new expense please type 'e' or to quit type 'q': ")
        if session == 'q':
            write_dict(data)
            print('Session ended. Goodbye!')
            break
        else:
            create_entry(data)

data = read_data()
session_on(data)

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
