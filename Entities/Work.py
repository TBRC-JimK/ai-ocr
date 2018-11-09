from typing import List

from Entities.EntityBase import EntityBase
from Entities.Volume import Volume
from Entities.Metadata import Metadata


class Work(EntityBase):
    """
    A collection of Volumes, with metadata
    """

    def __init__(self):
        self.volumes = [Volume]
        self.metadata = None

    _volumes: List[Volume]
    _metadata: Metadata

    @property
    def volumes(self):
        return self._volumes

    @volumes.setter
    def volumes(self, value):
        self._volumes = value

    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        self._metadata = value
