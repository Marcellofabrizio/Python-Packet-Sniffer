from utils import format_multi_line
from ..package.protocol import Protocol

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

class HTTP:

    def __init__(self, raw_data):
        self.build_package(raw_data)
    
    def build_package(self, raw_data):
        try:
            self.data = raw_data.decode('utf-8')
            self.http_info = str(self.data).split('\n')
        except:
            self.data = raw_data
            self.tcp_info = self.data
    
    
    def print_data(self):
        if self.tcp_info is None:
            print(TAB_2 + 'TCP Data:')
            print(format_multi_line(TAB_3, self.tcp_info))

        if self.http_info is not None:
            print(TAB_2 + 'HTTP Data:')
            for line in self.http_info:
                print(TAB_3 + str(line))