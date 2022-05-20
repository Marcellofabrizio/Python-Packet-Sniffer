from abc import ABC, abstractclassmethod

class Protocol(ABC):
    def __init__(self):
        pass

    @abstractclassmethod
    def build_package(self, raw_data):
        pass

    @abstractclassmethod
    def print_data(self):
        pass