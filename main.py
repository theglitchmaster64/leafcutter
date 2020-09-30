#!/usr/bin/env python3

from infra import *
from ecdsa import *

if __name__=='__main__':
    b=Blockchain()
    e=ECDSA()
    e.load_private_key('priv.pem')
