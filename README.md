scholarec
=========
Recommendation of Scholarly Works 
---------------------------------

[![Build Status](https://travis-ci.org/arcolife/scholarec.png?branch=master)](https://travis-ci.org/arcolife/scholarec)
[![Dependency Status](https://gemnasium.com/arcolife/scholarec.png)](https://gemnasium.com/arcolife/scholarec)
[![Zenodo DOI for github](https://zenodo.org/badge/4244/arcolife/scholarec.png)](http://dx.doi.org/10.5281/zenodo.10265)

This software has been built due to a need felt for a proper 
recommendation system for publicly available scholarly/research works. 

It classifies documents and uses personalization features and content-based algorithm to 
suggest/recommend similar ones, possibly of interest to the user. 

_Note:_ Currently, full-functionality is offered by combining this package and another one, 
	that offeres web interface (Django-based). 	
- [arcolife/django-scholarec](https://github.com/arcolife/django-scholarec "django-scholarec")

> *Inspired from an older project* [researchlei](http://cs.stanford.edu/people/karpathy/researchlei/ "BSD Licensed")

***

**Installation**

```
    $ git clone https://github.com/arcolife/scholarec.git
    $ cd scholarec/
    $ sh setup.sh
```

* See INSTALL for detailed instructions.

**Test**

* Optionally, to test if installed, look for a description on executing:
```
    $ python -m scholarec
```

* To see if the scripts runs without error:
```
    $ ./tests/run-tests.sh
    $ ./tests/test.py
```

**Usage**

* To use the module in a Python script, simply import:
```python
    import scholarec
```

* To check a sample run output, open log/sample_run.txt

* To go for a sample run:

```
    $ ./tests/query_parse
```

Note: For developing a small database from arXiv, you need to run 
the query_parse script and accept "Extract PDF" option for extracting 
related pdf's, converting them to plain text and extracting interesting 
words that would later be used for recommendations and suggestions.


* A simple arXiv API call can be achieved by executing the following sample code:
```python          
import scholarec
from scholarec.base.arxiv import DocumentArXiv
url = "http://export.arxiv.org/api/query?search_query=all:%22higgs%22&start=0&max_results=2"
from urllib2 import urlopen
query_xml = urlopen(url)
doc = DocumentArXiv(query_xml)
data_dict = doc.extract_tags()
for entry_id in data_dict.keys():
    print "ID: %s" % (entry_id)
    print(data_dict[entry_id]), "\n"
```
        
***

**FAQ**

Q. What data interchange file formats have been used?

A. Data conversion from XML to JSON as well as in XML itself.


Q. What are the Data sources? 

A. Dataset currently taken from arXiv. Future: DBLP/Google Scholar. 


Q. How is the Data dealt with?

A. ElasticSearch/MongoDB for search and storage

***

**LICENSE**

[![GPL V3](http://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0-standalone.html)