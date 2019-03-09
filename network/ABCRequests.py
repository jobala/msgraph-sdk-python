from abc import ABC, abstractmethod


class ABCRequests(ABC):
    @abstractmethod
    def get(self, path, token):
        pass

