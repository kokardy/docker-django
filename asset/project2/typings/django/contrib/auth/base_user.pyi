"""
This type stub file was generated by pyright.
"""

from django.db import models

"""
This module allows importing AbstractBaseUser even when django.contrib.auth is
not in INSTALLED_APPS.
"""
class BaseUserManager(models.Manager):
    @classmethod
    def normalize_email(cls, email): # -> str:
        """
        Normalize the email address by lowercasing the domain part of it.
        """
        ...
    
    def make_random_password(self, length=..., allowed_chars=...): # -> str:
        """
        Generate a random password with the given length and given
        allowed_chars. The default value of allowed_chars does not have "I" or
        "O" or letters and digits that look similar -- just to avoid confusion.
        """
        ...
    
    def get_by_natural_key(self, username):
        ...
    


class AbstractBaseUser(models.Model):
    password = ...
    last_login = ...
    is_active = ...
    REQUIRED_FIELDS = ...
    _password = ...
    class Meta:
        abstract = ...
    
    
    def __str__(self) -> str:
        ...
    
    def save(self, *args, **kwargs): # -> None:
        ...
    
    def get_username(self): # -> Any:
        """Return the username for this User."""
        ...
    
    def clean(self): # -> None:
        ...
    
    def natural_key(self): # -> tuple[Any]:
        ...
    
    @property
    def is_anonymous(self): # -> Literal[False]:
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        ...
    
    @property
    def is_authenticated(self): # -> Literal[True]:
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        ...
    
    def set_password(self, raw_password): # -> None:
        ...
    
    def check_password(self, raw_password): # -> Literal[False]:
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        ...
    
    def set_unusable_password(self): # -> None:
        ...
    
    def has_usable_password(self): # -> bool:
        """
        Return False if set_unusable_password() has been called for this user.
        """
        ...
    
    def get_session_auth_hash(self): # -> str:
        """
        Return an HMAC of the password field.
        """
        ...
    
    @classmethod
    def get_email_field_name(cls): # -> Literal['email']:
        ...
    
    @classmethod
    def normalize_username(cls, username): # -> str:
        ...
    


