from cryptography.fernet import Fernet

# key = Fernet.generate_key()

# Inputs
message = input('Enter a Message: ')
action = input('1 - Encrypt, 2 - Decrypt: ')

# Invalid Action
if action not in ['1', '2']:
    print('Invalid Action: %s (!)' % action)

# Valid Action
else:
    # Fetch Key
    key = ''
    try:
        with open('key.fnt', 'r') as key:
            key = key.read()        
            fernet = Fernet(bytes(key.encode()))
    except:
        print("'key.fnt' File Not Found (!)")
    
    # Valid Key
    if key != '':
        # Encrypt
        if action == '1':
            enc = fernet.encrypt(message.encode())
            print('Encrypted Message: %s' % enc)
        # Decrypt
        elif action == '2':
            # Bytes to String
            if message[:2] == "b'" and message[-1] == "'":
                message = message[2:-1]
            dec = fernet.decrypt(bytes(message.encode())).decode()
            print('Decrypted Message: %s' % dec)
