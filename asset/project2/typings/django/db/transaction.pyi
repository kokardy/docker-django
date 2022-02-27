"""
This type stub file was generated by pyright.
"""

from contextlib import ContextDecorator, contextmanager
from django.db import ProgrammingError

class TransactionManagementError(ProgrammingError):
    """Transaction management is used improperly."""
    ...


def get_connection(using=...): # -> Any:
    """
    Get a database connection by name, or the default database connection
    if no name is provided. This is a private API.
    """
    ...

def get_autocommit(using=...): # -> Any:
    """Get the autocommit status of the connection."""
    ...

def set_autocommit(autocommit, using=...): # -> Any:
    """Set the autocommit status of the connection."""
    ...

def commit(using=...): # -> None:
    """Commit a transaction."""
    ...

def rollback(using=...): # -> None:
    """Roll back a transaction."""
    ...

def savepoint(using=...): # -> Any:
    """
    Create a savepoint (if supported and required by the backend) inside the
    current transaction. Return an identifier for the savepoint that will be
    used for the subsequent rollback or commit.
    """
    ...

def savepoint_rollback(sid, using=...): # -> None:
    """
    Roll back the most recent savepoint (if one exists). Do nothing if
    savepoints are not supported.
    """
    ...

def savepoint_commit(sid, using=...): # -> None:
    """
    Commit the most recent savepoint (if one exists). Do nothing if
    savepoints are not supported.
    """
    ...

def clean_savepoints(using=...): # -> None:
    """
    Reset the counter used to generate unique savepoint ids in this thread.
    """
    ...

def get_rollback(using=...): # -> Any:
    """Get the "needs rollback" flag -- for *advanced use* only."""
    ...

def set_rollback(rollback, using=...): # -> Any:
    """
    Set or unset the "needs rollback" flag -- for *advanced use* only.

    When `rollback` is `True`, trigger a rollback when exiting the innermost
    enclosing atomic block that has `savepoint=True` (that's the default). Use
    this to force a rollback without raising an exception.

    When `rollback` is `False`, prevent such a rollback. Use this only after
    rolling back to a known-good state! Otherwise, you break the atomic block
    and data corruption may occur.
    """
    ...

@contextmanager
def mark_for_rollback_on_error(using=...): # -> Generator[None, None, None]:
    """
    Internal low-level utility to mark a transaction as "needs rollback" when
    an exception is raised while not enforcing the enclosed block to be in a
    transaction. This is needed by Model.save() and friends to avoid starting a
    transaction when in autocommit mode and a single query is executed.

    It's equivalent to:

        connection = get_connection(using)
        if connection.get_autocommit():
            yield
        else:
            with transaction.atomic(using=using, savepoint=False):
                yield

    but it uses low-level utilities to avoid performance overhead.
    """
    ...

def on_commit(func, using=...): # -> None:
    """
    Register `func` to be called when the current transaction is committed.
    If the current transaction is rolled back, `func` will not be called.
    """
    ...

class Atomic(ContextDecorator):
    """
    Guarantee the atomic execution of a given block.

    An instance can be used either as a decorator or as a context manager.

    When it's used as a decorator, __call__ wraps the execution of the
    decorated function in the instance itself, used as a context manager.

    When it's used as a context manager, __enter__ creates a transaction or a
    savepoint, depending on whether a transaction is already in progress, and
    __exit__ commits the transaction or releases the savepoint on normal exit,
    and rolls back the transaction or to the savepoint on exceptions.

    It's possible to disable the creation of savepoints if the goal is to
    ensure that some code runs within a transaction without creating overhead.

    A stack of savepoints identifiers is maintained as an attribute of the
    connection. None denotes the absence of a savepoint.

    This allows reentrancy even if the same AtomicWrapper is reused. For
    example, it's possible to define `oa = atomic('other')` and use `@oa` or
    `with oa:` multiple times.

    Since database connections are thread-local, this is thread-safe.

    An atomic block can be tagged as durable. In this case, raise a
    RuntimeError if it's nested within another atomic block. This guarantees
    that database changes in a durable block are committed to the database when
    the block exists without error.

    This is a private API.
    """
    _ensure_durability = ...
    def __init__(self, using, savepoint, durable) -> None:
        ...
    
    def __enter__(self): # -> None:
        ...
    
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    


def atomic(using=..., savepoint=..., durable=...): # -> Atomic:
    ...

def non_atomic_requests(using=...): # -> (view: Unknown) -> Unknown:
    ...

