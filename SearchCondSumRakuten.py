import pandas as pd

#startTime=2018-06-01&endTime=2019-03-17&orgCode=20170201202308
path = "./data/RakutenAuditData_20170201202308_20180601000000_20190317235959.csv"
outputfile = "../sampleoutputs/RakutenSearchOut.csv"

df = pd.read_csv(path,skiprows=[0,1],names = ['date','id','ip','activity_type','desc'],index_col=False,dtype=str)
rawdf = df[ (df['activity_type'] == 'SessionSearch') & 
        (df['id'].str.find("ibm.com") == -1) ]


#df = pd.DataFrame(columns = ["groupOperator","conditionOperator"],dtype=int)

#count groupOperator & conditionOperator
#rawdf['groupOperator'] = rawdf.desc.apply(lambda x: x.count('groupOperator'))
rawdf['conditionOperator'] = rawdf.desc.apply(lambda x: x.count('conditionOperator'))

#rawdf['operandType'] = rawdf.desc.apply(lambda x: x.count('operandType'))
rawdf.to_csv(outputfile, index=False, header=False)
#rawdf.groupby(['operandType'])[['activity_type']].count().to_csv('../sampleoutputs/OperatorTypeCount_dalwdc.csv')
rawdf.groupby(['conditionOperator'])[['activity_type']].count().to_csv('../sampleoutputs/ConditionOperatorCount_Rakuten.csv')
#rawdf.groupby(['groupOperator'])[['activity_type']].count().to_csv('./out/groupOperatorCount_dalwdc.csv')