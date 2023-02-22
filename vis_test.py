import numpy as np
import matplotlib.pyplot as plt
import timeit
import csv
# define IATA hashmap
with open('airport_codes.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    IATACodeHashmap = {}
    for row in reader:
        IATACodeHashmap[row[0]] = row[1]
# Define data

with open('test_reddit_posts.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    Data = []
    for row in reader:
        Data.append(row[0])
# Define the input sizes to test
input_sizes = [10, 100, 1000, 10000]

# Define an empty list to store the runtimes for each input size
runtimes = []

# Define the function to be timed
def process_data(Data, IATACodeHashmap):
    for title_comment in Data:
        title_comment = " " + title_comment + " "
        endindex = len(title_comment) - 5
        i = 0
        while i < endindex:
            if not title_comment[i].isalnum() and not title_comment[i+4].isalnum():
                potentialCode = title_comment[i+1] + title_comment[i+2] + title_comment[i+3]
                if potentialCode.isupper():
                    fullName = IATACodeHashmap.get(potentialCode)
                    if fullName != None:
                        title_comment = title_comment[0:i+1] + fullName + title_comment[i+4:]
                        endindex += (len(fullName) - 2)
                        i += len(fullName)
            i += 1
        title_comment = title_comment[1 : len(title_comment) - 1]

# Measure the runtime of the code for each input size
from tryItABunch import tryItABunch
nValues, tValues = tryItABunch( process_data(Data, IATACodeHashmap), startN = 50, endN = 1050, stepSize=50, numTrials=5, listMax = 10) 
# Plot the results
plt.plot(nValues, tValues, color="blue", label="mymom")
# plt.plot(input_sizes, runtimes)
plt.xlabel("Input size (n)")
plt.ylabel("Runtime (s)")
plt.title("Runtime complexity of code")
plt.show()




