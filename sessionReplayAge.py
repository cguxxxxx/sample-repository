import pandas as pd
import numpy as np
import json
import re
from pandas import to_datetime
import datetime

path = "./data/AA_AuditData_20160615205804_20181021000000_20190121235959.csv"
rawdf = pd.read_csv(path,skiprows=[0,1],names = ['date','id','ip','activity_type','desc'],index_col=False,dtype=str)

#filter out ids with ibm.com
rawdf['id_surfix'] = rawdf.id.apply(lambda x: "ibm.com" if x.find("ibm.com") > 0 else x )
df1 = rawdf[-rawdf['id_surfix'].isin(['ibm.com'])]
df1.to_csv("./out/AA_3month_All.csv",index=False)

df0 = df1[(df1['activity_type'] == 'SessionReplay')]
df0.to_csv("./out/AA_3month_AllSessionReplay.csv",index=False)

df0['invalid'] = df0['desc'].apply(lambda x: 1 if re.match(r'^[\w,\W]*\_',x) == None else 0 )
df2= df0.loc[(df0['invalid'] == 0)] 

# Session id: 30412625532929289771671019218702_20190121123534,
df2['tmpstr'] = df2['desc'].apply(lambda x: re.sub(r'^[\w,\W]*\_', '', x))
df2['tmpstr2'] = df2['tmpstr'].apply(lambda x: re.sub(r'\,[\w,\W]*$', '', x))
df2['sessiondate'] = df2['tmpstr2'].apply(lambda x: re.sub(r'\d\d\d\d\d\d$', '', x))
df2.to_csv("./out/AA_3month_tmpSessionReplay.csv",index=False)
df2['dateparsed']=to_datetime(df2.date,format="%d %b %Y %I:%M %p")
df2['sessiondatepassed']=to_datetime(df2.sessiondate,format="%Y%m%d")
df2['sessionage'] = df2.dateparsed-df2.sessiondatepassed
df2['sessionretentionday28'] = df2['sessionage'].apply(lambda x: 1 if x <= datetime.timedelta(days=28) else 0)
df2['sessionretentionday21'] = df2['sessionage'].apply(lambda x: 1 if x <=datetime.timedelta(days=21) else 0)
df2['sessionretentionday14'] = df2['sessionage'].apply(lambda x: 1 if x <=datetime.timedelta(days=14) else 0)

#df2['sessionage'] = df2.date-df2.sessiondate
df2.to_csv("./out/AA_3month_SessionReplayAge.csv",index=False)

'''
df1 = rawdf['desc'].str.extractall(r'(?P<operand_type_str>{operandType[\w,\,,\:]*})')  #[] all the possible occurence
df1['operand_type'] = df1['operand_type_str'].str.extract(r'{operandType:(\w*)')  #() Regular expression pattern with capturing groups
df1['operand_type_str'] = df1['operand_type_str'].str.extract(r'{([\w\,\:]*)}')
#df1['operand_type'] = df1['operand_type_str'].apply(lambda x: re.sub(r'{operandType\:', '', x))
#df1['operand_type'] = df1['operand_type'].apply(lambda x: re.sub(r'[},].*$', '', x))
df1.to_csv('./out/DALWDC_AllSearchOperandTypes.csv',index=False)
df1.groupby(['operand_type'])[['operand_type']].count().to_csv('./out/DALWDC_searchcount_bytype.csv')

{application:8887ca317bdb419a89bf516491744a59,
dateAfter:2018-11-18T00:00:00,dateBefore:2018-11-21T00:00:00,
groupOperator:AND,conditionGroups:[
    {isNot:false,
    conditionOperator:AND,
    conditions:[
        {leftOperand:{operandType:SESSION_ATTRIBUTE,operandValue:SSV_LOGIN_ID},
        operator:EQUALS,
        rightOperand:[Muffy2016],excluded:false}
        ]
    }
]}
{dateAfter:2018-11-28T11:03:42,dateBefore:2018-11-30T11:03:42,
groupOperator:AND,conditionGroups:[
    {isNot:false,
    conditionOperator:AND,
    conditions:[
        {leftOperand:{operandType:FREE_TEXT},
        operator:EQUALS,
        rightOperand:[napoli],excluded:false}]}]}
'''