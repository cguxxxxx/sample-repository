import pandas as pd
import numpy as np
from asn1crypto._ffi import null
from azure.mgmt.datafactory.operations import datasets_operations

path = "./out/MMI_exclude 0 MMI.csv"
#path = "./data/test.csv"
rawdf = pd.read_csv(path,header=None,index_col=False)

row = 0
df = pd.DataFrame(columns = ["201711", "201712","201712chg", "201801","201801chg", "201802", "201802chg", "201803", "201803chg", "201804","201804chg", "201805", "201805chg", "201806", "201806chg", "201807", "201807chg", "201808", "201808chg", "201809", "201809chg", "201810", "201810chg", "201811", "201811chg", "orgcode"])

while row < 1273: 
    i = row
    dic = {}    #initialization of a Dic
    dic["orgcode"] = rawdf.iloc[i,0]
    if float(rawdf.iloc[i+2,1]) >=1:
        dic["201711"] = rawdf.iloc[i+2,1]
    while i<row+12:
        if float(rawdf.iloc[i+2,1]) >= 1:
            dic[rawdf.iloc[i+3,0]] = rawdf.iloc[i+3,1]
            dic[rawdf.iloc[i+3,0]+"chg"] = (float(rawdf.iloc[i+3,1]) - float(rawdf.iloc[i+2,1]))/float(rawdf.iloc[i+2,1])
        i = i+1   
    dataToAdd = pd.DataFrame([dic]) #construct a Data frame from Dic
    
    data = df.append(dic, sort=False, ignore_index=True)  #append Dic to a Dataframe
    df = data
    
    row = row +18

data.to_csv('./out/MMI change.csv',index=False)