import pandas as pd
import numpy as np
import pdb
import matplotlib.pyplot as plt
from pandas import DataFrame, read_csv

N = 50
t = arange(N)                  # sampling times
dw = np.random.randn(N)        # Wiener increments   
x = np.cumsum(dw)              # Brownian path    
plot(t, x)
xlabel('t')
ylabel('x')

#Opening a datafile to store the data:
f = open('data_new.txt', 'wb')
# Writing the numerical data as a string:
f.write(str(x))
f.write(str(t))
'''
Writing the output into the file: str() converts to string:
'''
f.close()#Closing the file:
data = pd.read_csv('data_new.txt')
'''
Read csv is to create dataframes with numbered rows:
'''
data # 
'''
I am loading the data directly to dataframe:
'''
df =  DataFrame({'x' : np.cumsum(dw),'t' :arange(N)})
df # print the data as a dataframe
