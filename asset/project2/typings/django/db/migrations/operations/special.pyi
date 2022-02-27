"""
This type stub file was generated by pyright.
"""

from .base import Operation

class SeparateDatabaseAndState(Operation):
    """
    Take two lists of operations - ones that will be used for the database,
    and ones that will be used for the state change. This allows operations
    that don't support state change to have it applied, or have operations
    that affect the state or not the database, or so on.
    """
    serialization_expand_args = ...
    def __init__(self, database_operations=..., state_operations=...) -> None:
        ...
    
    def deconstruct(self): # -> tuple[str, list[Unknown], dict[Unknown, Unknown]]:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def describe(self): # -> Literal['Custom state/database change combination']:
        ...
    


class RunSQL(Operation):
    """
    Run some raw SQL. A reverse SQL statement may be provided.

    Also accept a list of operations that represent the state change effected
    by this SQL change, in case it's custom column/table creation/deletion.
    """
    noop = ...
    def __init__(self, sql, reverse_sql=..., state_operations=..., hints=..., elidable=...) -> None:
        ...
    
    def deconstruct(self): # -> tuple[str, list[Unknown], dict[str, Unknown]]:
        ...
    
    @property
    def reversible(self): # -> bool:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def describe(self): # -> Literal['Raw SQL operation']:
        ...
    


class RunPython(Operation):
    """
    Run Python code in a context suitable for doing versioned ORM operations.
    """
    reduces_to_sql = ...
    def __init__(self, code, reverse_code=..., atomic=..., hints=..., elidable=...) -> None:
        ...
    
    def deconstruct(self): # -> tuple[str, list[Unknown], dict[str, Unknown]]:
        ...
    
    @property
    def reversible(self): # -> bool:
        ...
    
    def state_forwards(self, app_label, state): # -> None:
        ...
    
    def database_forwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def database_backwards(self, app_label, schema_editor, from_state, to_state): # -> None:
        ...
    
    def describe(self): # -> Literal['Raw Python operation']:
        ...
    
    @staticmethod
    def noop(apps, schema_editor): # -> None:
        ...
    


