scholarec v0.1
==============
Recommendation of Scholarly Works 
---------------------------------

[![Build Status](https://travis-ci.org/arcolife/scholarec.png?branch=master)](https://travis-ci.org/arcolife/scholarec)

This software has been built due to a need felt for a proper recommendation system for publicly available scholarly/research works. It classifies documents and uses personalization features to suggest/recommend similar ones, possibly of interest to the user.

> *Inspired from an older project* [researchlei](http://cs.stanford.edu/people/karpathy/researchlei/ "BSD Licensed")

***

**Installation**

> It is under heavy development currently, so instead of 'install', 
> use 'develop' with setup.py for now. Keep doing 'git pull' on the repo clone. 

$ sudo python setup.py develop

**Usage**

To use the module in a Python script, simply import:

import scholarec

To go for a sample run (Later, have a look at the following script to see how the module works.)

$ ./tests/query_parse

To see if the scripts runs without error

$ ./tests/run-tests.sh

***

**FAQ**

Q. What data interchange file formats have been used?

A. Data conversion from XML to JSON as well as representation in XML itself.


Q. What are the Data sources? 

A. Dataset currently taken from DBLP, arXiv


Q. How is the Data dealt with?

A. We hope to use ElasticSearch/MongoDB for search and storage

***

**LICENSE**

[![GPL V3](http://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0-standalone.html)