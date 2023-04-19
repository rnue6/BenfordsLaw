# User input to read sales file and check for accounting fraud
# Opening the folder and locating sales file.
import os
folder = os.getcwd()
fileName = folder + "\\sales.csv"
file = open(fileName, 'r')

# Empty sales list for appending first digits and list of numbers to look for
salesList = []
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def readSalesFile():
    '''This function reads and prints the sales data from the sales.csv file. It also appends the first digit of each
    number into an empty list.'''
    readFile = file.readlines()[1:]
    # Splitting all the lines, printing sales data and getting the first number of each sale
    for line in readFile:
        split = line.split(',')
        firstNum = split[1]
        print(firstNum)
        salesList.append(int(firstNum[0]))

def numFrequency(num, list):
    '''This function counts the frequency of numbers 1-9 in the list of first digits and produces a percentage of the occurences
    in the list.'''
    # Counts number of times a number occurs
    occurrences = (list.count(num))

    # Converts to a percentage
    percentage = occurrences/len(list)*100
    print(percentage)

# User prompt
num = input("Press 1 to read the sales file, 2 to check for accounting fraud, or any other key to exit. ")  

# While loop to reprompt user
while num:
    if num == "1":
        readSalesFile()
        num = input("Press 1 to read the sales file, 2 to check for accounting fraud, or any other key to exit. ")  

    if num == "2":
        # Gets numbers from numList (numbers 1-9) and checks for them in salesList (first digits)
        for i in range(len(numList)):
            print(i+1, "as first digit frequency (%):")
            numFrequency(numList[i], salesList)
            print()
            
        num = input("Press 1 to read the sales file, 2 to check for accounting fraud, or any other key to exit. ")  

    else:
        file.close()
        print("Exited.")
        break
