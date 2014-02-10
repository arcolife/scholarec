---------
**About**
This software has been built due to a need felt for a proper recommendation system for publicly available scholarly/research works. It classifies documents and uses personalization features to suggest/recommend similar ones, possibly of interest to the user.

> Inspired from an older project 'researchlei' ( http://cs.stanford.edu/people/karpathy/researchlei/ ) to get an idea of data representation and basic architecture. #BSD Licensed 

**Installation**

$ python setup.py install

**Usage**

1.	Use ./bin/query_parse to query the source and parse results
2.	Use ./bin/saved_entries_count to count existing DB entries

**FAQ**

Q. What data interchange file formats have been used?
A. Data conversion from XML to JSON as well as representation in XML itself.

Q. What are the Data sources? 
A. Dataset currently taken from DBLP, arXiv

Q. How is the Data dealt with?
A. Use ElasticSearch to store data; possible integration with MongoDB

**LICENSE**

GPL v3