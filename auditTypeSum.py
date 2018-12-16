import pandas as pd
import numpy as np
import json
import re

#path = "./AuditData_20180501000000_20181101235959.csv"
path = "./data/DAL_AuditData_20180501000000_20181130235959.csv"
#path = "./WDC AuditData_20180101000000_20181101235959.csv"

#rawdf = pd.read_csv(path,header=1)
rawdf = pd.read_csv(path,skiprows=[0,1],names = ['date','id','ip','org','activity_type','desc'],index_col=False,dtype=str)

#DAL orgs to filter out
out1 = rawdf[-rawdf['org'].isin(['503994339-502220653','503994353-502220660','503383882-502757208','tealeaf-com','503180793-501780791','503180793-501780791','503994359-502220663','503994372-502220669','503994374-502220670','20170815093721','501137933-502338157','aurora-com','20160310172727','20160922180442','503557519-502041070','505112566-502822877','503994370-502220668','503881273-502159154','501198785-501849152','503836898-502135413','503994363-502220665','503570692-501991547','503761519-502094499','20170727124237','503994367-502220667','org4'])]

#filter out ibm.com
out1['id'] = out1['id'].map(lambda x: "ibm.com" if x.find("ibm.com") > 0 else x )
out2 = out1[-out1['id'].isin(['ibm.com'])]

out2.groupby(['activity_type'])[['activity_type']].count().to_csv('./out/audit_type_grandtotal.csv')