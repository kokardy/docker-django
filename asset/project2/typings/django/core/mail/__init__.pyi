"""
This type stub file was generated by pyright.
"""

from django.conf import settings
from django.core.mail.message import BadHeaderError, DEFAULT_ATTACHMENT_MIME_TYPE, EmailMessage, EmailMultiAlternatives, SafeMIMEMultipart, SafeMIMEText, forbid_multi_line_headers, make_msgid
from django.core.mail.utils import CachedDnsName, DNS_NAME
from django.utils.module_loading import import_string

"""
Tools for sending email.
"""
__all__ = ['CachedDnsName', 'DNS_NAME', 'EmailMessage', 'EmailMultiAlternatives', 'SafeMIMEText', 'SafeMIMEMultipart', 'DEFAULT_ATTACHMENT_MIME_TYPE', 'make_msgid', 'BadHeaderError', 'forbid_multi_line_headers', 'get_connection', 'send_mail', 'send_mass_mail', 'mail_admins', 'mail_managers']
def get_connection(backend=..., fail_silently=..., **kwds): # -> Any:
    """Load an email backend and return an instance of it.

    If backend is None (default), use settings.EMAIL_BACKEND.

    Both fail_silently and other keyword arguments are used in the
    constructor of the backend.
    """
    ...

def send_mail(subject, message, from_email, recipient_list, fail_silently=..., auth_user=..., auth_password=..., connection=..., html_message=...): # -> Any | Literal[0]:
    """
    Easy wrapper for sending a single message to a recipient list. All members
    of the recipient list will see the other recipients in the 'To' field.

    If from_email is None, use the DEFAULT_FROM_EMAIL setting.
    If auth_user is None, use the EMAIL_HOST_USER setting.
    If auth_password is None, use the EMAIL_HOST_PASSWORD setting.

    Note: The API for this method is frozen. New code wanting to extend the
    functionality should use the EmailMessage class directly.
    """
    ...

def send_mass_mail(datatuple, fail_silently=..., auth_user=..., auth_password=..., connection=...): # -> Any:
    """
    Given a datatuple of (subject, message, from_email, recipient_list), send
    each message to each recipient list. Return the number of emails sent.

    If from_email is None, use the DEFAULT_FROM_EMAIL setting.
    If auth_user and auth_password are set, use them to log in.
    If auth_user is None, use the EMAIL_HOST_USER setting.
    If auth_password is None, use the EMAIL_HOST_PASSWORD setting.

    Note: The API for this method is frozen. New code wanting to extend the
    functionality should use the EmailMessage class directly.
    """
    ...

def mail_admins(subject, message, fail_silently=..., connection=..., html_message=...): # -> None:
    """Send a message to the admins, as defined by the ADMINS setting."""
    ...

def mail_managers(subject, message, fail_silently=..., connection=..., html_message=...): # -> None:
    """Send a message to the managers, as defined by the MANAGERS setting."""
    ...
