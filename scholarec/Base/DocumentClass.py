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

""" This script parses the XML structure 
passed to the object of Document Class."""

## import general modules
from urlparse \
    import urlparse
from xml.dom.minidom import \
    parseString #,parse

## import dependencies
import xmltodict
from BeautifulSoup import \
    BeautifulStoneSoup as Soup
#import requests

class DocumentArXiv(object):
    """
    ETL: extract, transform, load
    To parse XML dataset (on arXiv: using search API) 
    and return: 
        - XML-dom
        - OrderedDict """

    def __init__(self, query_xml):
        self.query_xml = query_xml
        self.parsed_to_dict = None
        self.parsed_dict_results = None
        self.set_dom = None
        self.entries = None
        self.find_authors = lambda x: x.find('name').string
        self.data = {} # keys: id & values: metadata

    def extract_tags(self):
        """
        Using: BeatifulSoup's XML parser
        Returns XML data in dict format 
        """
        soup = Soup(self.query_xml) # XML as a string
        self.entries = soup.findAll('entry') # list of <entry>'s
        for entry in self.entries:
            # strip down entry ID in url to (say) -> 'abs/math/0507289v1'
            entry_id = urlparse(entry.find('id').string).path.lstrip('/') 
            title = entry.find('title').string
            summary = entry.find('summary').string
            # findAll() for multiple entries 
            authors = entry.findAll('author') 
            # returns list of data-type: BeautifulSoup.Tag
            authors = map(self.find_authors, authors)
            published = entry.find('published').string
            meta = { 'title': title, 'summary': summary, \
                  'authors': authors, 'published': published }
            self.data[entry_id] = meta

        return self.data # python dict

    def extract_tags_xmltodict(self):
        """
        WARNING: this method is now Obsolete, but still included; 
        USE > Document.extract_data_soup < instead.
        This method uses: xmltodict
        """
        # form a DOM structure
        self.set_dom = parseString(self.query_xml) 
        self.parsed_to_dict =  xmltodict.parse(self.query_xml, \
                                               process_namespaces=True)
        #list of OrderedDicts
        self.parsed_dict_results = self.parsed_to_dict.values()[0].values()[7]
        # Relevant XML entries
        self.entries = self.set_dom.getElementsByTagName('entry')        
        try:
            # check/compare both type entries    
            assert len(self.entries) == len(self.parsed_dict_results)
        except AssertionError:
            print "Data entries different or some other anomaly found\n \
            **On comparing data in OrderedDict type & in XML-dom type\n"

        return self.entries, self.parsed_dict_results
