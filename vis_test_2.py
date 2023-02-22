import numpy as np
import matplotlib.pyplot as plt
import timeit
import csv
import random
import string

# def generate_random_string(n):
#     alphanumeric = string.ascii_letters + string.digits + ' '
#     return ''.join(random.choice(alphanumeric) for _ in range(n))

# # Generate a random string of length 10, including spaces
# random_string = generate_random_string(50)
# print(random_string)

# Define IATA hashmap
with open('airport_codes.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    IATACodeHashmap = {}
    for row in reader:
        IATACodeHashmap[row[0]] = row[1]

# Define data
# with open('test_reddit_posts.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     Data = []
#     for row in reader:
#         Data.append(row[0])
Data = []
# for i in range (10000):
#     random_number = random.randint(10, 50)
#     Data.append(generate_random_string(random_number))

try:
    with open('./datasets/aviation_comments_submissions_2023.csv', 'r', encoding='utf-8') as file: 
    #with open('C:/Users/adamf/OneDrive/Documents/iata_codes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        Data = []
        for row in reader:
            Data.append(row[0])
except Exception as e:
    print("Error:", e)

# Define the function to be timed
def process_data_n(n):
 for title_comment in Data:
  if (len(title_comment) >= 3): #filter out titles and comments that are less than 3 characters long (iata codes are 3 characters long)
    title_comment = " " + title_comment + "  "
    #find all capital 3-letter words
    endindex = len(title_comment) - 5
    i = 0
    while i < endindex:
      #print(str(i) + title_comment[i] + " " + title_comment[i+4])
      #print(title_comment)
      if not title_comment[i].isalnum() and not title_comment[i+4].isalnum(): #check if the character left and right of potential code is nonalphanumeric
        potentialCode = title_comment[i+1] + title_comment[i+2] + title_comment[i+3]
        if potentialCode.isupper():
          fullName = IATACodeHashmap.get(potentialCode)
          if fullName!= None: #if there was a match
            title_comment = title_comment[0 : i + 1] + fullName + title_comment[i+4 : len(title_comment)]
            endindex += (len(fullName) - 3) #adjust the end index l
            i += len(fullName) #skip scanning the airport name
      i += 1
    title_comment = title_comment[1 : len(title_comment) - 2] #remove first and last space


# Measure the runtime of the code for each input size
from timeit import timeit
def measure_runtime(func, n):
    return timeit(lambda: func(n), number=5)

n_values = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000]

runtimes = []
for n in n_values:
    runtime = measure_runtime(process_data_n, n)
    runtimes.append(runtime)

# Plot the results
plt.plot(n_values, runtimes, color="blue", label="mymom")
plt.xlabel("Input size (n)")
plt.ylabel("Runtime (s)")
plt.title("Runtime complexity of code")
plt.show()
print("done!")