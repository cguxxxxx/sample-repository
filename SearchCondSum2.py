import pandas as pd

#path = "./out/AllSearchOut.csv"
path = "./out/DALWDC_AllSearchOut.csv"

df = pd.DataFrame(columns = ["groupOperator","conditionOperator"],dtype=int)

rawdf = pd.read_csv(path,skiprows=[0,1],names = ['date','id','ip','org','activity_type','desc'],index_col=False,dtype=str)

#count groupOperator & conditionOperator
rawdf['groupOperator'] = rawdf.desc.apply(lambda x: x.count('groupOperator'))
rawdf['conditionOperator'] = rawdf.desc.apply(lambda x: x.count('conditionOperator'))
rawdf['operandType'] = rawdf.desc.apply(lambda x: x.count('operandType'))
rawdf.groupby(['operandType'])[['activity_type']].count().to_csv('./out/OperatorTypeCount_dalwdc.csv')
rawdf.groupby(['conditionOperator'])[['activity_type']].count().to_csv('./out/ConditionOperatorCount_dalwdc.csv')
rawdf.groupby(['groupOperator'])[['activity_type']].count().to_csv('./out/groupOperatorCount_dalwdc.csv')