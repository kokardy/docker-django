"""
This type stub file was generated by pyright.
"""

import functools
from django.core.signals import setting_changed
from django.dispatch import receiver

UNUSABLE_PASSWORD_PREFIX = ...
UNUSABLE_PASSWORD_SUFFIX_LENGTH = ...
def is_password_usable(encoded): # -> bool:
    """
    Return True if this password wasn't generated by
    User.set_unusable_password(), i.e. make_password(None).
    """
    ...

def check_password(password, encoded, setter=..., preferred=...):
    """
    Return a boolean of whether the raw password matches the three
    part encoded digest.

    If setter is specified, it'll be called when you need to
    regenerate the password.
    """
    ...

def make_password(password, salt=..., hasher=...): # -> str | bytes:
    """
    Turn a plain-text password into a hash for database storage

    Same as encode() but generate a new random salt. If password is None then
    return a concatenation of UNUSABLE_PASSWORD_PREFIX and a random string,
    which disallows logins. Additional random string reduces chances of gaining
    access to staff or superuser accounts. See ticket #20079 for more info.
    """
    ...

@functools.lru_cache()
def get_hashers(): # -> list[Unknown]:
    ...

@functools.lru_cache()
def get_hashers_by_algorithm(): # -> dict[Unknown, Unknown]:
    ...

@receiver(setting_changed)
def reset_hashers(**kwargs): # -> None:
    ...

def get_hasher(algorithm=...): # -> str:
    """
    Return an instance of a loaded password hasher.

    If algorithm is 'default', return the default hasher. Lazily import hashers
    specified in the project's settings file if needed.
    """
    ...

def identify_hasher(encoded): # -> str:
    """
    Return an instance of a loaded password hasher.

    Identify hasher algorithm by examining encoded hash, and call
    get_hasher() to return hasher. Raise ValueError if
    algorithm cannot be identified, or if hasher is not loaded.
    """
    ...

def mask_hash(hash, show=..., char=...):
    """
    Return the given hash, with only the first ``show`` number shown. The
    rest are masked with ``char`` for security reasons.
    """
    ...

def must_update_salt(salt, expected_entropy):
    ...

class BasePasswordHasher:
    """
    Abstract base class for password hashers

    When creating your own hasher, you need to override algorithm,
    verify(), encode() and safe_summary().

    PasswordHasher objects are immutable.
    """
    algorithm = ...
    library = ...
    salt_entropy = ...
    def salt(self): # -> str:
        """
        Generate a cryptographically secure nonce salt in ASCII with an entropy
        of at least `salt_entropy` bits.
        """
        ...
    
    def verify(self, password, encoded):
        """Check if the given password is correct."""
        ...
    
    def encode(self, password, salt):
        """
        Create an encoded database value.

        The result is normally formatted as "algorithm$salt$hash" and
        must be fewer than 128 characters.
        """
        ...
    
    def decode(self, encoded):
        """
        Return a decoded database value.

        The result is a dictionary and should contain `algorithm`, `hash`, and
        `salt`. Extra keys can be algorithm specific like `iterations` or
        `work_factor`.
        """
        ...
    
    def safe_summary(self, encoded):
        """
        Return a summary of safe values.

        The result is a dictionary and will be used where the password field
        must be displayed to construct a safe representation of the password.
        """
        ...
    
    def must_update(self, encoded): # -> Literal[False]:
        ...
    
    def harden_runtime(self, password, encoded): # -> None:
        """
        Bridge the runtime gap between the work factor supplied in `encoded`
        and the work factor suggested by this hasher.

        Taking PBKDF2 as an example, if `encoded` contains 20000 iterations and
        `self.iterations` is 30000, this method should run password through
        another 10000 iterations of PBKDF2. Similar approaches should exist
        for any hasher that has a work factor. If not, this method should be
        defined as a no-op to silence the warning.
        """
        ...
    


class PBKDF2PasswordHasher(BasePasswordHasher):
    """
    Secure password hashing using the PBKDF2 algorithm (recommended)

    Configured to use PBKDF2 + HMAC + SHA256.
    The result is a 64 byte binary string.  Iterations may be changed
    safely but you must rename the algorithm if you change SHA256.
    """
    algorithm = ...
    iterations = ...
    digest = ...
    def encode(self, password, salt, iterations=...): # -> str:
        ...
    
    def decode(self, encoded): # -> dict[str, Unknown]:
        ...
    
    def verify(self, password, encoded): # -> bool:
        ...
    
    def safe_summary(self, encoded): # -> dict[Any, Unknown]:
        ...
    
    def must_update(self, encoded): # -> bool:
        ...
    
    def harden_runtime(self, password, encoded): # -> None:
        ...
    


class PBKDF2SHA1PasswordHasher(PBKDF2PasswordHasher):
    """
    Alternate PBKDF2 hasher which uses SHA1, the default PRF
    recommended by PKCS #5. This is compatible with other
    implementations of PBKDF2, such as openssl's
    PKCS5_PBKDF2_HMAC_SHA1().
    """
    algorithm = ...
    digest = ...


class Argon2PasswordHasher(BasePasswordHasher):
    """
    Secure password hashing using the argon2 algorithm.

    This is the winner of the Password Hashing Competition 2013-2015
    (https://password-hashing.net). It requires the argon2-cffi library which
    depends on native C code and might cause portability issues.
    """
    algorithm = ...
    library = ...
    time_cost = ...
    memory_cost = ...
    parallelism = ...
    def encode(self, password, salt): # -> Any:
        ...
    
    def decode(self, encoded): # -> dict[str, Unknown]:
        ...
    
    def verify(self, password, encoded): # -> Any | Literal[False]:
        ...
    
    def safe_summary(self, encoded): # -> dict[Any, Unknown]:
        ...
    
    def must_update(self, encoded): # -> bool:
        ...
    
    def harden_runtime(self, password, encoded): # -> None:
        ...
    
    def params(self): # -> Any:
        ...
    


