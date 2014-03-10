#!/bin/sh

/usr/bin/python ./scholarec/Base/DocumentClass.py
echo "Tested ./scholarec/Base/DocumentClass.py"
/usr/bin/python ./scholarec/Base/DocumentData.py
echo "Tested ./scholarec/Base/DocumentData.py"
/usr/bin/python ./scholarec/__init__.py
echo "Tested ./scholarec/__init__.py"
/usr/bin/python ./tests/test.py
echo "Tested ./tests/test.py"
