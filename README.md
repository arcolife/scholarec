scholarec v0.9
==============
Recommendation of Scholarly Works 
---------------------------------

[![Build Status](https://travis-ci.org/arcolife/scholarec.png?branch=master)](https://travis-ci.org/arcolife/scholarec)
[![Dependency Status](https://gemnasium.com/arcolife/scholarec.png)](https://gemnasium.com/arcolife/scholarec)

This software has been built due to a need felt for a proper 
recommendation system for publicly available scholarly/research works. 
It classifies documents and uses personalization features to 
suggest/recommend similar ones, possibly of interest to the user.

> *Inspired from an older project* [researchlei](http://cs.stanford.edu/people/karpathy/researchlei/ "BSD Licensed")

***

**Installation**

```
    $ git clone https://github.com/arcolife/scholarec.git
    $ cd scholarec/
    $ sudo python setup.py install
```

* See INSTALL for detailed instructions.

Optionally, to test if installed, look for a description on executing:
```
    $ python -m scholarec
```

* To see if the scripts runs without error
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

***

**FAQ**

Q. What data interchange file formats have been used?

A. Data conversion from XML to JSON as well as in XML itself.


Q. What are the Data sources? 

A. Dataset currently taken from DBLP, arXiv


Q. How is the Data dealt with?

A. We hope to use ElasticSearch/MongoDB for search and storage

***

**LICENSE**

[![GPL V3](http://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0-standalone.html)