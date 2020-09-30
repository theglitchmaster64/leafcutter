import os
from cryptography.hazmat.primitives.asymmetric import ec
import cryptography.hazmat.backends.openssl.backend as openssl_backend

from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

from cryptography.hazmat.primitives.serialization import Encoding as ENCODING
from cryptography.hazmat.primitives.serialization import PrivateFormat as PRIV_FORMAT
from cryptography.hazmat.primitives.serialization import PublicFormat as PUB_FORMAT
from cryptography.hazmat.primitives.serialization import NoEncryption as NO_ENCRYPTION
from cryptography.hazmat.primitives.serialization import load_pem_private_key

class ECDSA:
    def __init__(self):
        self.privkey = None
        self.pubkey = None

    def generate_keypair(self):
        self.privkey = ec.generate_private_key(ec.SECP256K1(),openssl_backend)
        self.pubkey = self.privkey.public_key()
        self.privkey_dump = self.privkey.private_bytes(encoding=ENCODING.PEM,format=PRIV_FORMAT.PKCS8,encryption_algorithm=NO_ENCRYPTION())
        self.pubkey_dump = self.pubkey.public_bytes(encoding=ENCODING.PEM,format=PUB_FORMAT.SubjectPublicKeyInfo)

    def __repr__(self):
        return str(self.privkey_dump)+str(self.pubkey_dump)

    def sign(self,msg):
        return self.privkey.sign(msg,signature_algorithm=ec.ECDSA(hashes.SHA256()))

    def verify(self,signature,msg):
            try:
                if self.pubkey.verify(signature,msg,signature_algorithm=ec.ECDSA(hashes.SHA256())) == None:
                    return True
            except InvalidSignature:
                return False

    def load_private_key(self,filename):
        if(os.path.isfile(filename)==True):
            pkstr = open(filename,'rb').read()
            self.privkey=load_pem_private_key(pkstr,password=None,backend=openssl_backend)
            self.pubkey = self.privkey.public_key()
        else:
            raise OSError('file not found')

    def save_keys(self):
        if (os.path.isfile('private.pem')==True or os.path.isfile('public.pem')==True):
            raise OSError('file(s) already exists')
        else:
            open('private.pem','wb').write(self.privkey_dump)
            open('public.pem','wb').write(self.pubkey_dump)

    def pubkey_dump(self):
        x_int = self.pubkey.public_numbers().x
        x_bytes = x_int.to_bytes(32,byteorder='big')
        y_int = self.pubkey.public_numbers().y
        y_bytes = y_int.to_bytes(32,byteorder='big')
        ret = {'x':{'bytes':x_bytes,'int':x_int},'y':{'bytes':y_bytes,'int':y_int} }
        return ret
