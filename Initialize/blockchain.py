# Initialising a Blockchain

# Modules Required to be Installed
# Flask == 0.12.2

# Importing the Libraries 
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - Building a Blockchain 

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0', )

