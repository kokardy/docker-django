#!/usr/bin/env python
import os.path
import sys

from django.core.management.utils import get_random_secret_key

def main():
    project_name = "pro1"
    if len(sys.argv) > 1:
        project_name = sys.argv[1]

    SECRET_KEY = get_random_secret_key()
    ofile = os.path.join(os.path.dirname(__file__), project_name, "secret_key.py")

    is_exists = os.path.exists(ofile)

    with open(ofile, "w") as f:
        def_secret_key = f"SECRET_KEY = '{SECRET_KEY}'"
        f.writelines(def_secret_key)

if __name__ == "__main__":
    main()


