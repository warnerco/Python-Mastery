#nnw
from cryptography.fernet import Fernet
 
#encrypting string
message = "sun"
 
#use fernet to generate
key = Fernet.generate_key() #128 bits, PKCS7 padding
 
#instance the Fernet class with the key
fernet = Fernet(key) #calling key with Fernet.generate_key() and printing it with variabke fernet
 
#then use the Fernet class instance 
#to encrypt the string string must must be encoded to byte string before encryption
encMessage = fernet.encrypt(message.encode())
print("original string: ", message)
print("encrypted string: ", encMessage)

#decrypt the encrypted string with the fernet instance of the key
decMessage = fernet.decrypt(encMessage).decode()
print("decrypted string: ", decMessage)