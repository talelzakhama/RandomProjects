# This script uses Python build-in max funtion to return the longest string in a list
# Here is an example of how to run the script: 
# python3 longestString.py -l "<string_1>" "<string_2>"" ... "<string_n>"


import argparse

parser = argparse.ArgumentParser(description="Returning Longest String")
parser.add_argument('-l','--list',nargs='+',metavar='',required=True,help='List of strings')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q','--quiet',action='store_true',help='print quiet')
group.add_argument('-v','--verbose',action='store_true',help='print verbose')
args = parser.parse_args()

def longestString(l):
	return max(l,key=len,default="")

if __name__=='__main__':
	if args.quiet:
		print(f"\n\033[1;34m{longestString(args.list)}\033[0m\n")
		print ("Hello world")
	elif args.verbose:
		print (f"\nThe longest string you enetered in your list {args.list} is: \033[1;34m{longestString(args.list)}\033[0m\n")
	else:
		print (f"\nHere is your longest string: \033[1;34m{longestString(args.list)}\033[0m\n")
