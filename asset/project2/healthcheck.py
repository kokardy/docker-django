#!/usr/bin/env python
import requests
import http


def main():
    ok = False
    with requests.get("http://localhost:8000/hc") as res:
        if res.status_code == http.HTTPStatus.OK:
            ok = True

    if ok:
        exit(0)
    exit(1)


if __name__ == "__main__":
    main()
