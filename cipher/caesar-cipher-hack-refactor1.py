import time
# Caesar Cipher Hacker
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def get_file_contents(filename):
    try:
        f = open(filename, "r")
    except:
        print(f'Error: failed to open {filename}')
        exit(1)
    return f.readlines()

def process_content(caesar_data, output_file):
    writer = open(output_file, 'w')

    # Loop through each line in file:
    for message in caesar_data:
        message = message.rstrip()
        print(f'Applying all possible keys to: "{message}"')
        time.sleep(2)
        # Loop through every possible key:
        for key in range(1, len(SYMBOLS)):

            # It is important to set translated to the blank string so that the
            # previous iteration's value for translated is cleared:

            translated = ''

            # Loop through each symbol in message:
            for symbol in message:
                if symbol in SYMBOLS:
                    symbolIndex = SYMBOLS.find(symbol)
                    translatedIndex = symbolIndex - key

                    # Handle the wraparound:
                    if translatedIndex < 0:
                        translatedIndex = translatedIndex + len(SYMBOLS)

                    # Append the decrypted symbol:
                    translated = translated + SYMBOLS[translatedIndex]

                else:
                    # Append the symbol without encrypting/decrypting:
                    print(f'Warning: character -->{symbol}<-- is not in the SYMBOLS set!')
                    translated = translated + symbol

            # Display every possible decryption:
            # print('Key #%s: %s' % (key, translated))
            writer.write('Key #%s: %s\n' % (key, translated))

    print(f'---------------------------------\nCheck {output_file} to find decrypted rows.')
    writer.close()

def main():
    filenm = input('whats the name of the encrypted file: ')
    file_list = get_file_contents(filenm)
    file_list = [x for x in file_list if len(x) >= 2]
    process_content(file_list, "caesar_out.txt")

if __name__ == '__main__':
    main()
