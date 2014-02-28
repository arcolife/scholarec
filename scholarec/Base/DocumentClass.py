'''
This script parses the XML structure 
passed to the object of Document Class in it.
'''
from xml.dom.minidom import parseString #,parse 
import xmltodict

class Document(object):
    '''
    A class representing the xml documents relevant information
    To parse XML dataset (arXiv: using search API) 
    and store the results as: 
    - XML-dom
    - OrderedDict
    '''
    def __init__(self, query_xml):
        self.query_xml = query_xml
        self.parsed_to_dict = None
        self.parsed_dict_results = None
        self.set_dom = None
        self.entries = None

    def extract_data(self):
        ''' 
        persistant data creation
        ETL: extract, transform, load
        - type XML
        - type OrderedDict 
        '''    
        self.set_dom = parseString(self.query_xml) 
        self.parsed_to_dict =  xmltodict.parse(self.query_xml, process_namespaces=True)
        self.parsed_dict_results = self.parsed_to_dict.values()[0].values()[7]
        self.entries = self.set_dom.getElementsByTagName('entry')
        
        try:
            # check/compare both type entries    
            assert len(self.entries) == len(self.parsed_dict_results)
        except AssertionError:
            print "Data entries different or some other anomaly found\n \
            **On comparing data in OrderedDict type & in XML-dom type\n"
        return self.entries, self.parsed_dict_results #list of OrderedDicts

"""
# This fragment of code takes certain tags out of the XML 
# and stores them in certain variables.

for entry in entries:
    #1 element list
    doc_id = entry.getElementsByTagName('id')[0]
    #possibly multiple list elements
    doc_authors = entry.getElementsByTagName('author')
    #1 element list
    doc_summ = entry.getElementsByTagName('summary')[0]
    #1 element list
    doc_title = entry.getElementsByTagName('title')[0]
    #possibly multiple list elements
    doc_pdf_link = entry.getElementsByTagName('link')
"""
