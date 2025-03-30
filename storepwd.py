"""
One of the most common usages for hash function is to store passwords. 
In most OS, passwords are not stored in a clear form, but in a hashed 
form. However, when the passwords are hashed, they are hashed together 
with a short random value, called a “random nonce” or “salt”. That is, in 
your system the record [salt, H(password||salt)] is stored and the 
system allows your password if you enter the right password. – Note that 
if the entered password, “password*” is the same as “password” 
H(password||salt) = H(password*||salt) holds, the system will 
allow your password.  
Using the password storage algorithm scrypt in cryptography module, 
we  can write a simple (but powerful) password storage code in Python. 
"""
import os

from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

salt = os.urandom(16)
kdf = Scrypt(salt=salt, length =32, n=2**14, r=8, p=1, backend=default_backend())
"""
 length: represents the length of the hashed password in byte. 
n represents the responsiveness. If the password store file is for interactive user login, 2∗∗14=214 is recommended, but in other situations, the higher number 2∗∗20=220 is recommended. 
The parameters r, n, and p are tuning parameters that impact how long it will take to compute and how much memory is required. the recommended are r-8, p=1

"""
key = kdf.derive(b'csit970*')
#print("key:", key)
#print("salt:", salt)

"""
(Note that in the above Scrypt function, length represents the length of the 
hashed password in byte.  n represents the responsiveness. If the password store 
file is for interactive user login, 2**14 = 214 is recommended, but in other 
situations, the higher number  2**20 = 220 is recommended. The parameters r, n, 
and p are tuning parameters that impact how long it will take to compute and 
how much memory is required. The recommended parameters are r=8 and p=1.) 

Print the values of salt, which is a random nonce, and 
key, which is a hashed password. 
"""
