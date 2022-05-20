from ..package.protocol import Protocol

class HTTP:

    def __init__(self, raw_data):
        self.build_package(raw_data)
    
    def build_package(self, raw_data):
        try:
            self.data = raw_data.decode('utf-8')
        except:
            self.data = raw_data
    
