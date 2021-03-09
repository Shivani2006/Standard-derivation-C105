import pandas as pd 
import plotly.express as px
import math 

df=pd.read_csv("project1.csv")

def average(data):

    total=0

    for h in data:
        total=total+h 

    mean=total/len(data)
    return mean

mean=average(df["Numbers"].tolist())
print(mean)


squaredList=[]
data=df["Numbers"].tolist()
for d in data:
    a=int(d)-mean
    a=a**2
    squaredList.append(a)

sum=0
for d in squaredList:
    sum=sum+d  

dividing=sum/len(data)

std_devaiation=math.sqrt(dividing)
print(std_devaiation)
