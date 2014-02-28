#!/bin/sh

python ./scholarec/Base/DocumentClass.py
grep '<entry>' ./log/output/query_results.xml | wc -l
