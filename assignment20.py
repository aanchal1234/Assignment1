#1 - Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.
import pandas as p
import numpy as np
Details={
'MY DETAILS':['aanchal','20','aanchalbudhiraja2349@gmail.com','8950697812'],
'MY FRIEND DETAILS':['jyoti','21','js1234@gmail.com','7404657889']}
df=p.DataFrame(Details)
print(df)
 #Q.2 - Download the dataset from this link ,
# Click Here
# Import the data and print the following :
# a.) First 5 rows of Dataframe
# b.) First 10 rows of the Dataframe
# c.) find basic statistics on the particular dataset.
# d.) Find the last 5 rows of the dataframe
# e.) Extract the 2nd column and find basic statistics on
import pandas as p
df=p.read_csv("C:/Users/Dell/Downloads/Weather.csv")
print(df)
print(df.head(10))
print(df.describe())
print(df.tail(5))
print(df['MinTemp'].describe())
df=p.DataFrame()
print(df.shape())


