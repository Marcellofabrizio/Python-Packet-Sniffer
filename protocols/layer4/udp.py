import struct
from ..package.protocol import Protocol

class UDP(Protocol):

    def __init__(self, raw_data):
        self.build_package(raw_data)

    def build_package(self, raw_data):
        self.src_port, self.dest_port, self.size = struct.unpack('! H H 2x H', raw_data[:8])
        self.data = raw_data[8:]
