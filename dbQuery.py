import ibm_db

#qa3
conn = ibm_db.connect("DATABASE=TLSAAS;HOSTNAME=10.122.107.243;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=db2inst1;", "", "")
#prodqa
#conn = ibm_db.connect("DATABASE=TLSAAS;HOSTNAME=10.108.240.66;PORT=50000;PROTOCOL=TCPIP;UID=tlsystem;PWD=B!rd33B!rd;", "", "")
#wdc
#conn = ibm_db.connect("DATABASE=TLSAAS;HOSTNAME=10.108.216.4;PORT=50000;PROTOCOL=TCPIP;UID=tlsystem;PWD=B!rd33B!rd;", "", "")
#dal
#conn = ibm_db.connect("DATABASE=TLSAAS;HOSTNAME=10.142.234.144;PORT=50000;PROTOCOL=TCPIP;UID=tlsystem;PWD=B!rd33B!rd;", "", "")
#SYD
#conn = ibm_db.connect("DATABASE=TLSAAS;HOSTNAME=10.138.55.105;PORT=50000;PROTOCOL=TCPIP;UID=tlsystem;PWD=B!rd33B!rd;", "", "")
#FRA
#conn = ibm_db.connect("DATABASE=TLSAAS;HOSTNAME=10.134.194.133;PORT=50000;PROTOCOL=TCPIP;UID=tlsystem;PWD=B!rd33B!rd;", "", "")
#sqlorgs = "select schemaname from syscat.schemata where schemaname like 'ORG%'"
sqlorgs = "select schemaname from syscat.schemata"
stmtorgs = ibm_db.exec_immediate(conn, sqlorgs)
resultorgs = ibm_db.fetch_both(stmtorgs)
while resultorgs != False:
    orgname = resultorgs["SCHEMANAME"]

    try:
        sqlQryEvents = "select count(*) from " + orgname+ ".EVENT where \"SIMPLE\" = 1 and reportable != 0"
        stmtQryEvents = ibm_db.exec_immediate(conn, sqlQryEvents)
        eventCount = ibm_db.fetch_tuple(stmtQryEvents)
        count = eventCount[0]
        if count > 0: print(orgname + "," + str(count))
    except:
        print(orgname + ", null")
    finally:
        resultorgs = ibm_db.fetch_both(stmtorgs)
    
    '''
    sqlQryEvents = "select count(*) from " + orgname+ ".EVENT where \"SIMPLE\" = 1 and reportable = 0"
    stmtQryEvents = ibm_db.exec_immediate(conn, sqlQryEvents)
    eventCount = ibm_db.fetch_tuple(stmtQryEvents)
    print(orgname + ":" + str(eventCount[0]))

    resultorgs = ibm_db.fetch_both(stmtorgs)

    '''