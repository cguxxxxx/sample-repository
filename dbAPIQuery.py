import pandas as pd
import ibm_db_dbi
import time
import os

qa3 = "10.122.107.243"
proda = "10.108.240.66"
wdchost = "10.108.216.4"
dalhost = "10.142.234.144"
sydhost = "10.138.55.105"

#sqlorgs = "select schemaname from syscat.schemata where schemaname like 'ORG%'"

def connectDB(hostname):
    conn = ibm_db_dbi.connect("DATABASE=TLSAAS;HOSTNAME="+hostname+";PORT=50000;PROTOCOL=TCPIP;UID=tlsystem;PWD=B!rd33B!rd;", "", "")
    return conn

def testQrySchemas(conn):
    cur = conn.cursor()
    cur.execute("select schemaname from syscat.schemata")
    rows=cur.fetchall()
    
    for row in rows:
        orgname = row[0]
        eventCursor = conn.cursor()
        sqlQryEvents = "select count(*) from " + orgname+ ".EVENT where \"SIMPLE\" = 1 and reportable != 0"
        try:
            eventCursor.execute(sqlQryEvents)
            eventCount = eventCursor.fetchone()
            if (eventCount[0] > 0): 
                print(orgname + "," + str(eventCount[0]))
        except:
            #print(orgname + ", null")
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


conn = connectDB(dalhost)
testQryToxlsx(conn)
#testQrySchemas(conn)
conn.close()
