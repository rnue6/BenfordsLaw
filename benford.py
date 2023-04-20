import matplotlib.pyplot as plt

# Digit frequency data
digit_data = {
    'Digit': ['6', '7', '1', '3', '2', '4', '5', '9', '8'],
    'Percentage': [6.790123456790123, 5.679012345679013, 31.48148148148148, 12.716049382716049,
                   13.82716049382716, 11.049382716049383, 9.012345679012345, 5.185185185185185,
                   4.2592592592592595],
    'Occurrences': [110, 92, 510, 206, 224, 179, 146, 84, 69]
}

# Extract data for plotting
digits = digit_data['Digit']
percentages = digit_data['Percentage']
occurrences = digit_data['Occurrences']

# Create a bar graph
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(digits, percentages)

# Set labels and title
ax.set_xlabel('Digit')
ax.set_ylabel('Percentage')
ax.set_title('Digit Frequency')

# Display the bar graph
plt.show()

# Save the bar graph as an image file
fig.savefig('results.png')

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
