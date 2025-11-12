#!/home/hashcon/Hacking-Kit/bin/python
import base64
import sys
import re

'''
What is a base64 string
'''

def isStringBase64():
	if((len(sys.argv) == 1) or (len(sys.argv) > 2)):
		print("Not enough arguments provided")
		sys.exit(-1)
	#read the provided file
	holdLargeFileContent = []
	with open(sys.argv[1],'r') as largeFile:
		for i in largeFile:
			holdLargeFileContent.append(i)

	potentialBase64 = "".join(holdLargeFileContent)
	#print(potentialBase64)

	#The length of a base64 sting must be of multiple of 4
	if((len(potentialBase64)%4)!=0):
		print("Provided string is not off base64")
		return
	regexForBase64 = "^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$"
	if(re.search(regexForBase64,potentialBase64)):
		#insted of print out to the console, we write to a file
		#val = base64.b64decode(potentialBase64)
		#Write to .bin file
		with open('./binary.bin','wb') as writeBinary:
			writeBinary.write(base64.b64decode(potentialBase64))
		return
	print("This is not a base64 string")


isStringBase64()
