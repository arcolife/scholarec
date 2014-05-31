# -*- coding: utf-8 -*- 

## This file is part of ScholaRec.
## A recommendation engine for Scholarly works.
## Copyright (C) 2014  Archit Sharma <archit.py@gmail.com>
##
## ScholaRec is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## ScholaRec is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>

""" This script parses the respective data structures, 
passed to the object of Document Class."""

## import general modules
import os
import feedparser

import urllib
import json
import pprint

## import dependencies
from pyes import *
#import requests

class DocumentUpload(object):
    """
    upload data to ElasticSearch instance.
    """
    def __init__(self, query_dsl, host, port):
        self.query_dsl = query_dsl
        self.host = host
        self.port = port

    def query_map(self):
        pass

    def query_status(self):
        pass

    def foo(self):
        pass

class DocumentQuery(object):
    """
    Run different queries on the data 
    already present on ElasticSearch instance.
    """
    def __init__(self, query_dsl, host, port):
        self.query_dsl = query_dsl
        self.host = host
        self.port = port

    def delete(self):
        pass

    def modify(self):
        pass

    def build(self, search_term):
        q = { "query":{
            "bool":{
                "must":[{
                    "query_string":{
                        "default_field":"_all",
                        "query":search_term
                    }
                }],
                "must_not":[],
                "should":[]
            }},
              "from":0,
              "size":10,
              "sort":[],
              "facets":{}
          }
        return q

    def search(self, query, **kwargs):
        #query = build_query(str(query))
        #query = json.dumps(query)
        kwargs['q'] = query
        args = kwargs.keys()
        if 'search_size' in args:
            kwargs['size'] = kwargs.pop('search_size')
        else:
            kwargs['size'] = 10
        if 'search_from' in args:
            kwargs['from'] = kwargs.pop('search_from')
        else:
            kwargs['from'] = 0
        #query = '?q='+query+'&'
        query = urllib.urlencode(kwargs)
        #for key, value in kwargs.items():
        #    query+=key+'='+str(value)+'&'
        response = urllib.urlopen(
            'http://127.0.0.1:9200/arxiv/docs/_search?' + query
        )
        result = json.loads( response.read() )
        #pprint.pprint(result['hits']['hits'])
        #JE = json.encoder.JSONEncoder()
        #return JE.encode(result)
        return result

