"""
This type stub file was generated by pyright.
"""

import functools

DEBUG_ENGINE = ...
def builtin_template_path(name):
    """
    Return a path to a builtin template.

    Avoid calling this function at the module level or in a class-definition
    because __file__ may not exist, e.g. in frozen environments.
    """
    ...

class ExceptionCycleWarning(UserWarning):
    ...


class CallableSettingWrapper:
    """
    Object to wrap callable appearing in settings.
    * Not to call in the debug page (#21345).
    * Not to break the debug page if the callable forbidding to set attributes
      (#23070).
    """
    def __init__(self, callable_setting) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    


def technical_500_response(request, exc_type, exc_value, tb, status_code=...): # -> HttpResponse:
    """
    Create a technical server error response. The last three arguments are
    the values returned from sys.exc_info() and friends.
    """
    ...

@functools.lru_cache()
def get_default_exception_reporter_filter(): # -> Any:
    ...

def get_exception_reporter_filter(request): # -> Any | None:
    ...

def get_exception_reporter_class(request): # -> Any | None:
    ...

class SafeExceptionReporterFilter:
    """
    Use annotations made by the sensitive_post_parameters and
    sensitive_variables decorators to filter out sensitive information.
    """
    cleansed_substitute = ...
    hidden_settings = ...
    def cleanse_setting(self, key, value):
        """
        Cleanse an individual setting key/value of sensitive content. If the
        value is a dictionary, recursively cleanse the keys in that dictionary.
        """
        ...
    
    def get_safe_settings(self): # -> dict[Unknown, Unknown]:
        """
        Return a dictionary of the settings module with values of sensitive
        settings replaced with stars (*********).
        """
        ...
    
    def get_safe_request_meta(self, request): # -> dict[Unknown, Unknown]:
        """
        Return a dictionary of request.META with sensitive values redacted.
        """
        ...
    
    def is_active(self, request): # -> bool:
        """
        This filter is to add safety in production environments (i.e. DEBUG
        is False). If DEBUG is True then your site is not safe anyway.
        This hook is provided as a convenience to easily activate or
        deactivate the filter on a per request basis.
        """
        ...
    
    def get_cleansed_multivaluedict(self, request, multivaluedict):
        """
        Replace the keys in a MultiValueDict marked as sensitive with stars.
        This mitigates leaking sensitive POST parameters if something like
        request.POST['nonexistent_key'] throws an exception (#21098).
        """
        ...
    
    def get_post_parameters(self, request): # -> dict[Unknown, Unknown]:
        """
        Replace the values of POST parameters marked as sensitive with
        stars (*********).
        """
        ...
    
    def cleanse_special_types(self, request, value): # -> str | MultiValueDict:
        ...
    
    def get_traceback_frame_variables(self, request, tb_frame):
        """
        Replace the values of variables marked as sensitive with
        stars (*********).
        """
        ...
    


class ExceptionReporter:
    """Organize and coordinate reporting on exceptions."""
    @property
    def html_template_path(self): # -> Path:
        ...
    
    @property
    def text_template_path(self): # -> Path:
        ...
    
    def __init__(self, request, exc_type, exc_value, tb, is_email=...) -> None:
        ...
    
    def get_traceback_data(self): # -> dict[str, Unknown]:
        """Return a dictionary containing traceback information."""
        ...
    
    def get_traceback_html(self):
        """Return HTML version of debug 500 HTTP error page."""
        ...
    
    def get_traceback_text(self):
        """Return plain text version of debug 500 HTTP error page."""
        ...
    
    def get_traceback_frames(self): # -> list[Unknown]:
        ...
    
    def get_exception_traceback_frames(self, exc_value, tb): # -> Generator[dict[str, Unknown], None, None]:
        ...
    


def technical_404_response(request, exception):
    """Create a technical 404 error response. `exception` is the Http404."""
    ...

def default_urlconf(request): # -> HttpResponse:
    """Create an empty URLconf 404 error response."""
    ...
