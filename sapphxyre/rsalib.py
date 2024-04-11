from Crypto.PublicKey import RSA
import uuid, os, keyboard

def generateNewKeys(outputDirPublicKey, outputDirPrivateKey):
    print('creating keychain\nvalidating target path...')
    if os.path.exists(outputDirPrivateKey) and os.path.exists(outputDirPublicKey):
        print('target path is valid')
    else:
        print('target path is not valid\ndefault target is \'' + str(os.getcwd()) + '\'\npress (C) to confirm, (X) to override, or press any other key to abort... ')
        while True:
            if keyboard.read_key() == str.lower('c'):
                outputDirPrivateKey = os.getcwd()
                outputDirPublicKey = os.getcwd()
                print('updated target path')
                break
            elif keyboard.read_key() == str.lower('x'):
                print('\a\nbypass selected (ATT=2)\nattempting to create dir at set target path')
                try:
                    if outputDirPrivateKey == outputDirPublicKey:
                        os.mkdir(outputDirPrivateKey)
                    else:
                        os.mkdir(outputDirPrivateKey)
                        os.mkdir(outputDirPublicKey)
                    print('operation completed. no errors were reported')
                except:
                    print('operation failed. target path set to the default dir')
                    outputDirPrivateKey = os.getcwd()
                    outputDirPublicKey = os.getcwd()
                break
            else:
                return False
    print('creating new keys')
    key_value = RSA.generate(2048)
    print('setting identifiers')
    while True:
        public_key_identifier = uuid.uuid4().hex
        private_key_identifier = uuid.uuid4().hex
        if os.path.exists(os.path.join(outputDirPublicKey, public_key_identifier)) or os.path.exists(os.path.join(outputDirPrivateKey, private_key_identifier)):
            continue
        else:
            break
    public_key_path = os.path.join(outputDirPublicKey, public_key_identifier + '.pem')
    private_key_path = os.path.join(outputDirPrivateKey, private_key_identifier + '.pem')
    print('writing keys to file')
    f = open(public_key_path, 'wb')
    f.write(key_value.publickey().exportKey('PEM'))
    f.close()
    f = open(private_key_path, 'wb')
    f.write(key_value.exportKey('PEM'))
    f.close()
    print('clearing cache')
    key_value = 0
    print('key operation completed sucessfully\noutput dir=\'' + str(private_key_path) + '\'')
    return True
