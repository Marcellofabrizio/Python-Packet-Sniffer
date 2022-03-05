import struct

class IPv4:

    def __init__(self, raw_data):
        version_header_length = raw_data[0]
        self.version = version_header_length >> 4
        self.header_length = (version_header_length & 15) * 4
        self.ttl, self.proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', raw_data[:20])
        self.src = self.build_ipv4_addr(src)
        self.target = self.build_ipv4_addr(target)
        self.data = raw_data[self.header_length:]

    def build_ipv4_addr(self, addr):
        '''
        Returns properly formatted IPv4 address
        '''
        return '.'.join(map(str, addr))
