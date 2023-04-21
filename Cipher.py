# Paulean Marguerette F. Parrish
# BSCPE 1-4
# Problem 3 of Assignment 2
# The purpose of this program is to generate the ciphertext using the Vigenere Cipher

import pyfiglet

# Header for the activity
print("Vigenere Cipher".center(70, "="))

# Ask the user to input a message and key to be encrypted
message = input("\033[95mEnter a message: ")
keyword = input("\033[96mEnter a keyword: ")

# Look over the string and convert it to uppercase
message_uc = message.upper()
keyword_uc = keyword.upper()

# Remove spaces in the string
message_ns = message_uc.replace(" ", "")
keyword_ns = keyword_uc.replace(" ", "")

# Convert the keyword to its corresponding letter values 0-25
keyword_value = [ord(letter) - ord('A') for letter in keyword_ns]

# Encryption of the message
cipher_text = ''.join(chr((ord(letter) - ord('A') + keyword_value[index % len(keyword_ns)]) % 26 
+ ord('A')) for index, letter in enumerate(message_ns))

# Print the ciphertext
des = pyfiglet.figlet_format(cipher_text, font = "digital")
print("\033[93mThe message: ", message_ns)
print("\033[93mThe keyword: ", keyword_ns)
print("\033[97mThe Ciphertext: ")
print(des)