# First of all install fuzzywuzzy library: pip3 install fuzzywuzzy
from fuzzywuzzy import fuzz, process
# from testlogger import logger

# Try this command
fuzz.ratio ("hell","hello")


def matchingScore(text1,text2):
	# import the first txt file
	file1=open (text1,"r")
	file1=file1.read()

	# import the second txt file
	file2= open (text2,"r")
	file2 = file2.read()
	return fuzz.ratio(file1,file2)


if __name__=="__main__":
	path1= input("Please enter path to first text:\n")
	path2= input("Please enter path to second text:\n")
	print (f"fuzz ratio is {matchingScore(path1,path2)}")
