def print_badinputerror(n):
    error_message = "Unzulaessige Eingabe! Eingegebener Wert:\n{n}".format(n=n)
    print(error_message)


def datacell(content):
    return f"| {content} "


def emptycell():
    return "| "


def endrow():
    return "|\n"


def header(columns):
    headline = "|"
    separator = "|"
    for key in columns.keys():
        headline += f"{key}|"
        separator += "-|"
    return f"{headline}\n{separator}\n"

def containslists(columns):
    for column in columns:


def tabulate(columns):
    assert isinstance(columns, dict), print_badinputerror(columns)
    assert containslists(columns), print_badinputerror(columns)
    numberofrows = [len(columns[k]) for k in columns.keys()]
    table = header(columns)

    for rowindex in range(max(numberofrows)):
        colindex = 0
        for colname, data in columns.items():
            if rowindex < numberofrows[colindex]:
                table += datacell(data[rowindex])
            else:
                table += emptycell()
            colindex += 1
        table += endrow()

    return table


def test_tabulate():
    testcases = [
        {
            "input": {
                "time": [0.1, 1.0, 10.0],
                "precision": [1.e-2, 2.34e-3, 8.98e-5],
                "algorithm": ["A", "B", "C"]
            },
            "expected":
                "|time|precision|algorithm|\n|-|-|-|\n"
                + "| 0.1 | 0.01 | A |\n"
                + "| 1.0 | 0.00234 | B |\n"
                + "| 10.0 | 8.98e-05 | C |\n"
        },
        {
            "input": {
                "time": [0.1, 1.0],
                "precision": [1.e-2, 2.34e-3, 8.98e-5],
                "algorithm": ["A", "B", "C"]
            },
            "expected":
                "|time|precision|algorithm|\n|-|-|-|\n"
                + "| 0.1 | 0.01 | A |\n"
                + "| 1.0 | 0.00234 | B |\n"
                + "| | 8.98e-05 | C |\n"
        }
    ]
    for pair in testcases:
        table = tabulate(pair["input"])
        assert pair["expected"] == table


def run_example():
    data = {
        "time": [0.1, 1.0, 10.0],
        "precision": [1.e-2, 2.34e-3, 8.98e-5],
        "algorithm": ["A", "B", "C"]
    }
    table = tabulate(data)
    f = open("table.md", 'w')
    f.write(table)
    f.close()


if __name__ == "__main__":
    test_tabulate()
    run_example()
