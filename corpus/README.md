scripts
=======

* add_stopwords.py - script to add new stopwords

* stopwords_combined.p - Final 'list' of pickled stopwords


* stopwords.lst - data list type file

* stopwords.txt - TEXT type file 

* stopwords_researchlei.txt - stopwords from researchlei

* data_handler.py - script that produces data upload scripts and executes them 
  		    
		    to upload data to ElasticSearch and MongoDB

***

* data_arxiv_json/ - contains raw json files that contains doc metadata (JSON format)
  		     
		     for 150 categories in ArXiv


* data_modelling/ - contains script to load sample data-to-user matrix to pandas package


* db_arxiv_pdf_txt/ - 
  	```
	db_arxiv_pdf_txt/
	|-- abs
	|   |-- 1008.1384v1
	|   `-- cs
	|       `-- 0701087v2
	`-- data
	    |-- raw
            `-- stemmed
	```

	This folder that contains raw and stemmed data and 2 scripts:

	    > extract.py - extracts raw data (pdf) from json files kept in data_arxiv_json/

	    > search.py - sample script to show Tf-IDF search

