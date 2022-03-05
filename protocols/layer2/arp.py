import socket
import struct
from utils import *

class ARP:
    
    def __init__(self, raw_data):
        header = raw_data
        self.hrdwr_type = header[0]
        self.proto_type = header[1]
        