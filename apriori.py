

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pylab as plt
import apriori

accident_data=pd.read_csv("accidents.csv")
accident_data.dtypes
print accident_data.head()

# the current data-set isn't in transactional format. To convert it into a transactional data-set, we use the following snippet of code:
basket_str=""

for rowNum, row in accident_data.iterrows():
    
    #Break lines
    if (rowNum != 0):
        basket_str = basket_str + "\n"
    #Add the rowid as the first column
    basket_str = basket_str + str(rowNum) 
    #Add columns
    for colName, col in row.iteritems():
           if ( colName != 'Accident_Index'):
               basket_str = basket_str + "," + colName + "=" + str(col)
#print basket_str
basket_file=open("accidents_basket.csv","w")
basket_file.write(basket_str)
basket_file.close()

import csv
with open("accidents_basket.csv","rb") as f:
    reader=csv.reader(f)
    my_list=list(reader)

#my_list
L,supportData=apriori.apriori(my_list,0.6)
f_rules= apriori.generateRules(L,supportData,0.6)

for row in f_rules:
    print list(row[0]), " => ", list(row[1]), row[2]   
    