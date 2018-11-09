"""
Section of a work
"""
from typing import List

from Entities.EntityBase import EntityBase
from Entities.Image import Image


class Volume(EntityBase):

    _images: list[EntityBase]

    def __init_subclass__(cls, **kwargs):
        _images: List[Image] = []

    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        assert isinstance(value, list)
        self._images = value
