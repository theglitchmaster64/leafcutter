import datetime
import hashlib
import json
import uuid
from flask import Flask, jsonify
import socket

class NodeController:
    def __init__(self,port=2121):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM | socket.SOCK_NONBLOCK)
        self.peers = []


class BlockData:
    def __init__(self):
        self.data = None

class Transaction:
    def __init__(self):
        self.data = []
        self.uuid = (str(uuid.uuid4()).replace('-',''))

    def add(self,sender,reciever,amount):
        self.data.append({'sender':sender,'reciever':reciever,'amount':amount})

    def __repr__(self):
        uuid = str(self.uuid)+'\n'
        ret_str = ''
        for t in self.data:
            ret_str = ret_str + str(t) +'\n'
        return uuid+ret_str[:-1]

class Mempool:
    def __init__(self):
        self.pool = []

    def add(self,transactionList):
        if type(transactionList) == Transaction:
            transactionList = [transactionList]
        for item in transactionList:
            self.pool.append(item)

class Block:
    def __init__(self,index=None,nonce=None,data=None,prev_hash=None,hash=None):
       self.info = {'index':index,'timestamp':str(datetime.datetime.now()),'nonce':nonce,'data':data,'prev_hash':prev_hash,'hash':hash}
       self.hashable_keys = ['index','timestamp','nonce','data','prev_hash']

    def hash(self,nonce):
        hash_timestamp = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.info['nonce'] = nonce
        self.info['timestamp'] = hash_timestamp
        self.info['hash']=str(hashlib.sha256(self.dump()).hexdigest())
        return (hashlib.sha256(self.dump()).hexdigest())

    def dump(self):
        hashable_dict = dict((i,self.info[i]) for i in self.hashable_keys)
        return (str(hashable_dict).encode())

    def __repr__(self):
        return (str(self.info))

class Blockchain:
    def __init__(self):
        self.chain=[]
        self.chain.append(self.genesis_block())

    def genesis_block(self):
        gen = Block(index=0,nonce=0,data=0,prev_hash=0)
        gen.info['hash']=gen.hash(0)
        return gen

    def get_chain(self):
        return str(self.chain)

    def prev_block(self):
        return self.chain[-1]

    def mine_block(self):
        tmp_block = Block(index=len(self.chain),prev_hash=self.prev_block().info['hash'])
        is_valid = False
        nonce = 0
        while (not is_valid):
            tmp_hash = tmp_block.hash(nonce)
            if (tmp_block.info['hash'][0:4]=='0000'):
                is_valid = True
            else:
                nonce+=1
        self.chain.append(tmp_block)
        return tmp_hash

    def __repr__(self):
        return (str(self.chain))
