from pandas import Series, DataFrame
import pandas as pd
import re
from pandas import to_datetime
import datetime

# regular expression grouping
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))  #010-12345
print(m.group(1))   #010
print(m.group(2))   #12345

# df replace with regular expression
df = DataFrame([['22 Jan 2019 4:25 PM',
    'adriane.nichols@aa.com',
    '144.9.56.131',
    'SessionReplay',
    'Session id: 30412625532929289771671019218702_20190121123534, Application: www.aa.com']],
    columns=['date','id','ip','activity_type','desc'])
df2 = df.replace({ 'desc': r'^.*\_(\d{8}).*$'}, { 'desc' : r'\1'} ,regex=True)   #20190121 8 digits date
print(df2) 

# timedelta col desc - col date
df2['dateparsed']=to_datetime(df2.date,format="%d %b %Y %I:%M %p")
df2['sessiondatepassed']=to_datetime(df2.desc,format="%Y%m%d")
df2['sessionage'] = df2.dateparsed-df2.sessiondatepassed
print(df2['sessionage'])
df2['sessionretentionday28'] = df2['sessionage'].apply(lambda x: 1 if x <= datetime.timedelta(days=28) else 0)
df2['sessionretentionday21'] = df2['sessionage'].apply(lambda x: 1 if x <=datetime.timedelta(days=21) else 0)
df2['sessionretentionday14'] = df2['sessionage'].apply(lambda x: 1 if x <=datetime.timedelta(days=1) else 0)
print(df2)
