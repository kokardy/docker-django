#!/bin/bash

f=$(python -c "import django; print(django.__file__)")


d1=$(dirname "$f")

d2=$d1/contrib/admin/static/admin

echo COPY
echo origin:$d1
echo dest:$d2

cp -r $d2 /usr/share/nginx/html/
