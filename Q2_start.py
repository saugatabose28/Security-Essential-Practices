from cryptography.fernet import Fernet 
import hashlib
import base64

#An encryption function that on input secret key and plaintext, it returns a ciphertext
def encrypt(key, ptext):
	ctext = Fernet(key).encrypt(ptext)
	return ctext

#A decryption function that on input secret key and ciphertext, it returns a plaintext
def decrypt(key, ctext):
	ptext = Fernet(key).decrypt(ctext)
	return ptext

#A function that on input PIN, it returns its SHA256 in Hex format
def hash_to_key(pin):
	PIN = str(pin)
	hash_pin = hashlib.sha256(PIN.encode()).hexdigest()
	return hash_pin

#A function that on input Hex value, it returns string in Base64 format
#Note that this Base64 format is necessary as the input for encryption function
def b64_encode(hex_input):
	b64 = base64.b64encode(bytes.fromhex(hex_input)).decode()
	return b64


print("==================== Welcome to XXXXXXX's password cracking program ====================")
# ===================== Start your answer here ==================================





# ===================== Stop your answer here ==================================
print("=========================== END ===========================")
