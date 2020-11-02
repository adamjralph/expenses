from datetime import date
import ast

def read_data():

    try:
        with open('expense_data.txt', 'r') as f:
            data = f.read()
        data_dict = ast.literal_eval(data)
        print(data_dict)
        print(type(data_dict))
        return data_dict
    except FileNotFoundError:
        open('expense_data.txt', 'w')
        data_dict = {}
        return data_dict
    except SyntaxError:
        print('Dictionary is empty!')
        data_dict = {}
        print(data_dict)
        print(type(data_dict))
        return data_dict

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
    return date.today().strftime('%Y-%m-%d')

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
