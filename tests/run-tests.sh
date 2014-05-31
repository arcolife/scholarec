#!/bin/sh

python ./scholarec/base/arxiv.py
python ./scholarec/base/operations.py
python ./scholarec/handlers/datahandler.py
python ./scholarec/__init__.py
python ./tests/test.py
