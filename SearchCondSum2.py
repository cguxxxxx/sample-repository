import pandas as pd

#path = "./out/AllSearchOut.csv"
path = "./out/WDC_AllSearchOut.csv"

df = pd.DataFrame(columns = ["groupOperator","conditionOperator"],dtype=int)

rawdf = pd.read_csv(path,skiprows=[0,1],names = ['date','id','ip','org','activity_type','desc'],index_col=False,dtype=str)

#count groupOperator & conditionOperator
rawdf['groupOperator'] = rawdf.desc.apply(lambda x: x.count('groupOperator'))
rawdf['conditionOperator'] = rawdf.desc.apply(lambda x: x.count('conditionOperator'))
rawdf['operandType'] = rawdf.desc.apply(lambda x: x.count('operandType'))
rawdf.to_csv('./out/OperatorCount_wdc.csv',index=False)
'''
i = 0
print(len(rawdf))

while i < len(rawdf):
    str = rawdf.iloc[i,5]
    df.loc[i] = [str.count('groupOperator'),str.count('conditionOperator')]
    i = i+1
    print(i)

df.to_csv('./out/OperatorCount.csv',index=False)
'''

