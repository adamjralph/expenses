#
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
    date = input('Please enter date: ')
    return date

data_dict = {}
def create_entry():

    # create a tuple containing data derived from data entry funcions 
    data_dict = {
            'name':add_item(),
            'price':add_price(),
            'category':add_category(),
            'date':add_date()
    }
    print(data_dict)
#    expense = (add_item(), add_price(), add_category(), add_date())
#    return expense 

id_num = 0
while True:
    
    session = input("To enter a new expense please type 'e' or to quit type 'q'")
    if session == 'q':
        break
    else:
        entry = create_entry()      
        id_num += 1



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
