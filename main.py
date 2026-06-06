
def encrypt():
    text_message = input("Enter your message: ")
    key = int(input("Enter shift value: "))
    
    encrypted_text=" "

    for ch in text_message:

        if ch.isupper():
            alphabet_position = ord(ch) - ord('A')
            shifted_position = (alphabet_position + key) % 26
            encrypted_char = chr(shifted_position + ord('A'))
            encrypted_text += encrypted_char

        elif ch.islower():
            alphabet_position = ord(ch) - ord('a')
            shifted_position = (alphabet_position + key) % 26
            encrypted_char = chr(shifted_position + ord('a'))
            encrypted_text += encrypted_char

        else:
            encrypted_text += ch

    print("\nOriginal Message : ",text_message)
    print("Encrypted Message : ",encrypted_text)

def decrypt():
    encrypted_text = input("Enter encrypted message: ")
    key = int(input("Enter shift value: "))

    decrypted_text = " "

    for ch in encrypted_text:

        if ch.isupper():
            alphabet_position = ord(ch) - ord('A')
            shifted_position = (alphabet_position - key) % 26
            decrypted_char = chr(shifted_position + ord('A'))
            decrypted_text += decrypted_char

        elif ch.islower():
            alphabet_position = ord(ch) - ord('a')
            shifted_position = (alphabet_position - key) % 26
            decrypted_char = chr(shifted_position + ord('a'))
            decrypted_text += decrypted_char

        else:
            decrypted_text += ch

    print("\nEncrypt Message: ",encrypted_text)
    print("Original Message: ",decrypted_text)


print("============ Caesar Cipher Program ============")

print("1 for encryption")
print("2 for decryption")

choice = int(input("Enter your choice(1 or 2): "))

if (choice==1):
    encrypt()

elif(choice==2):
    decrypt()

else:
    print("Invalid choice!")


