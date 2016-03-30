import re
import sys

input_file = open("Equations.txt", 'r')
outfile = open("EQDIFF.txt", 'w')

for line in input_file:
    line = line.strip()
    line = line.split('\t')
    eq = line[0]
    keggeq = line[1]
    eq = eq.replace("[c] : ", "")
    if eq.startswith("[c]"):
        eq = eq.replace("[c]:", "")
        eq = eq.replace("+", " + ")
        eq = eq.replace("<==>", " <=> ")
        eq = eq.replace("-->", " ")
    eq_split = eq.split(" ")
    kegg_split = keggeq.split(" ")
    for eqDif in eq_split:
        if eqDif.startswith("+") or eqDif.startswith("<") or eqDif == "2" or eqDif == "3" or eqDif == "4" or eqDif == "5" or eqDif == "6" or eqDif == "7" or eqDif == "8" or eqDif == "9" or eqDif == "10" or eqDif == "11" or eqDif == "12" or eqDif == "13" or eqDif == "n" or eqDif == "2n" or eqDif == "3n" or eqDif == "4n" or eqDif == "5n" or eqDif == "6n" or eqDif == "n-1" or eqDif == "n-2" or eqDif == "(n+1)" or eqDif == "16" or eqDif == "(n-1)": 
            pass
        else:
            print eqDif
            outfile.write(eqDif + '\n')
