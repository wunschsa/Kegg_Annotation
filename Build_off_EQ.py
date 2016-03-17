import sys
import re

Eq_in = open("Eq_Convert.txt", 'r')
input_file = open("iJR904RXN.txt", 'r')

LIST = open("LIST_OF_COMPOUNDS.txt", 'w')

metDic = {} 

out = open("Converted.txt", 'w')

for line in Eq_in:
    line = line.strip()
    line = line.split('\t')
    met = line[0]
    kegg = line[1]
    if met.startswith("C") and kegg.startswith("C"):
        pass
    elif met.startswith("G") and kegg.startswith("G"):
        pass
    else:
        LIST.write(met + '\t' + kegg + '\n')
        metDic[met] = kegg

for line in input_file:
    line = line.strip()
    line = line.split('\t')
    reaction = line[2]
    if reaction.startswith("[c]"):
        rxn = reaction.replace("[c]", "")
        rxn = rxn.split(" ")
        for rxn_sing in rxn:                                                                                                                                              
            for met, kegg in metDic.iteritems():
                if rxn_sing == met:
                    #out.write(kegg + " ")
                    rxn_sing = kegg
            out.write(rxn_sing + " ")
        out.write("\n")
        #print rxn
    elif reaction.startswith("[e]"):
        rxn = reaction.replace("[e]", "")
        rxn = rxn.split(" ")
        for rxn_sing in rxn:
            for met, kegg in metDic.iteritems():
                if rxn_sing == met:
                    #out.write(kegg + " ")                                                                                                                                    
                    rxn_sing = kegg
            out.write(rxn_sing + " ")
        out.write("\n")
    else:
        ## ADD these manually to the yaml file. 
        manual = reaction
