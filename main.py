
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
            encrypted_text += encrypted_char

    print("\nOriginal Message : ",text_message)
    print("Encrypted Message : ",encrypted_text)

encrypt()



