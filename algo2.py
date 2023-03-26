
################################
#Here is the data that will have it's acronyms replaced with the airport name
################################

Data = {"wow! This is a test!", "I love GCT Airport!", "CSF", "LAX 2002", "relaxing day at my mom's house", "VERY RELAXING", "ABC", "LAX LAX", "LAXLAX", "LAX sucks lol 😀", "wa", "", "!COW!", "I've used my phone fully unpressurized above 20k, the only part turned off was the cell antenna, the GPS and wifi and everything else was on", "''APG ASQ\nRCS''"}
# Data = {"""APG ASQ RCS 
# """}
# Data = {"""LAX LAX LAX LAX asd"""}a
#Data = {"?? IAH BNA ??"}
# Data = {"AIR OFF 42"}
# Data = {"New FAA Aviation Weather Handbook FAA-H-8083-28"}
# Data = {"HOT AND!!!!"}
# Data = {"LAX LAX ab"}
# Data = {"GET THA MUH  "}
#Data = {"CSF"}

# IATACodeHashmap = {S
#   "CSE": "Crested Butte Airpark",
#   "GCT": "Grand Canyon Bar Ten Airstrip",
#   "LAX": "Los Angeles International Airport"
# }

################################
#here is where we create a hashmap of IATA codes to airport names
################################

import csv
IATACodeHashmap = {}
try:
    with open('airport_codes.csv', 'r', encoding='utf-8') as file: 
    #with open('C:/Users/adamf/OneDrive/Documents/iata_codes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        IATACodeHashmap = {}
        for row in reader:
            IATACodeHashmap[row[0]] = row[1]
except Exception as e:
    print("Error:", e)

#################################
#the algorithm below will replace the IATA codes with the airport names and print before and after
#################################

from collections import deque
newData = deque()

print("BEFORE")
for title_comment in Data:
  print(title_comment)

import re
for comment in Data:
  words = re.split('(\W)', comment)  #using \W will keep the delimiter
  for i in range(0, len(words)):
    word = words[i]
    if len(word) == 3 and word.isupper():
      airport_name = IATACodeHashmap.get(word)
      if (airport_name is not None):
         words[i] = airport_name
  newData.append(''.join(words)) #using ‘’.join is much more efficient than using str += str2



print("\nAFTER")
for replaced_title_comment in newData:
  print(replaced_title_comment)
