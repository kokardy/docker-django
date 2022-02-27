"""
This type stub file was generated by pyright.
"""

import functools
from django.core.files.storage import FileSystemStorage

searched_locations = ...
class BaseFinder:
    """
    A base file finder to be used for custom staticfiles finder classes.
    """
    def check(self, **kwargs):
        ...
    
    def find(self, path, all=...):
        """
        Given a relative file path, find an absolute file path.

        If the ``all`` parameter is False (default) return only the first found
        file path; if True, return a list of all found files paths.
        """
        ...
    
    def list(self, ignore_patterns):
        """
        Given an optional list of paths to ignore, return a two item iterable
        consisting of the relative path and storage instance.
        """
        ...
    


class FileSystemFinder(BaseFinder):
    """
    A static files finder that uses the ``STATICFILES_DIRS`` setting
    to locate files.
    """
    def __init__(self, app_names=..., *args, **kwargs) -> None:
        ...
    
    def check(self, **kwargs):
        ...
    
    def find(self, path, all=...): # -> str | list[Unknown]:
        """
        Look for files in the extra locations as defined in STATICFILES_DIRS.
        """
        ...
    
    def find_location(self, root, path, prefix=...): # -> str | None:
        """
        Find a requested static file in a location and return the found
        absolute path (or ``None`` if no match).
        """
        ...
    
    def list(self, ignore_patterns): # -> Generator[tuple[str | Unknown, Unknown], None, None]:
        """
        List all files in all locations.
        """
        ...
    


class AppDirectoriesFinder(BaseFinder):
    """
    A static files finder that looks in the directory of each app as
    specified in the source_dir attribute.
    """
    storage_class = FileSystemStorage
    source_dir = ...
    def __init__(self, app_names=..., *args, **kwargs) -> None:
        ...
    
    def list(self, ignore_patterns): # -> Generator[tuple[str | Unknown, Unknown], None, None]:
        """
        List all files in all app storages.
        """
        ...
    
    def find(self, path, all=...): # -> list[Unknown]:
        """
        Look for files in the app directories.
        """
        ...
    
    def find_in_app(self, app, path): # -> None:
        """
        Find a requested static file in an app's static locations.
        """
        ...
    


class BaseStorageFinder(BaseFinder):
    """
    A base static files finder to be used to extended
    with an own storage class.
    """
    storage = ...
    def __init__(self, storage=..., *args, **kwargs) -> None:
        ...
    
    def find(self, path, all=...): # -> list[Unknown]:
        """
        Look for files in the default file storage, if it's local.
        """
        ...
    
    def list(self, ignore_patterns): # -> Generator[tuple[str | Unknown, Unknown | None], None, None]:
        """
        List all files of the storage.
        """
        ...
    


class DefaultStorageFinder(BaseStorageFinder):
    """
    A static files finder that uses the default storage backend.
    """
    storage = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    


def find(path, all=...):
    """
    Find a static file with the given path using all enabled finders.

    If ``all`` is ``False`` (default), return the first matching
    absolute path (or ``None`` if no match). Otherwise return a list.
    """
    ...

def get_finders(): # -> Generator[BaseFinder, None, None]:
    ...

@functools.lru_cache(maxsize=None)
def get_finder(import_path): # -> BaseFinder:
    """
    Import the staticfiles finder class described by import_path, where
    import_path is the full Python path to the class.
    """
    ...

