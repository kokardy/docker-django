"""
This type stub file was generated by pyright.
"""

import functools
from django.core.exceptions import ImproperlyConfigured
from django.utils.functional import cached_property

"""
This type stub file was generated by pyright.
"""
class InvalidTemplateEngineError(ImproperlyConfigured):
    ...


class EngineHandler:
    def __init__(self, templates=...) -> None:
        """
        templates is an optional list of template engine definitions
        (structured like settings.TEMPLATES).
        """
        ...
    
    @cached_property
    def templates(self):
        ...
    
    def __getitem__(self, alias):
        ...
    
    def __iter__(self):
        ...
    
    def all(self):
        ...
    


@functools.lru_cache()
def get_app_template_dirs(dirname):
    """
    Return an iterable of paths of directories to load app templates from.

    dirname is the name of the subdirectory containing templates inside
    installed applications.
    """
    ...

