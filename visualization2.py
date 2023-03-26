import csv
import time
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

IATACodeHashmap = {}
try:
    with open('airport_codes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        IATACodeHashmap = {}
        for row in reader:
            IATACodeHashmap[row[0]] = row[1]
except Exception as e:
    print("Error:", e)

Data = []
try:
    with open('datasets/smaller_data_set.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            Data.append(row[0])
except Exception as e:
    print("Error:", e)

print("data len: " + str(len(Data)))

import re
from collections import deque

def algo2(myData):
    newData = []
    for comment in myData:
        words = re.split('(\W)', comment)  #using \W will keep the delimiterr
        for i in range(0, len(words)):
            word = words[i]
            if len(word) == 3 and word.isupper():
                airport_name = IATACodeHashmap.get(word)
                if (airport_name is not None):
                    words[i] = airport_name
        newData.append(''.join(words)) #using ''.join is much more efficient than using str += str2
    return newData

def algo(myData):
    newData = deque()
    for title_comment in myData:
        if (len(title_comment) >= 3):  # filter out titles and comments that are less than 3 characters long (iata codes are 3 characters long)

            title_comment = " " + title_comment + "  "
            # find all capital 3-letter words
            endindex = len(title_comment) - 5
            i = 0
            # print("comment length" + str(len(title_comment)))

            while i < endindex:
                # print(len(title_comment))
                # print(str(i) + title_comment[i] + " " + title_comment[i+4])
                # check if the character left and right of potential code is nonalphanumeric
                if not title_comment[i].isalnum() and not title_comment[i+4].isalnum():
                    potentialCode = title_comment[i+1] + \
                        title_comment[i+2] + title_comment[i+3]
                    if potentialCode.isupper():
                        fullName = IATACodeHashmap.get(potentialCode)
                        if fullName != None:  # if there was a match
                            title_comment = title_comment[0: i + 1] + \
                                fullName + \
                                title_comment[i+4: len(title_comment)]
                            # adjust the end index
                            endindex += (len(fullName) - 3)
                            # skip scanning the airport name
                            i += len(fullName)
                            # print("endindex: " + str(endindex))
                            # print("i: " + str(i))
                i += 1
            # remove first and last space
            title_comment = title_comment[1: len(title_comment) - 2]
        newData.append(title_comment)
    return newData


def tryItABunch(myFn, startN=10, endN=100, stepSize=10, numTrials=20, listMax=10):
    nValues = []
    tValues = []
    for n in range(startN, endN, stepSize):
        print("trying " + str(n) + " times")
        # run myFn several times and average to get a decent idea.
        runtime = 0
        for t in range(numTrials):
            lst = Data[:n]  # generate a random list of length n
            start = time.time()
            myFn(lst)
            end = time.time()
            runtime += (end - start) * 1000  # measure in milliseconds
        runtime = runtime/numTrials
        nValues.append(n)
        tValues.append(runtime)
    return nValues, tValues


end = 1500
nValues2, tValues2 = tryItABunch(algo2, startN=10, endN=end)
nValues, tValues = tryItABunch(algo, startN=10, endN=end)


m2 = tValues2[-1]/nValues2[-1]
x2 = np.arange(0, end, 10)
y2 = m2*x2

m = tValues[-1]/nValues[-1]
x = np.arange(0, end, 10)
y = m*x


plt.plot(nValues, tValues, color="blue", label="First Algorithm")
plt.plot(nValues2, tValues2, color="green", label="Second Algorithm") #
#plt.plot(x,y, color = "red", label="O(n)")
plt.xlabel("n")
plt.ylabel("Time(ms)")
plt.legend()
plt.title("Algorithm comparison")
plt.show()
