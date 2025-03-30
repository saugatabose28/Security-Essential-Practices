"""
Evaluations of log files using Python

Cut and paste 50-100 lines of sample.log 
into the “Your test string:” window in https://pythex.org/. Using the right 
regex expression, try to highlight IP addresses such as 83.149.216.43 : the answer: '(\d+\.\d+\.\d+\.\d+\d)'

Note that  
• \d: Numeric numbers (0-9) 
• \S: Anything except space, tab, carriage return 
• \s: Space, tab, carriage return 
• +: Quantifier – match 1 or more of the preceding 
• ( ): Capture group – Groups part of the regular expression together 
• \" : escape character that instructs regex to treat the character as ".

highlight URL starting with "http…  What regex should 
we use?   the asnwer is: (\"http(\S+)) OR  \"http\:\/\/\S+ 

incorporate the above regex’s into the FOLLOWING code FOR sample.log file input
"""
import re

log_file = input("Enter file name: ")
f = open(log_file, "r")

pattern = r'(\d+\.\d+\.\d+\.\d+\d)'
#pattern = r'(\"http(\S+))'

while True:
	line = f.readline()
	if not line:
		break
	s = re.search(pattern, line)
	if s:
		#print(line.strip())
		print(s.group())

f.close()
	
