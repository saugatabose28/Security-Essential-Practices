"""
1. Performing symmetric encryption using Python:  
a) To install Cryptography module on Python:  On Command Prompt, 
type  pip install cryptography 

b) First, create a file called “symenc.py” in your folder. Then, type the 
following codes in symenc.py: 
from cryptography.fernet import Fernet  
def create_key():  
key = Fernet.generate_key() 
return key 
secretkey = create_key() 
print("Encryption Key:", secretkey) 
In the first line of the above code, “Fernet” is a part of Python 
cryptography library that enables users to implement symmetric 
encryption easily without knowing great details of the cryptographic 
algorithms.  The Fernet class has a generate_key() method, which we 
can call to generate a random (pseudorandom actually) key. Run this 
code. What is the result? You will see the random key starting with b’. 
This means the key is represented as “byte”. Remember that the key, 
plaintext, ciphertext, all of which are processed by Fernet 
methods should be all bytes.  
Now, comment out the line of code that displays the key and add a few 
lines of code to get the following:  
from cryptography.fernet import Fernet  
def create_key(): # def means “function” 
key = Fernet.generate_key() 
return key 
def encrypt(key, ptext):   
ctext = Fernet(key).encrypt(ptext) 
return ctext 
secretkey = create_key() 
print("Encryption Key:", secretkey) 
plaintext = input("Enter your message to encrypt: ") 
ciphertext = encrypt(secretkey, plaintext) 
print("Ciphertext: ", ciphertext) 
Run the above code. Did the code run okay? Most likely, we will get 
TypeErrors. Why did this happen? Because the string you inputted is not 
in byte type. Then you should change it to byte. To do that, we need to use 
encode() method.  Change 
ciphertext = encrypt(secretkey, plaintext) 
to  
ciphertext = encrypt(secretkey, plaintext.encode())

and compile the code again and run. What happens? You will see the 
ciphertext begins with b’. This means the ciphertext is represented in 
byte format.   
Now, modify the above code to the following one:  
from cryptography.fernet import Fernet  
def create_key(): # def means “function” 
key = Fernet.generate_key() 
return key 
def encrypt(key, ptext):   
ctext = Fernet(key).encrypt(ptext) 
return ctext 
def decrypt(key, ctext): 
ptext = Fernet(key).decrypt(ctext) 
return ptext 
secretkey = create_key() 
#print("Encryption Key:", secretkey) 
plaintext = input("Enter your message to encrypt: ") 
ciphertext = encrypt(secretkey, plaintext.encode()) 
print("Ciphertext:", ciphertext) 
print("Plaintext (decrypted): ", decrypt(secretkey, 
ciphertext)) 
Note that the same secretkey is used for decryption as we are using 
symmetric encryption. 
Additional comments:  
1) We often need to display all the ciphertexts and plaintexts in string 
format, not byte format. To do this, we can use the decode() method. 
Change   
print("Plaintext (decrypted): ", decrypt(secretkey, 
ciphertext)) 
to  
print("Plaintext (decrypted): "+ decrypt(secretkey, 
ciphertext).decode()) 
What happens? Why could you use + in the print function? 
2) If you want to make the functions in the code to return the results in 
string format, we can make key to key.decode(), ctext to 
ctext.decode() and so on.  

3) You may find that whenever the code is run a different ciphertext will 
be created, this is because a random key is generated whenever the 
code is run.  

"""
from cryptography.fernet import Fernet 

def create_key():
    key = Fernet.generate_key()
    return key

def encrypt(key, ptext):
    ctext = Fernet(key).encrypt(ptext)
    return ctext

def decrypt(key, ctext):
    ptext = Fernet(key).decrypt(ctext)
    return ptext

enckey = create_key()
plaintext = input("Enter your message to encrypt: ")
ciphertext = encrypt(enckey, plaintext.encode())
print("Ciphertext:"+ ciphertext.decode())

deckey = enckey
print("Plaintext (decrypted): ", decrypt(deckey, ciphertext))
