"""
This type stub file was generated by pyright.
"""

def sql_flush(style, connection, reset_sequences=..., allow_cascade=...):
    """
    Return a list of the SQL statements used to flush the database.
    """
    ...

def emit_pre_migrate_signal(verbosity, interactive, db, **kwargs): # -> None:
    ...

def emit_post_migrate_signal(verbosity, interactive, db, **kwargs): # -> None:
    ...

