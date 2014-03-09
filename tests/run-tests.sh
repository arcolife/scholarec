#!/bin/sh

grep '<entry>' ./log/output/query_results.xml | wc -l
sudo python setup.py test
python ./scholarec/Base/DocumentClass.py
python ./scholarec/__init__.py
