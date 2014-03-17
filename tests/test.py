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

""" This module tests the installed package
by executing statements on sample XML set"""

## import general modules
import sys

## Import dependencies specific to scholarec
from scholarec.Base.DocumentClass import DocumentArXiv

class QueryParse:
    ''' mathods to parse query '''    
    def __init__(self, query_xml):
        self.query_xml = query_xml
        self.entry_count = None
        self.data_dict = None
        self.doc = None
        
    def parse_data(self):
        """ parse extracted data into python dict format """
        self.doc = DocumentArXiv(self.query_xml)
        #self.data_xml, self.data_dict = Doc.extract_data()
        self.data_dict = self.doc.extract_tags()
        self.entry_count = len(self.data_dict.keys())
        if self.entry_count:
            print "\t\tTotal Entries: ", self.entry_count
        else:
            sys.exit("\nNo matching entries found!")

if __name__ == '__main__':
    try:
        XML_RESPONSE = ''' 
        <?xml version="1.0" encoding="UTF-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
        <link href="http://arxiv.org/api/query?search_query%3Dall%3Acern%26id_list%3D%26start%3D0%26max_results%3D5" rel="self" type="application/atom+xml"/>
        <title type="html">ArXiv Query: search_query=all:cern&amp;id_list=&amp;start=0&amp;max_results=5</title>
        <id>http://arxiv.org/api/XczqPj3ee1QcMgpV9B7g7as81Dc</id>
        <updated>2014-03-05T00:00:00-05:00</updated>
        <opensearch:totalResults xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">10902</opensearch:totalResults>
        <opensearch:startIndex xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">0</opensearch:startIndex>
        <opensearch:itemsPerPage xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">5</opensearch:itemsPerPage>        
        <entry>
        <id>http://arxiv.org/abs/1206.4876v1</id>
        <updated>2012-06-21T13:42:05Z</updated>
        <published>2012-06-21T13:42:05Z</published>
        <title>40th Anniversary of the First Proton-Proton Collisions in the CERN
        Intersecting Storage Rings (ISR)</title>
        <summary>  No Abstract of this Colloquium
        </summary>
        <author>
        <name>U. Amaldi</name>
        </author>
        <author>
        <name>P. J. Bryant</name>
        </author>
        <author>
        <name>P. Darriulat</name>
        </author>
        <author>
        <name>K. Hubner</name>
        </author>
        <link href="http://arxiv.org/abs/1206.4876v1" rel="alternate" type="text/html"/>
        <link title="pdf" href="http://arxiv.org/pdf/1206.4876v1" rel="related" type="application/pdf"/>
        </entry>
        </feed>
        '''        
        QP = QueryParse(XML_RESPONSE)
        QP.parse_data()

    except IOError as err:
        print "\nI/O error({0}): {1}".format(err.errno, err.strerror)
        print "Maybe you're disconnect from the Internet.."
    except KeyboardInterrupt:
        print "\n\n\t\tYou've aborted the program! \n"
    except ValueError as err:
        print "\nERROR: ", err, "\nCheck your input type."
    except IndexError as err:
        print "\nERROR: ", err, "\nResponse attributes not satisfied."
    except AssertionError as err:
        print "\nERROR: Response: not OK! Maybe a site error"
    except:
        # >>sys.exc_info()<< gives whole exception
        print "Error: ", sys.exc_info()[0]  
        # system call to raise the exception out loud
        raise
