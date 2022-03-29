import re

# Read the txt file.
infile =r"/Users/talelzakhama/Desktop/Test.log"

#Read the txt file.
with open (infile) as f:
	f=f.readlines()

# Converting the list to a string
fstr= str(f)

word = input ("Please enter the word you're looking for below\n")

#Searching for the string of interest, here it's "Passed"
re.search (word,fstr)

# Listing all found strings of interest.
all_found = re.findall("Passed",fstr)

print ("Keyword ""{}"" was found {} times\nAdios Amigo".format(word,len(all_found)))