"""
This type stub file was generated by pyright.
"""

"""
Useful auxiliary data structures for query construction. Not useful outside
the SQL domain.
"""
class MultiJoin(Exception):
    """
    Used by join construction code to indicate the point at which a
    multi-valued join was attempted (if the caller wants to treat that
    exceptionally).
    """
    def __init__(self, names_pos, path_with_names) -> None:
        ...
    


class Empty:
    ...


class Join:
    """
    Used by sql.Query and sql.SQLCompiler to generate JOIN clauses into the
    FROM entry. For example, the SQL generated could be
        LEFT OUTER JOIN "sometable" T1 ON ("othertable"."sometable_id" = "sometable"."id")

    This class is primarily used in Query.alias_map. All entries in alias_map
    must be Join compatible by providing the following attributes and methods:
        - table_name (string)
        - table_alias (possible alias for the table, can be None)
        - join_type (can be None for those entries that aren't joined from
          anything)
        - parent_alias (which table is this join's parent, can be None similarly
          to join_type)
        - as_sql()
        - relabeled_clone()
    """
    def __init__(self, table_name, parent_alias, table_alias, join_type, join_field, nullable, filtered_relation=...) -> None:
        ...
    
    def as_sql(self, compiler, connection): # -> tuple[str, list[Unknown]]:
        """
        Generate the full
           LEFT OUTER JOIN sometable ON sometable.somecol = othertable.othercol, params
        clause for this join.
        """
        ...
    
    def relabeled_clone(self, change_map): # -> Self@Join:
        ...
    
    @property
    def identity(self): # -> tuple[Type[Self@Join], Unknown, Unknown, Unknown, Unknown]:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def equals(self, other):
        ...
    
    def demote(self): # -> Self@Join:
        ...
    
    def promote(self): # -> Self@Join:
        ...
    


class BaseTable:
    """
    The BaseTable class is used for base table references in FROM clause. For
    example, the SQL "foo" in
        SELECT * FROM "foo" WHERE somecond
    could be generated by this class.
    """
    join_type = ...
    parent_alias = ...
    filtered_relation = ...
    def __init__(self, table_name, alias) -> None:
        ...
    
    def as_sql(self, compiler, connection): # -> tuple[Unknown, list[Unknown]]:
        ...
    
    def relabeled_clone(self, change_map): # -> Self@BaseTable:
        ...
    
    @property
    def identity(self): # -> tuple[Type[Self@BaseTable], Unknown, Unknown]:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def equals(self, other):
        ...
    


