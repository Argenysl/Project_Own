import csv


def SSN_Checker(ssn):
    with open("information.csv", "r") as f:
        csvreader = csv.reader(f, delimiter=",")
        for row in csvreader:
            if ssn in row[4]:
                return False
            else:
                return True


