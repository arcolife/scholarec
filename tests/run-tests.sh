#!/bin/sh

grep '<entry>' ./log/output/query_results.xml | wc -l
python ./scholarec/__init__.py
python ./scholarec/Base/DocumentClass.py
