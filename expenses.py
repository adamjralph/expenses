from datetime import date
import ast

def read_data():

    try:
        with open('expense_data.txt', 'r') as f:
            data = f.read()
        data_dict = ast.literal_eval(data)
        return data_dict
    except FileNotFoundError:
        open('expense_data.txt', 'w')
        data_dict = {}
        return data_dict
    except SyntaxError:
        print('Dictionary is empty!')
        data_dict = {}
        return data_dict

def request_data(data):

    show = input('Do you wish to read the current data? y/n? ')
    while True:
        if show.lower() == y:
            return data
        elif show.lower() == n:
            break
        else:
            print('Please enter y/n')

def create_id(data):
    # Do i need the id_num or can I just use max_id as is?
    id_num = 0
    if data:
        max_id = max(k for k, v in data.items())
        id_num = max_id
        return id_num
    else:
        return id_num

def add_item():
        
    while True:
        name = str(input('Please enter item name: '))
        if len(name) > 10:
            print('Item name must not be longer than 10 characters. \nPlease try again.')
        else:
            return name

def add_price():
    
    while True:
        try: 
            price = float(input('Please enter price: '))
            return price
        except:
            print('Please enter a numberical value.')
    

def add_category():
    
    while True:
        category = input('Please enter category: ')
        if len(category) > 10:
            print('Category name must not be longer than 10 characters. \nPlease try again.')
        else: 
            return category

def add_date():
    
    print('Date of purchase.')
    while True:
        choose_date = input("Type 't' for today's date or 'd' to enter date manually. ")
        if choose_date.lower() == 't':
            return date.today().strftime('%Y-%m-%d')
        elif choose_date.lower() == 'd':
            year = date_item('Year', 4, 'four') 
            month = date_item('Month', 2, 'two')
            day = date_item('Day', 2, 'two')
            return f'{year}-{month}-{day}'
        else:
            print("Please enter 't' or 'd'")
            
def date_item(ymd, length, str_len):
    
    while True:
        enter_ymd = input(f'Please enter {ymd}: ')
        try:
            int(enter_ymd)
        except ValueError:
            print(f'Please enter {str_len}  digits only.')
        if len(enter_ymd) != length:
            print(f'{ymd} must be {str_len} digits.')
        else:
            return enter_ymd

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
        if session.lower() == 'q':
            write_dict(data)
            print('Session ended. Goodbye!')
            break
        elif session.lower() == 'e':
            create_entry(data) 
        else:
            print("Please enter 'e' or 'q'")
        
data = read_data()
session_on(data)
