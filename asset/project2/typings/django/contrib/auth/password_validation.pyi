"""
This type stub file was generated by pyright.
"""

import functools
from django.utils.functional import cached_property

@functools.lru_cache(maxsize=None)
def get_default_password_validators(): # -> list[Unknown]:
    ...

def get_password_validators(validator_config): # -> list[Unknown]:
    ...

def validate_password(password, user=..., password_validators=...):
    """
    Validate whether the password meets all validator requirements.

    If the password is valid, return ``None``.
    If the password is invalid, raise ValidationError with all error messages.
    """
    ...

def password_changed(password, user=..., password_validators=...): # -> None:
    """
    Inform all validators that have implemented a password_changed() method
    that the password has been changed.
    """
    ...

def password_validators_help_texts(password_validators=...): # -> list[Unknown]:
    """
    Return a list of all help texts of all configured validators.
    """
    ...

password_validators_help_text_html = ...
class MinimumLengthValidator:
    """
    Validate whether the password is of a minimum length.
    """
    def __init__(self, min_length=...) -> None:
        ...
    
    def validate(self, password, user=...): # -> None:
        ...
    
    def get_help_text(self): # -> Any:
        ...
    


def exceeds_maximum_length_ratio(password, max_similarity, value): # -> Literal[False]:
    """
    Test that value is within a reasonable range of password.

    The following ratio calculations are based on testing SequenceMatcher like
    this:

    for i in range(0,6):
      print(10**i, SequenceMatcher(a='A', b='A'*(10**i)).quick_ratio())

    which yields:

    1 1.0
    10 0.18181818181818182
    100 0.019801980198019802
    1000 0.001998001998001998
    10000 0.00019998000199980003
    100000 1.999980000199998e-05

    This means a length_ratio of 10 should never yield a similarity higher than
    0.2, for 100 this is down to 0.02 and for 1000 it is 0.002. This can be
    calculated via 2 / length_ratio. As a result we avoid the potentially
    expensive sequence matching.
    """
    ...

class UserAttributeSimilarityValidator:
    """
    Validate whether the password is sufficiently different from the user's
    attributes.

    If no specific attributes are provided, look at a sensible list of
    defaults. Attributes that don't exist are ignored. Comparison is made to
    not only the full attribute value, but also its components, so that, for
    example, a password is validated against either part of an email address,
    as well as the full address.
    """
    DEFAULT_USER_ATTRIBUTES = ...
    def __init__(self, user_attributes=..., max_similarity=...) -> None:
        ...
    
    def validate(self, password, user=...):
        ...
    
    def get_help_text(self): # -> Any:
        ...
    


class CommonPasswordValidator:
    """
    Validate whether the password is a common password.

    The password is rejected if it occurs in a provided list of passwords,
    which may be gzipped. The list Django ships with contains 20000 common
    passwords (lowercased and deduplicated), created by Royce Williams:
    https://gist.github.com/roycewilliams/281ce539915a947a23db17137d91aeb7
    The password list must be lowercased to match the comparison in validate().
    """
    @cached_property
    def DEFAULT_PASSWORD_LIST_PATH(self): # -> Path:
        ...
    
    def __init__(self, password_list_path=...) -> None:
        ...
    
    def validate(self, password, user=...): # -> None:
        ...
    
    def get_help_text(self): # -> Any:
        ...
    


class NumericPasswordValidator:
    """
    Validate whether the password is alphanumeric.
    """
    def validate(self, password, user=...): # -> None:
        ...
    
    def get_help_text(self): # -> Any:
        ...
    

