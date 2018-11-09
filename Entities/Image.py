"""
A format-independent representation of an image
"""

from Entities.EntityBase import EntityBase


class Image(EntityBase):

    def __init_subclass__(cls, **kwargs):
        pass
