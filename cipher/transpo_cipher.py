import pdb

def main():
    myMessage = 'Common sense is not so common'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)
    print(ciphertext + '|')
    
def encryptMessage(key, message):
    ciphertext = [''] * key
    for field in ciphertext:
        print(f'field: {field}')

    # loop thru each column in ciphertrext:
    for column in range(key):
        currentIndex = column
        print(f'currentIndex: {currentIndex}')

        # keep looping til currentIndex goes past the messag length:
        while currentIndex < len(message):
            # place the character at currentIndex in message at the end
            # of the currnt column in the ciphertext list:
            ciphertext[column] += message[currentIndex]
            print(f'len(message):{len(message)}, column: {column}, ciphertext[{column}]: {ciphertext[column]}')

            # move currentIndex over:
            currentIndex += key
            print(f'currentIndex: {currentIndex}')
    # convert the ciphertext list into a single string value and 
    # return it:
    return  ''.join(ciphertext)

# if this file is run (instead of imported as a module), 
# call the main() function:
if __name__ == '__main__':
    ret = main()










