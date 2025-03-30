"""
write a function called PermGen (permutation generate) to 
generate all the possible permutations of given characters of various 
length up to a maximum value. For example, PermGen(‘ab’, 2) will 
generate strings a, b, aa, ab, ba, bb. 

"""

import hashlib
import time

def PermGen(char_set, max_len):
    if max_len <=0: return 
    for c in char_set:
        yield c
    for c in char_set:
        for next in PermGen(char_set, max_len-1):
            yield c + next

result=PermGen('hello',5) 
print(list(result))  
"""
then compute SHA1 hash values for the permuted characters. Note 
that these characters are represented as strings in Python, so to compute 
hash, we need to convert them to bytes using the “encode()” method. 
"""
for item in list(result): 
    hashvalue = hashlib.sha1(item.encode()).hexdigest() 
    print('SHA1('+item+')='+hashvalue) 

"""
When a password is hashed, the attacker may try to find the preimage 
(the original password). Modify the above code so that the attacker 
can find a password of one English-character (a preimage) from the 
hashed password by going through all the possible characters (froma to z).
Try to find a little longer password, such as ‘fguit’ and measure 
the time to complete the task
"""
start=time.time()
testhash = hashlib.sha1(b'hello').hexdigest()  
print("Suppose we are given SHA1:", testhash)
result=PermGen('abcdefghijklmnopqrstuvwxyz',4)
for item in list(result): 
    hashvalue = hashlib.sha1(item.encode()).hexdigest() 
    if(hashvalue==testhash):
        print('Found: SHA1('+item+')='+hashvalue) 
end=time.time()
print(end - start) 