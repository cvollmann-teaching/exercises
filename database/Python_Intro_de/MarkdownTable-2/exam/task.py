def mdTable(nrows, ncols):
    """
    Gibt eine Markdowntabelle mit ncols Spalten, einer Kopfzeile,
	einer Zwischenlinie und nrows weiteren Zeilen und  in der Konsole aus.
    """
    row_string = ""
    line_string = ""

    for c in range(ncols):
        row_string += "| "  # beachten Sie das Leerzeichen nach dem Strich
        line_string += "|-"

    print(row_string)
    print(line_string)
    for r in range(nrows):
        print(row_string)

if __name__ == "__main__":
	mdTable(0,1)
	mdTable(1,2)
