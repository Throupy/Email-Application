"""Decorators that may be useful, sometimes."""

class WriteOnceReadWhenever:
    def __setattr__(self, attr, value):
        if hasattr(self, attr):
            raise Exception("Attempting to alter read-only value")

        self.__dict__[attr] = value
