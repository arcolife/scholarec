#!/usr/bin/env python
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

""" This module queries the arxiv API after every 3 sec 
and  curates the results in JSON format """

## import general modules
import os
import sys
from urllib2 import \
    urlopen
import json
from pprint import \
    pprint, pformat
import time

## Import dependencies specific to scholarec
import wikipedia
from scholarec.Base.DocumentClass import DocumentArXiv
SOURCE_PATH = os.path.dirname(os.path.abspath(__file__))

class QueryParse:
    ''' mathods to parse query '''    
    def __init__(self, query_xml, keyword_list):
        self.query_xml = query_xml
        self.entry_count = None
        self.data_dict = None
        self.keywords = keyword_list
        self.doc = None
        self.data_json = None

    def parse_data(self):
        """ parse extracted data into python dict format """
        self.doc = DocumentArXiv(self.query_xml)
        #self.data_xml, self.data_dict = Doc.extract_data()
        self.data_dict = self.doc.extract_tags()
        self.entry_count = len(self.data_dict.keys())
        if self.entry_count:
            print "Total Entries: ", self.entry_count
        else:
            sys.exit("\nNo matching entries found!")

    def store_data(self):
        """ write response to enternal file """
        # write to JSON
        self.data_json = json.JSONEncoder().encode(self.data_dict)
        f_json = open( SOURCE_PATH + '/query_results' + self.keywords + '.json','wb')
        f_json.write(self.data_json)
        f_json.close()

if __name__ == '__main__':    
    f = open('searchWords.lst','rb')
    import ast
    search_words = ast.literal_eval(f.read())
    f.close()
    
    BASE_URL = "http://export.arxiv.org/api/query?"
    START = 0
    MAX_RESULTS = int(raw_input("Supply max result size: "))
    WAIT_TIME = 5
    list_len = len(search_words)
    one_unit = 100.0/float(list_len)
    print "One unit: {}".format(one_unit)
    COMPLETED = 0

    for kw in search_words:
        SEARCH_QUERY = "all:%22" \
                       + '%20'.join(kw.split()) + "%22"
        SEARCH = BASE_URL + \
                 'search_query=%s&start=%i&max_results=%i' % \
                 (SEARCH_QUERY,
                  START,
                  MAX_RESULTS)
        print "\n\t\tPlease wait for query response of: {}".format(kw)
        RESPONSE = urlopen(SEARCH)
        assert RESPONSE.msg.upper() == 'OK'        
        print "\t\tResponse: OK\n"
        XML_RESPONSE = RESPONSE.read()
        QP = QueryParse(XML_RESPONSE, kw)
        QP.parse_data()
        QP.store_data()
        COMPLETED += one_unit

        print " {} % completed".format(COMPLETED)
        print 'Sleeping for %i seconds' % WAIT_TIME
        time.sleep(WAIT_TIME)        

    print "100 % done"
