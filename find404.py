##!/usr/bin/env python3
#  find out some information from the log files.  In this 
#exercise, we write a code (named “find404.py”) to find the logs that 
#contain the error code “404”. 

# Provide sample.log as input file

log_file=input("What file to analyse? ")
f= open(log_file, "r")

while True:
	line = f.readline()
	if not line:
		break
	if "404" in line:
		print(line.strip())

f.close()
