"""
Project 2: Basic Encryption & Decryption (Caesar Cipher)
DecodeLabs Cyber Security Internship Kit

Goal:
Encrypt a message with a Caesar cipher, decrypt it back,
and display both the encrypted and decrypted output.
"""


def shift_character(char, shift):
    """
    Shifts a single character by 'shift' positions.
    - Uppercase letters wrap around A-Z
    - Lowercase letters wrap around a-z
    - Anything else (spaces, digits, punctuation) is left unchanged
    """
    if char.isupper():
        base = 65  # ASCII value of 'A'
    elif char.islower():
        base = 97  # ASCII value of 'a'
    else:
        return char  # edge case: spaces, numbers, punctuation

    # 1) Convert letter to number 0-25
    position = ord(char) - base
    # 2) Add the shift, use % 26 to wrap around the alphabet
    new_position = (position + shift) % 26
    # 3) Convert back to a letter
    return chr(new_position + base)


def encrypt(text, shift):
    """Encrypts the text by shifting every character forward."""
    return "".join(shift_character(char, shift) for char in text)


def decrypt(text, shift):
    """Decrypts the text by shifting every character backward."""
    return "".join(shift_character(char, -shift) for char in text)


def get_shift_key():
    """Asks the user for a shift key and makes sure it is a valid number."""
    while True:
        value = input("Enter shift key (a number, e.g. 3): ")
        try:
            return int(value)
        except ValueError:
            print("Invalid key. Please enter a whole number.")


def main():
    print("=== DecodeLabs Caesar Cipher: Encryption & Decryption ===")

    while True:
        message = input("\nEnter your message (or type 'exit' to quit): ")
        if message.lower() == "exit":
            print("Goodbye!")
            break

        shift = get_shift_key()

        encrypted = encrypt(message, shift)
        decrypted = decrypt(encrypted, shift)

        print("\n--- Result ---")
        print(f"Original Text  : {message}")
        print(f"Encrypted Text : {encrypted}")
        print(f"Decrypted Text : {decrypted}")

        # Validation: decrypting must give back the original message
        if decrypted == message:
            print("Validation     : PASSED (decrypted text matches original)")
        else:
            print("Validation     : FAILED")


if __name__ == "__main__":
    main()
