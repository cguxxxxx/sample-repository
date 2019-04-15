import ibm_db

#qa3
#conn = ibm_db.connect("DATABASE=TLSAAS;HOSTNAME=10.122.107.243;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=db2inst1;", "", "")
#prodqa
#conn = ibm_db.connect("DATABASE=TLSAAS;HOSTNAME=10.108.240.66;PORT=50000;PROTOCOL=TCPIP;UID=tlsystem;PWD=B!rd33B!rd;", "", "")
#wdc
#conn = ibm_db.connect("DATABASE=TLSAAS;HOSTNAME=10.108.216.4;PORT=50000;PROTOCOL=TCPIP;UID=tlsystem;PWD=B!rd33B!rd;", "", "")
#dal
#conn = ibm_db.connect("DATABASE=TLSAAS;HOSTNAME=10.142.234.144;PORT=50000;PROTOCOL=TCPIP;UID=tlsystem;PWD=B!rd33B!rd;", "", "")
#SYD
conn = ibm_db.connect("DATABASE=TLSAAS;HOSTNAME=10.138.55.105;PORT=50000;PROTOCOL=TCPIP;UID=tlsystem;PWD=B!rd33B!rd;", "", "")
#FRA
#conn = ibm_db.connect("DATABASE=TLSAAS;HOSTNAME=10.134.194.133;PORT=50000;PROTOCOL=TCPIP;UID=tlsystem;PWD=B!rd33B!rd;", "", "")
#sqlorgs = "select schemaname from syscat.schemata where schemaname like 'ORG%'"
sqlorgs = "select schemaname from syscat.schemata"
stmtorgs = ibm_db.exec_immediate(conn, sqlorgs)
resultorgs = ibm_db.fetch_both(stmtorgs)
while resultorgs != False:
    orgname = resultorgs["SCHEMANAME"]

    try:
        sqlQryEvents = "select sharetype, COUNT(*) from " + orgname + ".workspace group by sharetype order by sharetype"
        stmtQryEvents = ibm_db.exec_immediate(conn, sqlQryEvents)
        eventCount = ibm_db.fetch_tuple(stmtQryEvents)
        count0 = 0
        count1 = 0
        count2 = 0
        while eventCount != False:
            if eventCount[0] == 0: count0 = eventCount[1]
            if eventCount[0] == 1: count1 = eventCount[1]
            if eventCount[0] == 2: count2 = eventCount[1]
            eventCount = ibm_db.fetch_tuple(stmtQryEvents)
        
        print(orgname + "," + str(count0)+ "," + str(count1)+ "," + str(count2))
    except:
        #print(orgname + ", null")
        pass
    finally:
        resultorgs = ibm_db.fetch_both(stmtorgs)
    
    '''
    sqlQryEvents = "select count(*) from " + orgname+ ".EVENT where \"SIMPLE\" = 1 and reportable = 0"
    stmtQryEvents = ibm_db.exec_immediate(conn, sqlQryEvents)
    eventCount = ibm_db.fetch_tuple(stmtQryEvents)
    print(orgname + ":" + str(eventCount[0]))

    resultorgs = ibm_db.fetch_both(stmtorgs)

    '''