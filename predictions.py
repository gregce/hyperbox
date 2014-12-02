import numpy as np
import pandas as pd
import os
from pandas import DataFrame, Series 
from sklearn import preprocessing
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

##ensure that the directory of the program is always correctly set
os.chdir('/users/ceccarelli/hyperbox')
#print __file__

##read in the csv as a dataframe
df = pd.read_csv("churn.csv")

##convert the dataframe to a numpy array
dataset = np.array(df)

#breakout the data and target variable
x=dataset[:,0:19]
y=dataset[:,20]

model = LogisticRegression()
model.fit(x,y)

