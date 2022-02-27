"""
This type stub file was generated by pyright.
"""

from .. import Tags, register

CROSS_ORIGIN_OPENER_POLICY_VALUES = ...
REFERRER_POLICY_VALUES = ...
SECRET_KEY_INSECURE_PREFIX = ...
SECRET_KEY_MIN_LENGTH = ...
SECRET_KEY_MIN_UNIQUE_CHARACTERS = ...
W001 = ...
W002 = ...
W004 = ...
W005 = ...
W006 = ...
W008 = ...
W009 = ...
W018 = ...
W019 = ...
W020 = ...
W021 = ...
W022 = ...
E023 = ...
E024 = ...
@register(Tags.security, deploy=True)
def check_security_middleware(app_configs, **kwargs): # -> list[Warning]:
    ...

@register(Tags.security, deploy=True)
def check_xframe_options_middleware(app_configs, **kwargs): # -> list[Warning]:
    ...

@register(Tags.security, deploy=True)
def check_sts(app_configs, **kwargs): # -> list[Warning]:
    ...

@register(Tags.security, deploy=True)
def check_sts_include_subdomains(app_configs, **kwargs): # -> list[Warning]:
    ...

@register(Tags.security, deploy=True)
def check_sts_preload(app_configs, **kwargs): # -> list[Warning]:
    ...

@register(Tags.security, deploy=True)
def check_content_type_nosniff(app_configs, **kwargs): # -> list[Warning]:
    ...

@register(Tags.security, deploy=True)
def check_ssl_redirect(app_configs, **kwargs): # -> list[Warning]:
    ...

@register(Tags.security, deploy=True)
def check_secret_key(app_configs, **kwargs): # -> list[Warning]:
    ...

@register(Tags.security, deploy=True)
def check_debug(app_configs, **kwargs): # -> list[Warning]:
    ...

@register(Tags.security, deploy=True)
def check_xframe_deny(app_configs, **kwargs): # -> list[Warning]:
    ...

@register(Tags.security, deploy=True)
def check_allowed_hosts(app_configs, **kwargs): # -> list[Warning]:
    ...

@register(Tags.security, deploy=True)
def check_referrer_policy(app_configs, **kwargs): # -> list[Warning] | list[Error]:
    ...

@register(Tags.security, deploy=True)
def check_cross_origin_opener_policy(app_configs, **kwargs): # -> list[Error]:
    ...

