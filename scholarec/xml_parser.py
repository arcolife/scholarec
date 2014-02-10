"""
To parse XML dataset (arXiv: using search API) 
and store the results as: 
- XML-dom
- OrderedDict """

from xml.dom.minidom import parseString #,parse 
import xmltodict as xd 

def extract_data(query_xml):
    ''' 
    persistant data creation
    ETL: extract, transform, load
    - type XML
    - type OrderedDict '''    
    dom = parseString(query_xml) 
    parsed_to_dict =  xd.parse(query_xml, process_namespaces=True)
    parsed_dict_results = parsed_to_dict.values()[0].values()[7]
    entries = dom.getElementsByTagName('entry')
    try:
        # check/compare both type entries    
        assert len(entries) == len(parsed_dict_results)
    except AssertionError:
        print "Data entries different or some other anomaly found\n \
        **On comparing data in OrderedDict type & in XML-dom type\n"
    return entries, parsed_dict_results
        
'''
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
'''
