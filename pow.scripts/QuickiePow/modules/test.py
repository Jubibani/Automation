from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()

# Initialize a Fernet cipher object with the key
cipher_suite = Fernet(key)

# Plaintext message to encrypt
plaintext_message = b"Hello, this is a secret message!"

# Encrypt the plaintext message
cipher_text = cipher_suite.encrypt(plaintext_message)

# Decrypt the ciphertext back to plaintext
decrypted_message = cipher_suite.decrypt(cipher_text)

# Print the results
print("Original message:", plaintext_message.decode())
print("Encrypted message:", cipher_text)
print("Decrypted message:", decrypted_message.decode())
