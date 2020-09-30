from cryptography.hazmat.primitives.asymmetric import ec
import  cryptography.hazmat.backends.openssl.backend as openssl_backend

from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives.serialization import Encoding as ENCODING
from cryptography.hazmat.primitives.serialization import PrivateFormat as PRIV_FORMAT
from cryptography.hazmat.primitives.serialization import PublicFormat as PUB_FORMAT
from cryptography.hazmat.primitives.serialization import NoEncryption as NO_ENCRYPTION
from cryptography.hazmat.primitives.serialization import load_pem_private_key

privkey = ec.generate_private_key(ec.SECP256K1(),openssl_backend)
pubkey = privkey.public_key()

privkey_dump=privkey.private_bytes(encoding=ENCODING.PEM,format=PRIV_FORMAT.PKCS8,encryption_algorithm=NO_ENCRYPTION())
pubkey_dump=pubkey.public_bytes(encoding=ENCODING.PEM,format=PUB_FORMAT.SubjectPublicKeyInfo)

open('priv.pem','wb').write(privkey_dump)
open('pub.pem','wb').write(pubkey_dump)

msg=b'sup m9'
sign = privkey.sign(msg,signature_algorithm=ec.ECDSA(hashes.SHA256()))
