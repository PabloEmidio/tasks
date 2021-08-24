from .const import VALID_VALUES
from .exceptions import StatusError


class StatusDescriptor:
    def __get__(self, obj, objtype=None):
        value = obj._status
        return value

    def __set__(self, obj, value):
        if not value.lower() in VALID_VALUES:
            raise StatusError('', value.lower())
        obj._status = value.lower()
