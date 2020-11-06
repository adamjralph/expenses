import pandas as pd
import numpy as np
from expenses import data

df = pd.DataFrame(data, index=['Item:','Price:','Category:','Date:'])
print(df)

