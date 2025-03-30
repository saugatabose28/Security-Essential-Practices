"""
Python: Using hash function 

There are many hash functions
 ◦ SHA1, SHA224, SHA256, SHA384, SHA512, MD5
 ◦ Trade-offs between security, speed, and memory usage. 
◦ E.g., some hash functions prioritize speed and low memory usage over security, while others prioritize 
security at the expense of speed or memory usage.
 ◦ MD5 -> 128bits (16 bytes)
 ◦ SHA1 -> 160bits (20 bytes)
 ◦ SHA224 -> 224bits (28 bytes)
 ◦ The longer output length provides advantages in terms of security
 ◦ The output is longer, it is less likely that two different inputs produce the same hash value (a collision)
 ◦ NOTE: MD5 and SHA1 are no longer considered secure due to collision attack
 
 

There are a few different ways to use hash functions in Python. In this 
example, we will be use the “hashlib” module 
compile using python3. What is the result? 
Note that in the hashlib module, sha1(), sha224(), sha256(), sha384(), 
sha512() and md5() are normally available. Try one or two such 
functions. Note also that b'abcdef' is a byte stream for the string 
'abcdef'.  
Modify the above program to take a message as input from the user.   


"""
import hashlib


text = input("Please enter your text: ").encode()

sha1_hash = hashlib.sha1(text)
print("Object: "                      , sha1_hash)
print("Object\'s Hex: "                      , sha1_hash.hexdigest())
print("Object\'s has function name: "                      , sha1_hash.name)
print("Object\'s size: "                      , sha1_hash.digest_size)


md5_hash = hashlib.md5(text)
sha256_hash = hashlib.sha256(text)
sha384_hash = hashlib.sha384(text)
sha512_hash = hashlib.sha512(text)

print("MD5 has size of", md5_hash.digest_size, "bytes:", md5_hash.hexdigest(), '\n')

print("SHA256: has size of", sha256_hash.digest_size, "bytes:", sha256_hash.hexdigest(), '\n')

print("SHA384: has size of", sha384_hash.digest_size, "bytes:", sha384_hash.hexdigest(), '\n')

print("SHA512: has size of", sha512_hash.digest_size, "bytes:", sha512_hash.hexdigest())


"""
 observe the output with the following online tool:
 https://kt.gy/tools.html#conv/abcdef
"""