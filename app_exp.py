# Create a new version of the expenses app using oop and SQL
import numpy as np
import pandas as pd
#class Error:
#
#    def __init__(self, check_number):
#
#        self.check_number = check_number
#
#    def check_number(self, num):
#
#        while True:
#            if num == int(num)
#                return num
#            else:
#                print('Please enter a number.')
#                continue


class Entry():

#    def __init__(self, id_num, item, price, category, date):
#        
#        self.id_num = id_num
#        self.item = item
#        self.price = price
#        self.category = category
#        self.date = date
        
    def get_id(self):

        id_num = 1 
        return id_num

    def create_item(self):

        item = input('Please enter item name: ')
        return item

    def create_price(self):

        price = input('Please enter a price: ')
        return price 

    def create_category(self):
        
        category = input('Please enter a category: ')
        return category

    def create_date(self):

        date = input('Please enter the transaction date: ')
        return date

    def __str__(self):

        return f"""
item: {item}
price: {price}
category: {category}
date: {date}""" 
    

new_item = Entry()
item = new_item.create_item()
price = new_item.create_price()
category = new_item.create_category()
date = new_item.create_date()
labels = ['Item', 'Price', 'Category', 'Date']
my_data = [item, price, category, date]
arr = np.array(my_data)
d = {'Item':item, 'Price':price, 'Category':category, 'Date':date}
df = pd.DataFrame(data=my_data, index=labels)
print(df)
