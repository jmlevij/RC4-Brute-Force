import itertools
import string
from Crypto.Cipher import ARC4
from binascii import unhexlify
from tqdm import tqdm  # Import tqdm for the progress bar

# RC4 decryption function
def rc4_decrypt(key, ciphertext):
    cipher = ARC4.new(key)
    return cipher.decrypt(ciphertext)

# Prompt the user for the ciphertext and key length
ciphertext_hex = input("Enter the RC4-encrypted hex string: ")
key_length = int(input("Enter the key length: "))

# Convert the hex string into bytes
ciphertext = unhexlify(ciphertext_hex)

# Character set: lowercase, uppercase, and digits
charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Total number of combinations for the key length
total_combinations = len(charset) ** key_length

# Brute-force all possible passwords with a progress bar
for password_tuple in tqdm(itertools.product(charset, repeat=key_length), total=total_combinations, desc="Pwning - Please wait!"):
    password = ''.join(password_tuple)
    
    # Attempt to decrypt using the current password
    decrypted_message = rc4_decrypt(password.encode(), ciphertext)
    
    # Check if the decrypted message makes sense assuming it is readable in ASCII
    try:
        decrypted_message_ascii = decrypted_message.decode('ascii')
        # Print the password and decrypted message if it seems valid
        print(f"Password: {password}, Decrypted message: {decrypted_message_ascii}")
        break  # Stop if we find the correct password
    except UnicodeDecodeError:
        # Ignore invalid passwords that do not result in valid ASCII text
        continue
