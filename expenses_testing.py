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
#    name = input('Please enter item name: ')
#    return name
    return 'Apple'

def add_price():
#    price = input('Please enter price: ')
#    return price
    return 10

def add_category():
#    category = input('Please enter category: ')
#    return category
    return 'Fruit'
    
def add_date():
#    date = input('Please enter date: ')
#    return date
    return '12/10/20'    
    
def create_entry():

#class CreateEntry():
#    
#    def __init__(self, item, price, category, date):
#
#        self.item = add_item()
#        self.price = add_price()
#        self.category = add_category()
#        self.date = add_date()
#
#item = CreateEntry.item()
#print(item)
class Expense():

    def __init__(self, entry):

        self.entry = entry

    def print_item(self, entry):

        return print(self.entry)

new_item = Expense(create_entry())
print(new_item.print_item)
#

        
        
create_entry()


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
