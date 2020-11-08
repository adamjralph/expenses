import pandas as pd
#import numpy as np
from datetime import date
import csv

def read_data():

    try:
        open_data = open('datafile.csv', 'r')
        data_csv = csv.reader(open_data) 
        read_lines = list(data_csv)
        open_data.close()
        return read_lines
    except FileNotFoundError:
        open('datafile.csv', 'w')
        #data_csv = []
        return data_csv
    except SyntaxError:
        print('File is empty!')
        #data_csv = [] 
        return data_csv

def request_data(data):

    data = read_data()
    while True:
        show = input('Do you wish to read the current data? y/n? ')
        if show.lower() == 'y':
            show_data = pd_data(data)
            return print(show_data)
        elif show.lower() == 'n':
            break
        else:
            print('Please enter y/n')

def create_id(data):
    # Do i need the id_num or can I just use max_id as is?
    id_num = 0
    length = len(data)
    id_list = []
    if length >= 2:
        for line in data:
            num = line[0]
            id_list.append(num)
            id_list[0] = 0
        for item in id_list:
            list_num = int(item)
            if list_num > id_num:
                id_num = list_num 
            else:
                continue
        return id_num + 1
    else:
        return id_num + 1

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

    if len(data) <= 1:
        new_id = 1
    else:
        new_id = create_id(data)
    entry_list = [new_id, add_item(), add_price(), add_category(), add_date()]
    write_file(entry_list)

def write_file(entry_list):

    data = read_data()
    if len(data) == 0:
        file_to_write = open('datafile.csv','w',newline='')
        csv_writer = csv.writer(file_to_write,delimiter=',')
        csv_writer.writerow(['Id','Item','Price','Category','Date'])
        csv_writer.writerows([entry_list])
        file_to_write.close() 
    else:
        file_to_write = open('datafile.csv','a',newline='')
        csv_writer = csv.writer(file_to_write)
        csv_writer.writerows([entry_list])
        file_to_write.close()

def session_on(data):

    while True:
        session = input("To enter a new expense please type 'e' or to quit type 'q': ")
        if session.lower() == 'q':
            request_data(data)
            print('Session ended. Goodbye!')
            break
        elif session.lower() == 'e':
            data = read_data()
            create_entry(data)
        else:
            print("Please enter 'e' or 'q'")

def pd_data(data):

    df = pd.DataFrame(data)
    return df

data = read_data()
request_data(data)       
session_on(data)



