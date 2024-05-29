def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (a number between 1 and 25): "))
    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted text:", encrypted_text)

    decrypted_text = caesar_cipher(encrypted_text, -shift)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()