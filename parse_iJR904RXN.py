import sys
import re

input_file = open("iJR904RXN.txt", 'r')

output = open("ecoli.init.txt", 'w')

for line in input_file:
    line = line.strip() 
    line = line.split("\t")
    rxnID = line[0]
    name = line[1]
    rxn = line[2]
#    subsystem = line[3]
    try:
        ec = line[4]
    except IndexError:
        ec = 'null'
    if ec == "" or ec == "null" or ec == "EC-Undetermined":
        ec = "."
    ec = ec.replace("EC-", "")
    print ec
    output.write(rxnID + "\t" + name + "\t" + rxn +  "\t" + ec + "\n")
