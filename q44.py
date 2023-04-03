import pandas as pd 
import random
 
 
lst = ['robot'] * 2
lst += ['human'] * 2
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data, "\n")
 

data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value = 0).astype(int)
data.columns = data.columns.droplevel()
data.columns.name = None
print(data)