from cryptography.fernet import Fernet
import hashlib
import base64

# An encryption function that on input secret key and plaintext, it returns a ciphertext
def encrypt(key, ptext):
    ctext = Fernet(key).encrypt(ptext)
    return ctext

# A decryption function that on input secret key and ciphertext, it returns a plaintext
def decrypt(key, ctext):
    ptext = Fernet(key).decrypt(ctext.encode())
    return ptext.decode()

# A function that on input PIN, it returns its SHA256 in Hex format
def hash_to_key(pin):
    PIN = str(pin)
    hash_pin = hashlib.sha256(PIN.encode()).hexdigest()
    return hash_pin

# A function that on input Hex value, it returns string in Base64 format
# Note that this Base64 format is necessary as the input for the encryption function
def b64_encode(hex_input):
    b64 = base64.b64encode(bytes.fromhex(hex_input)).decode()
    return b64

print("==================== Welcome to the password cracking program ====================")

# loading the encrypted password in Aarons personal computer 
# for general use remove comment from the next line and add comment to the line after
#with open("PWDCiphertext.txt", "r") as file:

with open("PWDCiphertext.txt", "r") as file:
    encrypt_msg = file.read().strip()

# iterating over 1000000 as the pin is 6 digit from 000000 to 999999
for pin in range(1000000):  
    # Convert pin to Fernet encrypt
    hash_msg = hash_to_key(pin)
    b64_msg = b64_encode(hash_msg)
    try:
        #attempt to decrypt
        decrypt_msg = decrypt(b64_msg, encrypt_msg)
        print(f"PIN: {pin:06d}, Password: {decrypt_msg}")
        break
    except Exception as e:
        # Printing error message for wrong pins
        print(f"Failed at PIN {pin:06d}: {str(e)}")

print("=========================== END ===========================")
