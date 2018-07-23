# -*- coding: utf-8 -*-
import hashlib as hasher
import datetime as date
import time
import json

# 定义块结构
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index;
        self.timestamp = timestamp;
        self.data = data;
        self.previous_hash = previous_hash;
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash))
        return sha.hexdigest()


def obj_2_json(self):
    return{
        "index": str(self.index),
        "timestamp": str(self.timestamp),
        "data": self.data,
        "previous_hash": self.previous_hash,
        "hash": self.hash_block()
    }


# 创世区块
def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block-CapybaraJ", "0")


# 定义下一个区块
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "CapybaraJ - Block No." + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


# 产生创世区块啦！
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# 我们这个程序这次要产生的区块
num_of_blocks_to_add = 20

# 加到区块链上去
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    time.sleep(1)
    # Tell everyone about it!
    # print json.dumps(block_to_add, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)
    print json.dumps(block_to_add, default=obj_2_json)
    print "Block #{} has been added to the blockchain!".format(block_to_add.index)
    print "Hash: {}\n".format(block_to_add.hash)