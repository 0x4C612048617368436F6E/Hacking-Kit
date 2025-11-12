#!/home/hashcon/Hacking-Kit/bin/python
import base64
import sys

'''
What is a base64 string
'''

def isStringBase64():
	if(len(sys.argv) == 1):
		print("Not enough arguments provided")
		sys.exit(-1)

	#user might add more stuff
	numOfStrings = []
	for i in range(len(sys.argv)-1): #-1 for the name of the file
		numOfStrings.append(sys.argv[i+1])
	stringToConvertToBase64 = "".join(numOfStrings)
	print(stringToConvertToBase64)
	print(base64.b64encode(bytes(stringToConvertToBase64,'utf-8')))


isStringBase64()
