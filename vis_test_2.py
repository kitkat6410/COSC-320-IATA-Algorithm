import numpy as np
import matplotlib.pyplot as plt
import timeit
import csv
import random
import string

def generate_random_string(n):
    alphanumeric = string.ascii_letters + string.digits + ' '
    return ''.join(random.choice(alphanumeric) for _ in range(n))

# Generate a random string of length 10, including spaces
random_string = generate_random_string(50)
print(random_string)

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
for i in range (1000000):
    random_number = random.randint(10, 50)
    Data.append(generate_random_string(random_number))


# Define the function to be timed
def process_data_n(n):
    data_copy = Data[:n]
    for title_comment in data_copy:
        title_comment = " " + title_comment + " "
        endindex = len(title_comment) - 5
        i = 0
        while i < endindex:
            if not title_comment[i].isalnum() and not title_comment[i+4].isalnum():
                potentialCode = title_comment[i+1] + title_comment[i+2] + title_comment[i+3]
                if potentialCode.isupper():
                    fullName = IATACodeHashmap.get(potentialCode)
                    if fullName is not None:
                        title_comment = title_comment[0:i+1] + fullName + title_comment[i+4:]
                        endindex += (len(fullName) - 2)
                        i += len(fullName)
            i += 1
        title_comment = title_comment[1 : len(title_comment) - 1]

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