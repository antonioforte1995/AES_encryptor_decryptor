import os
import cryptography
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


# padder() is A padding PaddingContext instance.
padder = padding.PKCS7(algorithms.AES.block_size).padder()

# load plaintext file
filename = input ("Give me the file to encrypt: \n")
readed_file = open("./"+ filename, "r").read()
print ("\nValue of the plaintext file is: {0}".format(readed_file))
message = bytes(readed_file, "utf-8")
padded_data  = padder.update(message) + padder.finalize()


backend = default_backend()


# comment the following lines if you haven't a key and an IV
# load key
key_filename = input ("Give me the file with the key: \n")
key = open("./"+ key_filename,"r").read()
# load iv
iv_filename = input ("Give me the file with the iv: \n")
iv = open("./"+ iv_filename,"r").read()


# A CipherBackend instance
cipher = Cipher(algorithms.AES(bytes.fromhex(key[0:64])), modes.CBC(bytes.fromhex(iv[0:32])), backend=backend)


# encryptor() is an encrypting CipherContext instance
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize() #finalize() finalizes the current context and return the rest of the data (data are bytes)
print("\nValue of the ciphertext is: {0}".format(ciphertext))


# decryptor() is a decrypting CipherContext instance
decryptor = cipher.decryptor()
ciphertext = decryptor.update(ciphertext) + decryptor.finalize()
print("\nValue of decrypted message with padding is: {0}".format(ciphertext))


# unpadder() is an unpadding PaddingContext instance.
unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
data = unpadder.update(ciphertext)
message = data + unpadder.finalize()
print("\nValue of  decrypted message without padding is: {0}".format(message[0:len(message)-1]))


