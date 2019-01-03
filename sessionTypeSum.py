import pandas as pd
import numpy as np
import json
import re

path = "./out/DALWDC_AllSearchOut.csv"
rawdf = pd.read_csv(path,skiprows=[0,1],names = ['date','id','ip','org','activity_type','desc'],index_col=False,dtype=str)
df1 = rawdf['desc'].str.extractall(r'(?P<operand_type_str>{operandType[\w,\,,\:]*})')  #[] all the possible occurence
df1['operand_type'] = df1['operand_type_str'].str.extract(r'{operandType:(\w*)')  #() Regular expression pattern with capturing groups
df1['operand_type_str'] = df1['operand_type_str'].str.extract(r'{([\w\,\:]*)}')
#df1['operand_type'] = df1['operand_type_str'].apply(lambda x: re.sub(r'{operandType\:', '', x))
#df1['operand_type'] = df1['operand_type'].apply(lambda x: re.sub(r'[},].*$', '', x))
df1.to_csv('./out/DALWDC_AllSearchOperandTypes.csv',index=False)
df1.groupby(['operand_type'])[['operand_type']].count().to_csv('./out/DALWDC_searchcount_bytype.csv')

'''
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