num = input("Press one to read the sales file, press three to check for accounting fraud. ")
import os
folder = os.getcwd()
fileName = folder + "\\sales.csv"
file = open(fileName, 'r')
salesList = []

def readSalesFile():
    readFile = file.readlines()[1:]
    for line in readFile:
        line.replace("\r", '')
        hi = line.split(',')
        hello = hi[1]
        print(hello)

if num == "1":
    readSalesFile()
    file.close()

else:
    file.close()
    print("end")