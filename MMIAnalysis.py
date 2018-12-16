import pandas as pd
import numpy as np

path = "./data/MMI_2017 Nov_2018Nov.csv"
#path = "./data/test.csv"
rawdf = pd.read_csv(path,header=None,index_col=False)

i = 0

# remove org lines with Nov MMI = 0
while i<3076 and i<len(rawdf.index)-1:
    if float(rawdf.iloc[i+14,1]) == 0:
        #print(i)
        rawdf = rawdf.drop(rawdf.index[i:i+18])
    else:
        i = i+18

rawdf.to_csv('./out/MMI_exclude 0 MMI.csv',index=False,header=False)