'''
Use this file to encrypt a string in reverse
'''

def reverse():
    message = input("Type your message here: ")
    cypher_text = str(message[::-1])
    return cypher_text

if __name__ == '__main__':
    while True:
        choice = input("Would you like to encrypt your message?")
        if "y" in choice:
            print(reverse())
        else:
            exit()
