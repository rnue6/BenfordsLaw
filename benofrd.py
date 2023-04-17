num = input("Press one to read the sales file, press three to check for accounting fraud. ")
import os
folder = os.getcwd()
fileName = folder + "\\sales.csv"
file = open(fileName, 'r')
salesList = []
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def readSalesFile():
    readFile = file.readlines()[1:]
    for line in readFile:
        line.replace("\r", '')
        split = line.split(',')
        firstNum = split[1]
        salesList.append(int(firstNum[0]))

def numFrequency(num, list):
    for num in list:
        this = (list.count(num))
        percentage = this/len(list)*100

if num == "1":
    readSalesFile()
    numFrequency(numList, salesList)
    file.close()

else:
    file.close()
    print("end")