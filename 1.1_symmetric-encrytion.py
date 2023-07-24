def encrypt_Function(message, key):
    encrypted_text = ""
    for char in message:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_Function(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print()
    print("Lab 9 - Ledidk")
    print("The Caesar Cipher Algorithm")
    print("-------------------------------------------------------------")
    print()

    count = int(0)
    while True:
        try:
            prompt1 = "Enter a shift key for Caesar Cipher\n(It should be an integer and 0 - 25)"
            prompt2 = "(Your key should be 0 - 25)"
            if count <= 0:
                print(prompt1)
            else:
                print(prompt2)

            key = int(input("-> : "))
            if 0 <= key <= 25:
                break
            else:
                count += 2
        except ValueError:
            count += 2

    print("Enter your message (Just a string)")
    message = input("-> : ")



    encrypted_message = encrypt_Function(message, key)
    print()
    print(f"The cipher text of message '{message}' is: {encrypted_message}")

    decrypted_message = decrypt_Function(encrypted_message, key)
    print(f"The recovered plain text is: {decrypted_message}")

if __name__ == "__main__":
    main()
