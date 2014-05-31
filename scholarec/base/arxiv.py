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
from urlparse import \
    urlparse
from urllib import \
    urlretrieve #, urlopen
from xml.dom.minidom import \
    parseString #,parse
from subprocess import \
    call
import feedparser

## import dependencies
import xmltodict
from bs4 import \
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
        self.parsed_dict_results = None
        self.set_dom = None
        self.entries = None
        self.data = {} # keys: id & values: metadata
        self.url_path = 'http://arxiv.org/pdf/'
        self.feed = None

    def extract_tags(self):
        ''' Use feedparser to directly parse 
        response (type: XML feed) from arxiv.'''
        self.feed = feedparser.parse(self.query_xml)
        for entry in self.feed.entries:
            meta = { 'title': entry.title, 'summary': entry.summary, \
                     'author': entry.author, 'authors' : entry.authors, \
                     'published': entry.published, 'links' : entry.links }
            self.data[entry.id] = meta
        
        return self.data
        
    def extract_tags_bs4(self):
        """
        Using: BeatifulSoup's XML parser
        Returns XML data in dict format 
        """
        soup = Soup(self.query_xml) # XML as a string
        self.entries = soup.findAll('entry') # list of <entry>'s
        find_authors = lambda x: x.find('name').string
        for entry in self.entries:
            # strip down entry ID in url to (say) -> 'abs/math/0507289v1'
            entry_id = urlparse(entry.find('id').string).path.lstrip('/') 
            title = entry.find('title').string
            summary = entry.find('summary').string
            # findAll() for multiple entries 
            authors = entry.findAll('author') 
            # returns list of data-type: BeautifulSoup.Tag
            # PYLINT chatters: authors = map(self.find_authors, authors)
            # using list comprehension instead
            authors = [find_authors(i) for i in authors]

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
        parsed_to_dict =  xmltodict.parse(self.query_xml, \
                                          process_namespaces=True)
        #list of OrderedDicts
        self.parsed_dict_results = parsed_to_dict.values()[0].values()[7]
        # Relevant XML entries
        self.entries = self.set_dom.getElementsByTagName('entry')        
        try:
            # check/compare both type entries    
            assert len(self.entries) == len(self.parsed_dict_results)
        except AssertionError:
            print "Data entries different or some other anomaly found\n \
            **On comparing data in OrderedDict type & in XML-dom type\n"

        return self.entries, self.parsed_dict_results

    def extract_pdfs(self):
        """
        Downloads a document's pdf and dumps 
        the output, for analysis. 
        """
        try:
            if os.path.exists('db'):
                pass
            else:
                os.mkdir('db')
            count = 1
            for entry in self.feed.entries:
                doc_id = entry['id'].split('http://arxiv.org/')[-1]
                dir_path = os.path.join('db', doc_id )
                if os.path.exists(dir_path):
                    pass
                else:
                    os.makedirs(dir_path)
                # download pdf
                pdf_path = os.path.join( 'db', \
                                         doc_id, \
                                         doc_id.split('/')[-1] + '.pdf' )
                if os.path.exists(pdf_path):
                    continue
                else:
                    print "\nExtracting entry #{}: %s".format(count) \
                        % (pdf_path)
                    for link in entry.links:
                        try:
                            if link.title == 'pdf':
                                print 'pdf link: %s' % link.href
                                urlretrieve(link.href, pdf_path)
                        except IOError as err:
                            print "\nI/O error({0}): {1}".\
                                format(err.errno, err.strerror)
                        except:
                            continue
                    print "Done:"
                    print "Converting: .pdf to .txt .."
                    cmd = ['pdftotext', \
                           pdf_path, \
                           os.path.join( \
                                         dir_path, \
                                         doc_id.split('/')[-1] + '.txt' ) ]
                    # execute shell
                    call(cmd)
                count += 1
        except OSError as err:
            print "\nERROR: ", err
        except KeyboardInterrupt:
            print "\n\n\t\tYou've aborted the program! \n"
        except:
            raise
