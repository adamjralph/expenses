#import json
#
#with open("expense_data.txt") as f:
#    data = f.read()
#
#print('Data type before reconstruction: ', type(data))
#
#js = json.loads(data)
#
#print('Data type after resonstruction: ', type(js))
#print(js)


# import pickle

# file = open('')


# importing the module 
import ast 
  
# reading the data from the file 
with open('expense_data.txt') as f: 
    data = f.read() 
  
print("Data type before reconstruction : ", type(data)) 
      
# reconstructing the data as a dictionary 
d = ast.literal_eval(data) 
  
print("Data type after reconstruction : ", type(d)) 
print(d) 

#Data type before reconstruction :  <class 'str'>
#Data type after reconstruction :  <class 'dict'>
#{'1': [1, 'fish', '6', 'food', '2020-11-01'], '2': [2, 'goo', '7', 'slop', '2020-11-01']}
