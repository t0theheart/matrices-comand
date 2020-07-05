from abc import ABC, abstractmethod


class ReceiverABC(ABC):
    @abstractmethod
    def get_result(self): pass

    @abstractmethod
    def set_result(self, result: dict): pass

    @abstractmethod
    def read(self, read_from: str): pass

    @abstractmethod
    def write(self, write_to: str): pass

    @abstractmethod
    def delete(self): pass

    @abstractmethod
    def sum(self): pass

    @abstractmethod
    def multiply(self): pass

    @abstractmethod
    def transport(self): pass
