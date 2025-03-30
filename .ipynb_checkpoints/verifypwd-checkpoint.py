"""
uses the 
stored salt and key from "storepwd.py" for the password  csit970* to check whether the password 
inputted from the user is correct.  

The method to check the input string as a byte stream against the key 
value is kdf.verify(your input as a byte stream, key) 
"""
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

#salt = b'\xe4ax\x96hx\xa6\xe4\x8b\xd3 \x19"\x7f\x9cC'
#key = b'?]\xeeLXu\x06\x8f\xc4\xcc\xa8\x05\x95L\xff`\xe7\xb7\xb0\x19 Z\x0f\xbf\xa0\xc0\xfb\x93\x03\xf3|\xdc'


kdf = Scrypt(salt=salt, length =32, n=2**14, r=8, p=1, backend=default_backend())

password = input("What is your password? ")


try:
	kdf.verify(password.encode(), key)
	print('Sucess!')
except:
	print('Incorrect Password')