
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
def create_entry(id_num):

    # create a dictionary of lists
    entry_list = [id_num, add_item(), add_price(), add_category(), add_date()]
    data_dict[id_num] = entry_list
    data_file = open('expense_data.txt', 'a')
    data_file.write(str(data_dict)+'\n')
    print(data_dict)
    data_file.close()
#    expense = (add_item(), add_price(), add_category(), add_date())
#    return expense 

def session_on():
    
    id_num = 0
    while True:
        session = input("To enter a new expense please type 'e' or to quit type 'q': ")
        if session == 'q':
            break
        else:
            entry = create_entry(id_num)      
            id_num += 1

session_on()

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
