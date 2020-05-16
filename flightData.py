import constants
#load pandas libraries
import pandas as pd
colnames = ['timeData', 'altData', 'speedData', 'A0AData']
df = pd.read_csv("flightData.csv", names=['altData','speedData','timeData','A0AData'], usecols=[0,1,2,3],header=None)

def getAlt():
    Alt_Data=[]
    for i in df.iloc[:,1]:
        Alt_Data+=[i]
    return Alt_Data

def getSpeed():
    Speed_Data = []
    for i in df.iloc[:,2]:
        Speed_Data += [i]
    return Speed_Data


def getTime():
    Time_Data = []
    for i in df.iloc[:,0]:
        Time_Data += [i]
    return Time_Data
 
def getAOA():  
    A0A_Data = []
    for i in df.iloc[:,3]:
        A0A_Data += [i]
    return A0A_Data

def getC_pmax():                # NOTE: INCOMPLETE, this needs to be varying with time
    return constants.C_pmax
