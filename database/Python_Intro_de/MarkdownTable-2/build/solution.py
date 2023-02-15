#!/usr/bin/env python
# coding: utf-8
# ### Markdown Tabelle mit Überschrift
def mdTable(**columns):
    """
    prints a list of dicts as markdown table. The keys are used as head
    and the content of the list as body of the table's columns.
    The lists do not need to have identical length.
    """
    mdTab = ""
    headline = "|"
    separator = "|"
    for key in columns.keys():
        headline += key  + "|"
        separator += "-|"
    
    mdTab += headline + "\n" + separator + "\n"
    #print(headline)
    #print(separator)
    n_rows = [len(columns[k]) for k in columns.keys()]
    for row in range(max(n_rows)):
        col_number = 0 # ColumNumber
        for key, value in columns.items():
            if row < n_rows[col_number]:
                #print("| " + str(value[row]) + " ", end="")
                mdTab += "| " + str(value[row]) + " "
            else:
                #print("| ", end="")
                mdTab += "| "
            col_number += 1
        #print("|")
        mdTab+="|\n"
        
    # in Datei speichern:
    # f = open("filename", "w")
    # f.write(table)
    # f.close()
    return mdTab
mdTab = mdTable(computationTime = [0.1, 1.0, 10.0],
        precision = [1.e-2, 2.34e-3, 8.98e-5],
        algorithm = ["A", "B", "C"])
print(mdTab)
# in Datei speichern:
#f=open("TESTMD", "w")
#f.write(table)
#f.close()
# |computationTime|precision|algorithm|
# |-|-|-|
# | 0.1 | 0.01 | A |
# | 1.0 | 0.00234 | B |
# | 10.0 | 8.98e-05 | C |
mdTab= mdTable(computationTime = [0.1, 1.0, 10.0],
        someValue = [1.e-2, 2.34e-3],
        algorithm = ["A", "B", "C"])
print(mdTab)
# |computationTime|someValue|algorithm|
# |-|-|-|
# | 0.1 | 0.01 | A |
# | 1.0 | 0.00234 | B |
# | 10.0 | | C |
