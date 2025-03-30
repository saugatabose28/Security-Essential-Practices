"""
use of “regular expression (regex)” to extract  
more versatile information from the log file

the regex expression “pattern” represents the 
following. 

• [ ]: Character set- match any character inside the brackets 
• \w: Word- any alphanumeric characters 
• - : The dash character 
• +: Quantifier – match 1 or more of the preceding 
• ( ): Capture group – Groups part of the regular expression together 
• \. : The period “.” character.  

Provide address.txt as input file 

"""
import re

log_file = input("Enter file name: ")

#with open(log_file,"r") as f:
#	sample_file = f.readlines()

f =open(log_file,"r")

email_pattern = r'[\w-]+@([\w-]+\.)+[\w-]'


while True:
	line = f.readline()
	if not line:
		break
	if re.search(email_pattern, line):
		print(line.strip())	

f.close()


	
	
