from crypt import *
import os

key=os.urandom(16)
a=AES(key)
data = b'The quick brown fox jummps over the lazy doge'
open('crypt.bin','wb').write(a.encrypt(data))
