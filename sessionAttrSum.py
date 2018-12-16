import pandas as pd
import numpy as np
import json
import re

#path = "./data/AuditData_20180501000000_20181101235959.csv"
path = "./data/DAL_AuditData_20180501000000_20181130235959.csv"

#rawdf = pd.read_csv(path,header=1)
rawdf = pd.read_csv(path,skiprows=[0,1],names = ['date','id','ip','org','activity_type','desc'],index_col=False)

out1 = rawdf[(rawdf['activity_type'] == 'SessionSearch')]
#out1 = rawdf[(rawdf['Organization'] == '20150714070544')]

#out1.to_csv('outfile_act_filter.csv')

out2 = out1[-out1['org'].isin(['503994339-502220653','503994353-502220660','503383882-502757208','tealeaf-com','503180793-501780791','503180793-501780791',
'503994359-502220663','503994372-502220669','503994374-502220670','20170815093721','501137933-502338157','aurora-com','20160310172727','20160922180442','503557519-502041070','505112566-502822877','503994370-502220668','503881273-502159154','501198785-501849152','503836898-502135413','503994363-502220665','503570692-501991547','503761519-502094499','20170727124237','503994367-502220667','org4'])]
#out2.to_csv('outfile2.csv')

out2['id'] = out2['id'].map(lambda x: "ibm.com" if x.find("ibm.com") > 0 else x )
#out2.to_csv('outfile3.csv')

#filter out ibm.com
out3 = out2[-out2['id'].isin(['ibm.com'])]
#out3.to_csv('search_all_out.csv')

#{operandType:SESSION_ATTRIBUTE,operandValue:SSV_1005}
out3['desc'] = out3['desc'].map(lambda x: x if re.search(r'^.*SESSION_ATTRIBUTE',x) else 'invalid')
out3 = out3[-out3['desc'].isin(['invalid'])]

out3['desc'] = out3['desc'].map(lambda x: re.sub(r'^.*SESSION_ATTRIBUTE,operandValue:', '', x))

out3['desc'] = out3['desc'].map(lambda x: re.sub(r'\}.*$', '', x))
out3.to_csv('./out/Session_attr_type_all.csv',index=False)
out3.groupby(['desc'])[['activity_type']].count().to_csv('./out/Session_attr_type_count.csv')

'''
#operandType:FREE_TEXT,operator:EQUALS,rightOperand:[jmamurphy@yahoo.com]
out3['desc'] = out3['desc'].map(lambda x: x if re.search(r'^.*FREE_TEXT',x) else 'invalid')

out3 = out3[-out3['desc'].isin(['invalid'])]
out3.to_csv('termsoutput1.csv')
#print(out3['desc'].count())

out3['desc'] = out3['desc'].map(lambda x: re.sub(r'^.*FREE_TEXT', '', x))
out3.to_csv('termsoutput2.csv')
out3['desc'] = out3['desc'].map(lambda x: re.sub(r'^.*\[', '', x))
out3['desc'] = out3['desc'].map(lambda x: re.sub(r'\].*$', '', x))
out3.to_csv('termsoutput3.csv',index=False)

out3['desc'] = out3['desc'].map(lambda x: 'email' if re.search(r'^.*@',x) else x)
out3['desc'] = out3['desc'].map(lambda x: 'ip' if re.search(r'\d+\.\d+\.\d+\.\d+',x) else x)
out3['desc'] = out3['desc'].map(lambda x: 'dash' if re.search(r'^.*\-',x) else x) #b5288ce0-861c-11e8-bfb7-03b75d67746c
out3['desc'] = out3['desc'].map(lambda x: 'url' if re.search(r'\\*$',x) else x)
out3['desc'] = out3['desc'].map(lambda x: 'underscore' if re.search(r'^.*_',x) else x)

print("email: ",out3[(out3['desc'] == 'email')].count())
print("url: ",out3[(out3['desc'] == 'url')].count())
print("dash: ",out3[(out3['desc'] == 'dash')].count())
print("underscore: ",out3[(out3['desc'] == 'underscore')].count())

out3 = out3[-out3['desc'].isin(['email','ip','dash','url','underscore'])]
out3.to_csv('termsoutput4.csv',index=False)
'''