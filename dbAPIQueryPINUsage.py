import pandas as pd
import ibm_db
import ibm_db_dbi
import time
import os
import traceback

def queryDatatoCSV(hostname,user,passwd,filename,org_excluded=None):
    conn = ibm_db.connect("DATABASE=TLSAAS;HOSTNAME="+hostname+";PORT=50000;PROTOCOL=TCPIP;UID="+user+";PWD="+passwd+";", "", "")
    pconn = ibm_db_dbi.Connection(conn)

    resultDict = {}
    df = pd.read_sql('select schemaname from syscat.schemata', pconn)
    for (schema,orgcode) in df.itertuples():
        #resultDict[orgcode] = 0
        #sql = "select COUNT(*) from " + orgcode + ".SESSION_SEARCH_PIN_ITEMS"
        sql = "select COUNT(*) from " + orgcode + ".REPORT_SCHEDULE where report_format = \'PDF\'"
        try:
            resdf = pd.read_sql(sql, con=pconn)
            count = resdf.loc[0,'1']
            if count > 0: resultDict[orgcode] = count
        except Exception as e:
            print(str(e))
            pass

    resultdf = pd.DataFrame.from_dict(data=resultDict,orient='index')
    df = resultdf.loc[~resultdf.index.isin(org_excluded)]
    df.to_csv(filename)
    #resultDF.to_csv("../sampleoutputs/dal_SearchPinUsage.csv")

def queryQa3(name):
    hostname = "10.122.107.243"
    filename = "../sampleoutputs/qa_"+name
    user = "db2inst1"
    passwd = "db2inst1"
    org_excluded = ['test']
    queryDatatoCSV(hostname,user,passwd,filename,org_excluded)

def queryProdqa(name):
    hostname = "10.108.240.66"
    filename = "../sampleoutputs/prodqa_"+name
    user = "tlsystem"
    passwd = "B!rd33B!rd"
    org_excluded = ['test']
    queryDatatoCSV(hostname,user,passwd,filename,org_excluded)

def queryDAL(name):
    hostname = "10.142.234.144"
    filename = "../sampleoutputs/DAL_"+name
    user = "tlsystem"
    passwd = "B!rd33B!rd"
    orgs_excluded = ['ORG20160922180442','AURORA','LEARNTEA','TEALEAF','503994339-502220653','503994353-502220660','503383882-502757208','tealeaf-com','503180793-501780791','503180793-501780791','503994359-502220663','503994372-502220669','503994374-502220670','20170815093721','501137933-502338157','aurora-com','20160310172727','20160922180442','503557519-502041070','505112566-502822877','503994370-502220668','503881273-502159154','501198785-501849152','503836898-502135413','503994363-502220665','503570692-501991547','503761519-502094499','20170727124237','503994367-502220667','org4']
    queryDatatoCSV(hostname,user,passwd,filename,orgs_excluded)

def queryWDC(name):
    hostname = "10.108.216.4"
    filename = "../sampleoutputs/WDC_" + name
    user = "tlsystem"
    passwd = "B!rd33B!rd"
    orgs_excluded = ['20150929204041','20160919173225','20171207212358','20171207212358','tealeaf-com','20170126125046','20170815093744','506126005-503356889','aurora-com','aurora-com','20141210113514','20151029154517','20160630140440','20160805162806','20161102203713','20150329174936','20150723064912','20150817155051','20160512060102','20180601222316','20150122093446','20150430070330','20160817183230','20150306090400','505677979-503123865','20160809205215','20160826171636','20170130214554','20171016114731','20180227204930','505923716-503251787']
    queryDatatoCSV(hostname,user,passwd,filename,orgs_excluded)

def querySYD(name):
    hostname = "10.138.55.105"
    filename = "../sampleoutputs/SYD_"+name
    user = "tlsystem"
    passwd = "B!rd33B!rd"
    org_excluded = ['test']
    queryDatatoCSV(hostname,user,passwd,filename,org_excluded)

#main code
queryDAL("ReportScheduleCount.csv")