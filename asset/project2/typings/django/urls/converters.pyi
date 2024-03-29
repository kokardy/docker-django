"""
This type stub file was generated by pyright.
"""

from functools import lru_cache

"""
This type stub file was generated by pyright.
"""
class IntConverter:
    regex = ...
    def to_python(self, value):
        ...
    
    def to_url(self, value):
        ...
    


class StringConverter:
    regex = ...
    def to_python(self, value):
        ...
    
    def to_url(self, value):
        ...
    


class UUIDConverter:
    regex = ...
    def to_python(self, value):
        ...
    
    def to_url(self, value):
        ...
    


class SlugConverter(StringConverter):
    regex = ...


class PathConverter(StringConverter):
    regex = ...


DEFAULT_CONVERTERS = ...
REGISTERED_CONVERTERS = ...
def register_converter(converter, type_name):
    ...

@lru_cache(maxsize=None)
def get_converters():
    ...

def get_converter(raw_converter):
    ...

