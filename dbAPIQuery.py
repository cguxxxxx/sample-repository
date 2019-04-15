import pandas as pd
import ibm_db_dbi
import time
import os

qa3 = "10.122.107.243"  #UID=db2inst1;PWD=db2inst1;
proda = "10.108.240.66"  #UID=tlsystem;PWD=B!rd33B!rd;
wdchost = "10.108.216.4"
dalhost = "10.142.234.144"
sydhost = "10.138.55.105"

#sqlorgs = "select schemaname from syscat.schemata where schemaname like 'ORG%'"

def connectDB(hostname, qa):
    if qa:
        conn = ibm_db_dbi.connect("DATABASE=TLSAAS;HOSTNAME="+hostname+";PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=db2inst1;", "", "")
    else:
        conn = ibm_db_dbi.connect("DATABASE=TLSAAS;HOSTNAME="+hostname+";PORT=50000;PROTOCOL=TCPIP;UID=tlsystem;PWD=B!rd33B!rd;", "", "")
    return conn


def testQrySchemas(conn):
    cur = conn.cursor()
    cur.execute("select schemaname from syscat.schemata")
    rows=cur.fetchall()
    
    for row in rows:
        orgname = row[0]
        eventCursor = conn.cursor()
        #sqlQryEvents = "select count(*) from " + orgname+ ".EVENT where \"SIMPLE\" = 1 and reportable != 0"
        sqlQryEvents = "select COUNT(*) from " + orgname + ".SESSION_SEARCH_PIN_ITEMS"
        #sqlQryEvents1 = "select COUNT(*) from " + orgname + ".workspace where sharetype = 1"
        #sqlQryEvents2 = "select COUNT(*) from " + orgname + ".workspace where sharetype = 2"
        #sqlQryEvents0 = "select COUNT(*) from " + orgname + ".workspace where sharetype = 0"
        #sqlQry = "select count(*) from ORG20190104024443.workspace where sharetype=1"
        
        try:
            eventCursor.execute(sqlQryEvents)
            countrow = eventCursor.fetchone()
            count1 = countrow[0]

            print(orgname + "," + count1)
        except:
            print(orgname + ", null")
            pass

def testQryToxlsx(conn):
    today = time.strftime("%Y%m%d")
    stmt = "select schemaname from syscat.schemata"
    #writer = pd.ExcelWriter('./temp/{hostname}_{dbname}report{rdate}.xlsx'.format(hostname=host,dbname=db,rdate=today), engine='xlsxwriter')
    writer = pd.ExcelWriter('./out/report{rdate}.xlsx'.format(rdate=today), engine='xlsxwriter')
    df = pd.read_sql(stmt, con=conn)
    df.to_excel(writer,sheet_name='dbschema',index=False)
    writer.save()
    print(df.to_json(orient='index'))

conn = connectDB(qa3, True)
#testQryToxlsx(conn)
testQrySchemas(conn)
conn.close()
