"""
This type stub file was generated by pyright.
"""

from django.db.models.expressions import Func
from django.db.models.lookups import Transform

class TimezoneMixin:
    tzinfo = ...
    def get_tzname(self): # -> Any | str | None:
        ...
    


class Extract(TimezoneMixin, Transform):
    lookup_name = ...
    output_field = ...
    def __init__(self, expression, lookup_name=..., tzinfo=..., **extra) -> None:
        ...
    
    def as_sql(self, compiler, connection): # -> tuple[Unknown, Unknown]:
        ...
    
    def resolve_expression(self, query=..., allow_joins=..., reuse=..., summarize=..., for_save=...): # -> Func:
        ...
    


class ExtractYear(Extract):
    lookup_name = ...


class ExtractIsoYear(Extract):
    """Return the ISO-8601 week-numbering year."""
    lookup_name = ...


class ExtractMonth(Extract):
    lookup_name = ...


class ExtractDay(Extract):
    lookup_name = ...


class ExtractWeek(Extract):
    """
    Return 1-52 or 53, based on ISO-8601, i.e., Monday is the first of the
    week.
    """
    lookup_name = ...


class ExtractWeekDay(Extract):
    """
    Return Sunday=1 through Saturday=7.

    To replicate this in Python: (mydatetime.isoweekday() % 7) + 1
    """
    lookup_name = ...


class ExtractIsoWeekDay(Extract):
    """Return Monday=1 through Sunday=7, based on ISO-8601."""
    lookup_name = ...


class ExtractQuarter(Extract):
    lookup_name = ...


class ExtractHour(Extract):
    lookup_name = ...


class ExtractMinute(Extract):
    lookup_name = ...


class ExtractSecond(Extract):
    lookup_name = ...


class Now(Func):
    template = ...
    output_field = ...
    def as_postgresql(self, compiler, connection, **extra_context): # -> tuple[Unknown | str, list[Unknown]]:
        ...
    


class TruncBase(TimezoneMixin, Transform):
    kind = ...
    tzinfo = ...
    def __init__(self, expression, output_field=..., tzinfo=..., is_dst=..., **extra) -> None:
        ...
    
    def as_sql(self, compiler, connection): # -> tuple[Unknown, Unknown]:
        ...
    
    def resolve_expression(self, query=..., allow_joins=..., reuse=..., summarize=..., for_save=...):
        ...
    
    def convert_value(self, value, expression, connection): # -> Any | datetime | _date | _time:
        ...
    


class Trunc(TruncBase):
    def __init__(self, expression, kind, output_field=..., tzinfo=..., is_dst=..., **extra) -> None:
        ...
    


class TruncYear(TruncBase):
    kind = ...


class TruncQuarter(TruncBase):
    kind = ...


class TruncMonth(TruncBase):
    kind = ...


class TruncWeek(TruncBase):
    """Truncate to midnight on the Monday of the week."""
    kind = ...


class TruncDay(TruncBase):
    kind = ...


class TruncDate(TruncBase):
    kind = ...
    lookup_name = ...
    output_field = ...
    def as_sql(self, compiler, connection): # -> tuple[Unknown, Unknown]:
        ...
    


class TruncTime(TruncBase):
    kind = ...
    lookup_name = ...
    output_field = ...
    def as_sql(self, compiler, connection): # -> tuple[Unknown, Unknown]:
        ...
    


class TruncHour(TruncBase):
    kind = ...


class TruncMinute(TruncBase):
    kind = ...


class TruncSecond(TruncBase):
    kind = ...


