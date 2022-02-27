"""
This type stub file was generated by pyright.
"""

from django.db.models.expressions import Func

__all__ = ['Index']
class Index:
    suffix = ...
    max_name_length = ...
    def __init__(self, *expressions, fields=..., name=..., db_tablespace=..., opclasses=..., condition=..., include=...) -> None:
        ...
    
    @property
    def contains_expressions(self): # -> bool:
        ...
    
    def create_sql(self, model, schema_editor, using=..., **kwargs):
        ...
    
    def remove_sql(self, model, schema_editor, **kwargs):
        ...
    
    def deconstruct(self): # -> tuple[str, tuple[F | Unknown, ...], dict[str, Unknown | str]]:
        ...
    
    def clone(self): # -> Self@Index:
        """Create a copy of this Index."""
        ...
    
    def set_name_with_model(self, model): # -> None:
        """
        Generate a unique name for the index.

        The name is divided into 3 parts - table name (12 chars), field name
        (8 chars) and unique hash + suffix (10 chars). Each part is made to
        fit its size by truncating the excess length.
        """
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    


class IndexExpression(Func):
    """Order and wrap expressions for CREATE INDEX statements."""
    template = ...
    wrapper_classes = ...
    def set_wrapper_classes(self, connection=...): # -> None:
        ...
    
    @classmethod
    def register_wrappers(cls, *wrapper_classes): # -> None:
        ...
    
    def resolve_expression(self, query=..., allow_joins=..., reuse=..., summarize=..., for_save=...): # -> Func:
        ...
    
    def as_sqlite(self, compiler, connection, **extra_context): # -> tuple[Unknown, list[Unknown]]:
        ...
    

