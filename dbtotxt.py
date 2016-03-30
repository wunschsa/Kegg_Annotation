import psycopg2
import sys
import re

InitFile = open("ecoli.init.txt",'r')
output = open("ecoli.out.txt", 'w')
#yamlout = open("sml.init.yaml", 'w')

con = None
r = 0
i = 0
j = 0 
m = 0
linecount = 0 
RList = []
ECList = []
GPRDict = {}
RXNDict = {}
ECDict = {}
period = "."

try:
    con = psycopg2.connect(database='metabolicrxn', user='wunschsa') 
    cur = con.cursor()
    cut = con.cursor()

except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)

cut.execute('SELECT * FROM kegg_enzymes')
enLines = cut.fetchall()
for row in enLines:
    ec_ID = row[4]
    ECG = row[0]
    reaction_ID = row[3]
    ec_ID = ec_ID.replace(": ", ":")
    newEC = ec_ID.split(" ")
    for i in newEC:
        if i.startswith("ECO:"):
            print i
            gpr = i.replace("ECO:", "")
            gpr = gpr + "_" + reaction_ID  
            GPRDict[ECG] = gpr
            print ECG, gpr
        
vet = cut.fetchone()

cur.execute('SELECT * FROM kegg_reactions')          
rows = cur.fetchall()
for row in rows:
    for ECG, gpr in GPRDict.iteritems():
        gpr2 = gpr.split("_")
        gpr = gpr2[0]
        reaction = gpr2[1]
        gene = re.sub(r"\w+\(", "", gpr)
        gene = re.sub(r"\)", "", gene)
        gpr = re.sub(r"\(\w+\)","", gpr)
        for t in range(0,8):
            if row[t] == "":
                row = list(row)    #Turn the tuple into a list
                row[t] = "."       #Add a period to the list
                row = tuple(row)   #Then turn it back to a tuple for the dictionary format. 
        rxn_ID = row[0]
        Name = row[1]
        KeggEq = row[2]
        KeggEqCodes = row[3]
        EC = row[4]
        EC = EC.split(" ")
        Subsystem = row[5]
        Subsystem = Subsystem.replace("rn\W+","")
        if row[4] != "":
            for EC_Sing in EC:
                if EC_Sing == ECG:
                    output.write(rxn_ID + "\t" + Name + "\t" + EC_Sing + "\t" + Subsystem + "\t" + KeggEq + "\t" + KeggEqCodes + "\t" + gpr + "\t" + gene + "\n")
                    rxn_ID = "USED"
    if rxn_ID == "USED":
        pass
    else:
        pass
ver = cur.fetchone()

output.close()

for line in InitFile:
    line = line.strip()
    if line.startswith("/EC"):
        ecNew = line.replace("/EC_number=\"", "")
        ecNewNew = ecNew.replace("\"", "")
        ECList.append(ecNewNew)
