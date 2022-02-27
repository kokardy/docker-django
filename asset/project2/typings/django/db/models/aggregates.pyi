"""
This type stub file was generated by pyright.
"""

from django.db.models.expressions import Func
from django.db.models.functions.mixins import FixDurationInputMixin, NumericOutputFieldMixin

"""
Classes to represent the definitions of aggregate functions.
"""
__all__ = ['Aggregate', 'Avg', 'Count', 'Max', 'Min', 'StdDev', 'Sum', 'Variance']
class Aggregate(Func):
    template = ...
    contains_aggregate = ...
    name = ...
    filter_template = ...
    window_compatible = ...
    allow_distinct = ...
    empty_result_set_value = ...
    def __init__(self, *expressions, distinct=..., filter=..., default=..., **extra) -> None:
        ...
    
    def get_source_fields(self): # -> list[Unknown | cached_property]:
        ...
    
    def get_source_expressions(self): # -> list[Unknown | F | Value]:
        ...
    
    def set_source_expressions(self, exprs): # -> None:
        ...
    
    def resolve_expression(self, query=..., allow_joins=..., reuse=..., summarize=..., for_save=...):
        ...
    
    @property
    def default_alias(self): # -> str:
        ...
    
    def get_group_by_cols(self, alias=...): # -> list[Unknown]:
        ...
    
    def as_sql(self, compiler, connection, **extra_context): # -> tuple[Unknown | str, Unknown] | tuple[Unknown, list[Unknown]]:
        ...
    


class Avg(FixDurationInputMixin, NumericOutputFieldMixin, Aggregate):
    function = ...
    name = ...
    allow_distinct = ...


class Count(Aggregate):
    function = ...
    name = ...
    output_field = ...
    allow_distinct = ...
    empty_result_set_value = ...
    def __init__(self, expression, filter=..., **extra) -> None:
        ...
    


class Max(Aggregate):
    function = ...
    name = ...


class Min(Aggregate):
    function = ...
    name = ...


class StdDev(NumericOutputFieldMixin, Aggregate):
    name = ...
    def __init__(self, expression, sample=..., **extra) -> None:
        ...
    


class Sum(FixDurationInputMixin, Aggregate):
    function = ...
    name = ...
    allow_distinct = ...


class Variance(NumericOutputFieldMixin, Aggregate):
    name = ...
    def __init__(self, expression, sample=..., **extra) -> None:
        ...
    

