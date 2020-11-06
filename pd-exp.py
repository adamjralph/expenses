import pandas as pd
import numpy as np
from expenses import data 

# imported_data = read_data()
df = pd.DataFrame(data, index=['Item:','Price:','Category:','Date:'])
print(df)

