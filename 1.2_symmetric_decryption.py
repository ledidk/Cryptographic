def decrypt_Function(secretMessage, key):
    decrypted_text = ""
    for char in secretMessage:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def hacking_Function(text):
    words = text.split()
    num_blocks = 4  # Assuming there are four blocks of words in the secret message

    for i in range(num_blocks):
        block_text = " ".join(words[i::num_blocks])  # Extract the words for each block
        print(f"\nBlock {i + 1} | Encrypted text: {block_text}\n")
        for key in range(26):
            decrypted_message = decrypt_Function(block_text, key)
            print(f"Key: {key:2} | Decrypted message: {decrypted_message}")

def main():
    print()
    print("Lab 9 - Ledidk")
    print("Hacking Activity: Retrieve the secret message from the given ciphertext")
    print("-------------------------------------------------------------")
    print()

    secretMessage = "QVIREFVGL ZJ DJG LMKXGZMA"
    print(f"Secret message to decrypt: {secretMessage}")
    hacking_Function(secretMessage)

if __name__ == "__main__":
    main()

# QVIREFVGL   -   ZJ   -   DJG  -   LMKXGZMA
#13 Disersity -  17 IS - 15 OUR - 19 STRENGH