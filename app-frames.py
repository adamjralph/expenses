# implemnent data analysis using pandas

from expenses import *
import pandas as pd

def check_yn(yn):
    
    while True:
        if yn.lower() == 'y':
            return True  
        elif yn.lower() == 'n':
            return False 
        else:
            yn = input('Please enter y or n. ')
            continue
            

def read_file():

    print('Reading datafile...')
    return pd.read_csv('datafile.csv')
   
def create_dataframe():
    
    print('Creating dataframe...')
    df = read_file()
    return df 

def display_dataframe():

    print('Displaying dataframe...')
    df = create_dataframe()
    return print(df)

def view_data():

    while True:

        yn = input('Do you wish to view the current data? y/n ')
        check = check_yn(yn)
        if check:
            display_dataframe()
            break
        elif check == False:
            print('Okay then.')
        else:
            check = yn
            continue

def choose_data():

    # filters
    df = create_dataframe()
    print('Items ...')
    i = df['Item']
    print(i)
    print('Categories ...')
    c = df['Category']
    print(c)
    print('Food')
    f = (df['Category'] == 'food')
    print(df[f])
    print('Food, fish')
    print(df.loc[f, 'Item'])

    # Totals
    t = df['Price'].sum()
    print(t)
    # Find the price of food

def audit_data_on():

    while True:
                
        view_data()
        choose_data()
        break 


        
audit_data_on()