class BCryptSHA256PasswordHasher(BasePasswordHasher):
    """
    Secure password hashing using the bcrypt algorithm (recommended)

    This is considered by many to be the most secure algorithm but you
    must first install the bcrypt library.  Please be warned that
    this library depends on native C code and might cause portability
    issues.
    """
    algorithm = ...
    digest = ...
    library = ...
    rounds = ...
    def salt(self): # -> Any:
        ...
    
    def encode(self, password, salt): # -> str:
        ...
    
    def decode(self, encoded): # -> dict[str, Unknown]:
        ...
    
    def verify(self, password, encoded): # -> bool:
        ...
    
    def safe_summary(self, encoded): # -> dict[Any, Unknown]:
        ...
    
    def must_update(self, encoded):
        ...
    
    def harden_runtime(self, password, encoded): # -> None:
        ...
    


class BCryptPasswordHasher(BCryptSHA256PasswordHasher):
    """
    Secure password hashing using the bcrypt algorithm

    This is considered by many to be the most secure algorithm but you
    must first install the bcrypt library.  Please be warned that
    this library depends on native C code and might cause portability
    issues.

    This hasher does not first hash the password which means it is subject to
    bcrypt's 72 bytes password truncation. Most use cases should prefer the
    BCryptSHA256PasswordHasher.
    """
    algorithm = ...
    digest = ...


class ScryptPasswordHasher(BasePasswordHasher):
    """
    Secure password hashing using the Scrypt algorithm.
    """
    algorithm = ...
    block_size = ...
    maxmem = ...
    parallelism = ...
    work_factor = ...
    def encode(self, password, salt, n=..., r=..., p=...): # -> str:
        ...
    
    def decode(self, encoded): # -> dict[str, Unknown]:
        ...
    
    def verify(self, password, encoded): # -> bool:
        ...
    
    def safe_summary(self, encoded): # -> dict[Any, Unknown]:
        ...
    
    def must_update(self, encoded):
        ...
    
    def harden_runtime(self, password, encoded): # -> None:
        ...
    


class SHA1PasswordHasher(BasePasswordHasher):
    """
    The SHA1 password hashing algorithm (not recommended)
    """
    algorithm = ...
    def encode(self, password, salt): # -> str:
        ...
    
    def decode(self, encoded): # -> dict[str, Unknown]:
        ...
    
    def verify(self, password, encoded): # -> bool:
        ...
    
    def safe_summary(self, encoded): # -> dict[Any, Unknown]:
        ...
    
    def must_update(self, encoded): # -> bool:
        ...
    
    def harden_runtime(self, password, encoded): # -> None:
        ...
    


class MD5PasswordHasher(BasePasswordHasher):
    """
    The Salted MD5 password hashing algorithm (not recommended)
    """
    algorithm = ...
    def encode(self, password, salt): # -> str:
        ...
    
    def decode(self, encoded): # -> dict[str, Unknown]:
        ...
    
    def verify(self, password, encoded): # -> bool:
        ...
    
    def safe_summary(self, encoded): # -> dict[Any, Unknown]:
        ...
    
    def must_update(self, encoded): # -> bool:
        ...
    
    def harden_runtime(self, password, encoded): # -> None:
        ...
    


class UnsaltedSHA1PasswordHasher(BasePasswordHasher):
    """
    Very insecure algorithm that you should *never* use; store SHA1 hashes
    with an empty salt.

    This class is implemented because Django used to accept such password
    hashes. Some older Django installs still have these values lingering
    around so we need to handle and upgrade them properly.
    """
    algorithm = ...
    def salt(self): # -> Literal['']:
        ...
    
    def encode(self, password, salt): # -> str:
        ...
    
    def decode(self, encoded): # -> dict[str, Unknown]:
        ...
    
    def verify(self, password, encoded): # -> bool:
        ...
    
    def safe_summary(self, encoded): # -> dict[Any, Unknown]:
        ...
    
    def harden_runtime(self, password, encoded): # -> None:
        ...
    


class UnsaltedMD5PasswordHasher(BasePasswordHasher):
    """
    Incredibly insecure algorithm that you should *never* use; stores unsalted
    MD5 hashes without the algorithm prefix, also accepts MD5 hashes with an
    empty salt.

    This class is implemented because Django used to store passwords this way
    and to accept such password hashes. Some older Django installs still have
    these values lingering around so we need to handle and upgrade them
    properly.
    """
    algorithm = ...
    def salt(self): # -> Literal['']:
        ...
    
    def encode(self, password, salt): # -> str:
        ...
    
    def decode(self, encoded): # -> dict[str, Unknown]:
        ...
    
    def verify(self, password, encoded): # -> bool:
        ...
    
    def safe_summary(self, encoded): # -> dict[Any, Unknown]:
        ...
    
    def harden_runtime(self, password, encoded): # -> None:
        ...
    


class CryptPasswordHasher(BasePasswordHasher):
    """
    Password hashing using UNIX crypt (not recommended)

    The crypt module is not supported on all platforms.
    """
    algorithm = ...
    library = ...
    def salt(self): # -> str:
        ...
    
    def encode(self, password, salt): # -> str:
        ...
    
    def decode(self, encoded): # -> dict[str, Unknown]:
        ...
    
    def verify(self, password, encoded): # -> bool:
        ...
    
    def safe_summary(self, encoded): # -> dict[Any, Unknown]:
        ...
    
    def harden_runtime(self, password, encoded): # -> None:
        ...
    


