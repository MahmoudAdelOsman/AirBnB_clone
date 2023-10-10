#!/usr/bin/env python3
from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel class defines common attributes/methods for other classes.
    """
    def __init__(self):
        """
        Initializes a new instance of BaseModel.

        Attributes:
            id (str): Unique identifier assigned using uuid.
            created_at (datetime): time of creation
            updated_at (datetime): time of update/edit
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: String representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: Dictionary representation of the BaseModel instance.
        """
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result
