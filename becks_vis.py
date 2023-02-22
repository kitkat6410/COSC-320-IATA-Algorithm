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
    with open('datasets/aviation_comments_submissions_2023.csv', 'r', encoding='utf-8') as file: 
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            Data.append(row[0])
except Exception as e:
    print("Error:", e)

print("data len: " + str(len(Data)))

def algo(myData):
    newData = []
    for title_comment in myData:
      title_comment = " " + title_comment + " "
      #find all capital 3-letter words
      endindex = len(title_comment) - 4
      i = 0
      while i < endindex:
            try:
                #print(str(i) + title_comment[i] + " " + title_comment[i+4])
                if not title_comment[i].isalnum() and not title_comment[i+4].isalnum(): #check if the character left and right of potential code is nonalphanumeric
                  potentialCode = title_comment[i+1] + title_comment[i+2] + title_comment[i+3]
                  if potentialCode.isupper():
                    fullName = IATACodeHashmap.get(potentialCode)
                    if fullName!= None: #if there was a match
                      title_comment = title_comment[0 : i + 1] + fullName + title_comment[i+4 : len(title_comment)]
                      endindex += (len(fullName) - 2) #adjust the end index 
                      i += len(fullName) #skip scanning the airport name
                i += 1
            except Exception as e:
                i += 1
                continue
      title_comment = title_comment[1 : len(title_comment) - 1] #remove first and last space
      newData.append(title_comment)
    return newData
   
def tryItABunch(myFn, startN=10, endN=100, stepSize=10, numTrials=20, listMax = 10):
    nValues = []
    tValues = []
    for n in range(startN, endN, stepSize):
        print("trying " + str(n) + " times")
        # run myFn several times and average to get a decent idea.
        runtime = 0
        for t in range(numTrials):
            lst = Data[:n] # generate a random list of length n
            start = time.time()
            myFn( lst )
            end = time.time()
            runtime += (end - start) * 1000 # measure in milliseconds
        runtime = runtime/numTrials
        nValues.append(n)
        tValues.append(runtime)
    return nValues, tValues


nValues, tValues = tryItABunch( algo, startN=10, endN=1000)

plt.plot(nValues, tValues, color="blue", label="Algo #1")
plt.xlabel("n")
plt.ylabel("Time(ms)")
plt.legend()
plt.title("Multiple string replace algo")