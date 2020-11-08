import pandas as pd
#import numpy as np
from expenses import read_data 

imported_data = read_data()
#df = pd.DataFrame(data, index=['Item:','Price:','Category:','Date:'])
df = pd.DataFrame(imported_data)
# df.set_index('Id', inplace=True)
print(df)

