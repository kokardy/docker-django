"""
This type stub file was generated by pyright.
"""

from collections import UserList

"""
This type stub file was generated by pyright.
"""
def pretty_name(name):
    """Convert 'first_name' to 'First name'."""
    ...

def flatatt(attrs):
    """
    Convert a dictionary of attributes to a single string.
    The returned string will contain a leading space followed by key="value",
    XML-style pairs. In the case of a boolean value, the key will appear
    without a value. It is assumed that the keys do not need to be
    XML-escaped. If the passed dictionary is empty, then return an empty
    string.

    The result is passed through 'mark_safe' (by way of 'format_html_join').
    """
    ...

class RenderableMixin:
    def get_context(self):
        ...
    
    def render(self, template_name=..., context=..., renderer=...):
        ...
    
    __str__ = ...
    __html__ = ...


class RenderableFormMixin(RenderableMixin):
    def as_p(self):
        """Render as <p> elements."""
        ...
    
    def as_table(self):
        """Render as <tr> elements excluding the surrounding <table> tag."""
        ...
    
    def as_ul(self):
        """Render as <li> elements excluding the surrounding <ul> tag."""
        ...
    


class RenderableErrorMixin(RenderableMixin):
    def as_json(self, escape_html=...):
        ...
    
    def as_text(self):
        ...
    
    def as_ul(self):
        ...
    


class ErrorDict(dict, RenderableErrorMixin):
    """
    A collection of errors that knows how to display itself in various formats.

    The dictionary keys are the field names, and the values are the errors.
    """
    template_name = ...
    template_name_text = ...
    template_name_ul = ...
    def __init__(self, *args, renderer=..., **kwargs) -> None:
        ...
    
    def as_data(self):
        ...
    
    def get_json_data(self, escape_html=...):
        ...
    
    def get_context(self):
        ...
    


class ErrorList(UserList, list, RenderableErrorMixin):
    """
    A collection of errors that knows how to display itself in various formats.
    """
    template_name = ...
    template_name_text = ...
    template_name_ul = ...
    def __init__(self, initlist=..., error_class=..., renderer=...) -> None:
        ...
    
    def as_data(self):
        ...
    
    def copy(self):
        ...
    
    def get_json_data(self, escape_html=...):
        ...
    
    def get_context(self):
        ...
    
    def __repr__(self):
        ...
    
    def __contains__(self, item):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __getitem__(self, i):
        ...
    
    def __reduce_ex__(self, *args, **kwargs):
        ...
    


def from_current_timezone(value):
    """
    When time zone support is enabled, convert naive datetimes
    entered in the current time zone to aware datetimes.
    """
    ...

def to_current_timezone(value):
    """
    When time zone support is enabled, convert aware datetimes
    to naive datetimes in the current time zone for display.
    """
    ...
