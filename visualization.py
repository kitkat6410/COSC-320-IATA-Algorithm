# %matplotlib inline
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import csv
airport_codes = {}
with open('airport_codes.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    airport_codes = {}
    for row in reader:
        airport_codes[row[0]] = row[1]

    
#     for each title or comment (with an added space as first and last character) (call it Data){
#   //find all capital 3-letter words
#   for (int i = 0; i < Data.length - 5; i++){     (length - 5 to not go out of string bounds)
#       if ( Data[i] is not alphanumeric and Data[i+4] is not alphanumeric) {
#          String potentialCode = Data[i+1] + Data[i+2] + Data[i+3];
#          if (potentialCode is uppercase)	
#                 String fullName = IATACodeHashmap.get(potentialCode);
# 	    if (fullName != null) { //if there was a match
#                         String L = Data[0 : i]; //everything left of IATA code
#                         String R = Data[i+4 : Data.length]; //everything right of IATA code
# 		Data = L + fullName + R; //replace the IATA code with the airport name
#                         i = i + fullName.length; //skip scanning the airport name
# 	    }
#           }
#     }
# }


def naiveInsertionSort(A):
    B = [None for i in range(len(A))] # B is a blank list of the same length as A
    for x in A:
        for i in range(len(B)):
            if B[i] == None or B[i] > x:
                # then x goes in spot i, and we should move everything over.
                j = len(B)-1
                while j > i:
                    B[j] = B[j-1]
                    j -= 1
                B[i] = x
                break # okay we are done placing x
    return B
A = [6,4,3,8,5]
B = naiveInsertionSort(A)
print(B)
def InsertionSort(A):
    for i in range(1,len(A)):
        current = A[i]
        j = i-1
        while j >= 0 and A[j] > current:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = current
A = [6,4,3,8,5]
InsertionSort(A)
print(A)
from tryItABunch import tryItABunch
nValuesNaive, tValuesNaive = tryItABunch( naiveInsertionSort, startN = 50, endN = 1050, stepSize=50, numTrials=10, listMax = 10 )
nValues, tValues = tryItABunch( InsertionSort, startN = 50, endN = 1050, stepSize=50, numTrials=5, listMax = 10) 
plt.plot(nValuesNaive, tValuesNaive, color="red", label="Naive version")
plt.plot(nValues, tValues, color="blue", label="Less naive version")
plt.xlabel("n")
plt.ylabel("Time(ms)")
plt.legend()
plt.title("Naive vs. non-naive insertion sort")
plt.show()


