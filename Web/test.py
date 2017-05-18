import base64

from Crypto import Random
from Crypto.Cipher import AES

encryptedMessage = base64.b64decode("VErgl7SxRy26bmAxT5UZgB1n3MM=")
IV = base64.b64decode("+FsdfmG+Sn8rvthNRZi/rQ==")
encryptionKey = "b1268a2700000000"

aes = AES.new(str(encryptionKey), AES.MODE_CFB, IV)
print(aes.decrypt(encryptedMessage))
