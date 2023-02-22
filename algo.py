'''
for each title or comment (with an added space as first and last character) (call it Data){
  //find all capital 3-letter words
  for (int i = 0; i < Data.length - 5; i++){     (length - 5 to not go out of string bounds)
      if ( Data[i] is not alphanumeric and Data[i+4] is not alphanumeric) {
         String potentialCode = Data[i+1] + Data[i+2] + Data[i+3];
         if (potentialCode is uppercase)	
                String fullName = IATACodeHashmap.get(potentialCode);
	    if (fullName != null) { //if there was a match
                        String L = Data[0 : i]; //everything left of IATA code
                        String R = Data[i+4 : Data.length]; //everything right of IATA code
		Data = L + fullName + R; //replace the IATA code with the airport name
                        i = i + fullName.length; //skip scanning the airport name
	    }
          }
    }
}
'''


################################
#Here is the data that will have it's acronyms replaced with the airport name
################################

Data = {"wow! This is a test!", "I love GCT Airport!", "CSE", "LAX 2002", "relaxing day at my mom's house", "VERY RELAXING", "ABC", "LAX LAX", "LAXLAX", "LAX sucks lol 😀"}
#Data = {"LAX LAX LAX"}

# IATACodeHashmap = {
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
    #with open('airport_codes.csv', 'r', encoding='utf-8') as file: 
    with open('C:/Users/adamf/OneDrive/Documents/iata_codes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        IATACodeHashmap = {}
        for row in reader:
            IATACodeHashmap[row[0]] = row[1]
except Exception as e:
    print("Error:", e)

################################
#the algorithm below will replace the IATA codes with the airport names and print before and after
################################

from collections import deque
newData = deque()

print("BEFORE")
for title_comment in Data:
  print(title_comment)

#I may have made a made this lower level than it needed to be but it works!
for title_comment in Data:
  title_comment = " " + title_comment + " "
  #find all capital 3-letter words
  endindex = len(title_comment) - 4
  i = 0
  while i < endindex:
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
  title_comment = title_comment[1 : len(title_comment) - 1] #remove first and last space
  newData.append(title_comment)



print("\nAFTER")
for replaced_title_comment in newData:
  print(replaced_title_comment)
