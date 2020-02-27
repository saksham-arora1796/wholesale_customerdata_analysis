##Final Project - AIT 664


##Importing the libraries and Dependencies
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from pandas import read_csv
import os

##Work directory setup
os.getcwd()
os.chdir('E:\GMU SEM 2\AIT 664\AIT - 664 Final Project')
os.getcwd()

##File reading using pandas
data = pd.read_csv("Wholesale customers data - Tableau.csv")

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

##Calculation of the number of missing values in the dataset
print("Number of null values in each column")                                   
print(data.isnull().sum())                                                                                              

##Inserting NA in the missing value space.
data.fillna("NA", inplace=True)                                                                                        

##Conversion of the data type of the columns from string to numeric and filling
##in all the NA values with the mean value of that the column. Conversion
##of certain columns to different data types as well.
print(data)
print(data.dtypes)

data["Channel"] = data["Channel"].apply(str)
data["Region"] = data["Region"].apply(str)
data["YEAR"] = data["YEAR"].apply(str)

data["Fresh"] = pd.to_numeric(data["Fresh"], errors='coerce')                              
data["Fresh"] = data["Fresh"].fillna(int(data["Fresh"].mean()), downcast='infer').astype(int)

data["Grocery"] = pd.to_numeric(data["Grocery"], errors='coerce')                              
data["Grocery"] = data["Grocery"].fillna(int(data["Grocery"].mean()), downcast='infer').astype(int)

data["Detergents_Paper"] = pd.to_numeric(data["Detergents_Paper"], errors='coerce')                              
data["Detergents_Paper"] = data["Detergents_Paper"].fillna(int(data["Detergents_Paper"].mean()), downcast='infer').astype(int)

####Printing the data types of the column to verify if the data type has been converted
##successfully.
print(data.dtypes)

####Check to verify if all the missing values have been filled up.
##print("After replacing null values with the mean value of each column")                 
##print(data.isnull().sum())
##
####Printing of the statistics of the data set
summary = data.describe()       
print("Summary Statistics")
print(summary)

##
####Redirecting the clean data set to a csv file.
data.to_csv('output.csv', index=False, encoding='utf-8')    
##
####Year vs Milk
##plt.scatter(data['YEAR'],data['Milk'], color='green', marker='*')                                          
##plt.title('Year versus Milk', color='red')
##plt.xlim(0,50)
##plt.xticks(rotation=90)
##plt.xlabel('Year', color='blue')
##plt.ylabel('Milk', color='blue')


plt.bar(data['LOCATION'],data['Detergents_Paper'].sort_values(ascending=False), width = 1/1.5, color="green")
plt.title('Location wise amount spent on Detergents_Paper', color='red')
plt.xlabel('Location', color='blue')
plt.ylabel('Amount spent on Detergents_Paper', color='blue')
plt.show()

plt.bar(data['YEAR'],data['Milk'].sort_values(ascending=False), width = 1/1.5, color="Brown")
plt.title('Year wise amount spent on Milk', color='blue')
plt.xlabel('Year', color='blue')
plt.xticks(rotation=90)
plt.ylabel('Amount spent on Milk', color='blue')
plt.show()

