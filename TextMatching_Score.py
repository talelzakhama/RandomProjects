# First of all install fuzzywuzzy library: pip3 install fuzzywuzzy
from fuzzywuzzy import fuzz, process
from testlogger import logger

# Try this command
fuzz.ratio ("hell","hello")

# import the first txt file
file1=open (r"/Users/talelzakhama/Desktop/Untitled_7.rtf","r")
file1=file1.read()

# import the second txt file
file2 = open (r"/Users/talelzakhama/Desktop/Untitled 3.rtf","r")
file2 = file2.read()

score = fuzz.ratio(file1,file2)

logger.info ("fuzz ratio is {}".format(score))
