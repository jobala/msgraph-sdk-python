from abc import ABC, abstractmethod


class ABCAuthentication(ABC):
    @abstractmethod
    def get_access_token(self):
        pass
