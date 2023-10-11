#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        mos_tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, mos_tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        mos_rdict = self.__dict__.copy()
        mos_rdict["created_at"] = self.created_at.isoformat()
        mos_rdict["updated_at"] = self.updated_at.isoformat()
        mos_rdict["__class__"] = self.__class__.__name__
        return mos_rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        mos_clname = self.__class__.__name__
        return "[{}] ({}) {}".format(mos_clname, self.id, self.__dict__)
