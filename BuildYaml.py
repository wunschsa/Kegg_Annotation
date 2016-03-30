import sys
import re

InitFile = open("ecoli.init.txt",'r')
Input = open("ecoli.out.txt", 'r')
yamlout = open("ecoli.init.yaml", "w")
equations = open("Equations.txt", 'r')

ECList = []
gprList = []
geneList = []
i = 1
EqDict = {}
ECDict = {}

for line in equations:
    line = line.strip()
    line = line.split('\t')
    eq = line[0]
    keggEq = line[1]
    EqDict[keggEq] = eq

gene_list = open("Gene_List.txt", 'w')

for line in Input:
    line = line.strip()
    line = line.split('\t')
    rxn = line[0]
    EC = line[2]
    Subsystem = line[3]
    KeggEq = line[4]
    KeggEqCodes = line[5]
    for keggEq, eq in EqDict.iteritems():
        if keggEq == KeggEqCodes:
            Equations = eq
    gpr = line[6]
    gene = line[7]
    EC = EC + "_" + Subsystem + "_" + KeggEq + "_" + KeggEqCodes + "_" + Equations + "_" + gpr + "_" + gene
    ECDict[rxn] = EC

for row in InitFile:
    row = row.strip()
    row = row.split("\t")
    rxnID = row[0]
    Name = row[1]
    eq = row[2]
    eq = eq.replace("[c]", "[c] : ")
    eq = eq.replace("(", "")
    eq = eq.replace(")", "")
    EC_new = row[3]
    for rxn, EC in ECDict.iteritems():
        col = EC.split("_")
        EC = col[0]
        Subsystem = col[1]
        KeggEq = col[2]
        KeggEqCodes = col[3]
        Equations = col[4]
        gpr = col[5]
        gene = col[6]
        if EC_new == EC and rxnID[:2] != "R_":
            yamlout.write("- model: eco.ECOReaction" + "\n")
            yamlout.write("  pk: " + str(i) + "\n")
            yamlout.write("  fields:" + "\n")
            yamlout.write("     rxnID: " + rxnID + "\n")
            yamlout.write("     name: \"" + Name + "\"" + "\n")
            yamlout.write("     ec: " + EC + "\n")
            yamlout.write("     subsystem: \"" + Subsystem + "\"" + "\n")
            yamlout.write("     equation: \"" + eq + "\"" + "\n")
            yamlout.write("     gpr: \"" + gpr + "\"" + "\n")
            yamlout.write("     keggID: " + rxn + "\n")
            yamlout.write("     keggEq: " + KeggEq + "\n")
            yamlout.write("     keggEqCodes: " + KeggEqCodes + "\n")
            yamlout.write("     genes: \"" + gene + "\"" + "\n")
            rxnID = "R_" + rxnID
            i += 1
    if rxnID[:2] != "R_":
        if EC_new == ".":
            EC_new = EC_new.replace(".", "\".\"")
        print EC_new
        yamlout.write("- model: eco.ECOReaction" + "\n")
        yamlout.write("  pk: " + str(i) + "\n")
        yamlout.write("  fields:" + "\n")
        yamlout.write("     rxnID: " + rxnID + "\n")
        yamlout.write("     name: \"" + Name + "\"" + "\n")
        yamlout.write("     ec: " + EC_new + "\n")
        yamlout.write("     subsystem: \"" + "." + "\"" + "\n")
        yamlout.write("     equation: \"" + eq + "\"" + "\n")
        yamlout.write("     gpr: \"" + "." + "\"" + "\n")
        yamlout.write("     keggID: " + "." + "\n")
        yamlout.write("     keggEq: " + "\".\"" + "\n")
        yamlout.write("     keggEqCodes: " + "\".\"" + "\n")
        yamlout.write("     genes: \"" + "." + "\"" + "\n")
        i += 1
