# This script take the path to a text file and returns the number of occurences of a string inside that file
import re

def FindWord(text,word):
	#Read the txt file.
	with open (text) as f:
		f=f.readlines()
	# Converting the list to a string
	fstr= str(f)
	#Searching for the string of interest, here it's "Passed"
	re.search (word,fstr)
	# Listing all found strings of interest.
	all_found = re.findall(word,fstr)
	return len(all_found)

if __name__=="__main__":
	path = input("Please enter path to text:\n")
	string = input ("Please enter the word you're looking for below\n")
	print (f"Keyword '{string}' was found {FindWord(path,string)} times\nAdios Amigo")
