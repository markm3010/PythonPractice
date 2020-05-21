# Reverse Cipher

def encrypt_msg(message):
    msg_len = len(message) - 1
    encrypted_msg = ''

    # I'm reading the 'Cracking Codes...' book
    # by Al Sweigart, I wrote this out for the
    # practice and experience.
    while msg_len >=0:
        encrypted_msg += message[msg_len]
        msg_len -= 1

    return encrypted_msg


def decrypt_it(message):
    return message[::-1]


def main():
    m = input("Type message to encrypt below.\n\n")
    encr_msg = encrypt_msg(m)
    print(f"ENCRYPTED MESSAGE:\n>>>{encr_msg}<<<\n")
    decr_msg = decrypt_it(encr_msg)
    print(f"DECRYPTED MESSAGE:\n>>>{decr_msg}<<<\n")


if __name__ == '__main__':
    main()
