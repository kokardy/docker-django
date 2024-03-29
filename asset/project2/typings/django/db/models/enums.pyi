"""
This type stub file was generated by pyright.
"""

import enum
from types import DynamicClassAttribute

__all__ = ['Choices', 'IntegerChoices', 'TextChoices']
class ChoicesMeta(enum.EnumMeta):
    """A metaclass for creating a enum choices."""
    def __new__(metacls, classname, bases, classdict, **kwds): # -> _EnumerationT@unique:
        ...
    
    def __contains__(cls, member): # -> bool:
        ...
    
    @property
    def names(cls): # -> list[str]:
        ...
    
    @property
    def choices(cls): # -> list[tuple[None, Unknown]]:
        ...
    
    @property
    def labels(cls): # -> list[Unknown]:
        ...
    
    @property
    def values(cls): # -> list[None]:
        ...
    


class Choices(enum.Enum, metaclass=ChoicesMeta):
    """Class for creating enumerated choices."""
    @DynamicClassAttribute
    def label(self):
        ...
    
    @property
    def do_not_call_in_templates(self): # -> Literal[True]:
        ...
    
    def __str__(self) -> str:
        """
        Use value when cast to str, so that Choices set as model instance
        attributes are rendered as expected in templates and similar contexts.
        """
        ...
    
    def __repr__(self): # -> str:
        ...
    


class IntegerChoices(int, Choices):
    """Class for creating enumerated integer choices."""
    ...


class TextChoices(str, Choices):
    """Class for creating enumerated string choices."""
    ...


