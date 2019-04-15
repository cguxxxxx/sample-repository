import pandas as pd
import os

outputfile = './../sampleoutputs/DALWDC_AllSuccLogin.csv'
if os.path.exists(outputfile):
    os.remove(outputfile)

inputfile_dir = "./data/dal/"
dal_orgs_excluded = ['503994339-502220653','503994353-502220660','503383882-502757208','tealeaf-com','503180793-501780791','503180793-501780791','503994359-502220663','503994372-502220669','503994374-502220670','20170815093721','501137933-502338157','aurora-com','20160310172727','20160922180442','503557519-502041070','505112566-502822877','503994370-502220668','503881273-502159154','501198785-501849152','503836898-502135413','503994363-502220665','503570692-501991547','503761519-502094499','20170727124237','503994367-502220667','org4']
wdc_orgs_excluded = ['20150929204041','20160919173225','20171207212358','20171207212358','tealeaf-com','20170126125046','20170815093744','506126005-503356889','aurora-com','aurora-com','20141210113514','20151029154517','20160630140440','20160805162806','20161102203713','20150329174936','20150723064912','20150817155051','20160512060102','20180601222316','20150122093446','20150430070330','20160817183230','20150306090400','505677979-503123865','20160809205215','20160826171636','20170130214554','20171016114731','20180227204930','505923716-503251787']

for inputfile in os.listdir(inputfile_dir):
    path = inputfile_dir+inputfile
    df = pd.read_csv(path,skiprows=[0,1],names = ['date','id','ip','org','activity_type','desc'],index_col=False,dtype=str)
    out1 = df[ (df['activity_type'] == 'SuccLogin') & 
        (df['id'].str.find("ibm.com") == -1) &
        (df['id'].str.find("gmail.com") == -1) &
        (~df['org'].isin(dal_orgs_excluded)) & 
        (~df['org'].isin(wdc_orgs_excluded)) ]
    out1.to_csv(outputfile,mode='a', index=False, header=False)
    #ibmcomout = out1[ (out1['org'] == 'ibm-com') ]
    #ibmcomout.to_csv('./../sampleoutputs/DALWDC_AllibmcomSuccLogin.csv',mode='a', index=False, header=False)

rawdf = pd.read_csv(outputfile,skiprows=[0,1],names = ['date','id','ip','org','activity_type','desc'],index_col=False,dtype=str)
rawdf.groupby(['org'])[['activity_type']].count().to_csv('./../sampleoutputs/DALWDC_AllSuccLogincount_byorg.csv')
