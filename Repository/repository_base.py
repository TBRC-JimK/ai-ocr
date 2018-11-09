from abc import ABC, abstractmethod
from Entities import *   # No whining. We want them all

class RepositoryBase(ABC):
    def __init_subclass__(self, **kwargs):
        """
        Do something as soon as I figure it out
        :param kwargs:
        """

    @abstractmethod
    def GetWork(self,workName) -> Work:
        """
        Retrieves a work by name
        :param workName:
        :return:
        """
        pass

    @abstractmethod
    def GetMetadata(self, Work) -> Metadata:
        pass

    @abstractmethod
    def GetVolumes(self, Work): list[Volume]
        """
        retrieves Volume objects for a work
        :param Work: 
        :return: 
        """

