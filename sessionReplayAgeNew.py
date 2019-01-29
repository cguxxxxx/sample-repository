import pandas as pd
import numpy as np
import json
import re
from pandas import to_datetime
import datetime

path = "./data/AA_AuditData_20160615205804_20181021000000_20190121235959.csv"
df = pd.read_csv(path,skiprows=[0,1],names = ['date','id','ip','activity_type','desc'],index_col=False,dtype=str)

#filter out ids with ibm.com
df1 = df.loc[ (df['id'].str.find("ibm.com") == -1) 
    & ( df['activity_type'] == 'SessionReplay' )
    & ( df['desc'].str.match(r'^[\w,\W]*\_') )
    ]
#print(df1.count())
# Session id: 30412625532929289771671019218702_20190121123534,
df2 = df1.replace({ 'desc': r'^.*\_(\d{8}).*$'}, { 'desc' : r'\1'} ,regex=True) #20190121 8 digits date
#df2.to_csv("./out/AA_3month_tmpSessionReplay.csv",index=False)

df2['dateparsed']=to_datetime(df2.date,format="%d %b %Y %I:%M %p")
df2['sessiondatepassed']=to_datetime(df2.desc,format="%Y%m%d")
df2['sessionage'] = df2.dateparsed-df2.sessiondatepassed
df2['sessionretentionday28'] = df2['sessionage'].apply(lambda x: 1 if x <= datetime.timedelta(days=28) else 0)
df2['sessionretentionday21'] = df2['sessionage'].apply(lambda x: 1 if x <=datetime.timedelta(days=21) else 0)
df2['sessionretentionday14'] = df2['sessionage'].apply(lambda x: 1 if x <=datetime.timedelta(days=14) else 0)

#df2['sessionage'] = df2.date-df2.sessiondate
df2.to_csv("./out/AA_3month_SessionReplayAge.csv",index=False)