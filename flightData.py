#load pandas libraries
import pandas as pd
colnames = ['altData', 'speedData', 'timeData']
df = pd.read_csv("flightData.csv", names=['altData','speedData','timeData'], usecols=[0,1,2],header=None)

def getAlt():
    Alt_Data=[]
    for i in df.iloc[:,0]:
        Alt_Data+=[i]
    return Alt_Data

def getSpeed():
    Speed_Data = []
    for i in df.iloc[:,1]:
        Speed_Data += [i]
    return Speed_Data


def getTime():
    Time_Data = []
    for i in df.iloc[:,2]:
        Time_Data += [i]
    return Time_Data
 

