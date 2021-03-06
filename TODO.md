*) IMMEDIATE
   - Implement current algorithms used in 
     mrec.crab/recsys library for Python #partial
   - Write useful sample cases. #done
   - Try the BeautifulSoup XML parser #done
   - Try xmltodict XML parser #done
   - Try xml XML parser #done
   - Add Webhooks for Travis CI #done
   - Asses requirements.txt #done
   - Refactor public/index.html #done
   - Add public/mockups #done
   - Connect Web Interface #done
   - Include tests/ into main package
   - Change TODO done/partial method to new [ ] and [x] format
   
*) ISSUES
			~~ In addition to github issue list ~~

   - Web Interface:
     - Add top citations / references column 
     - Integrate with Python script, 
       to search term in paper repo #partial
     - Add suggestions column on search page
     - Add definition column to search page
     - topwords / citations count display. 
     - fulltext link and pdf downloader #done
     - Select tools for data visualization and infographics
       (Google Chart API / D3 / GraphViz / Processing / etc.. )
       
   - Packaging (add to setup script):
     - check if javacc installed
     - install python-memcache
     - add django secret key
     - install curl
     - install elasticsearch
     - change setup file in django repo
     
   Logic:
	- tf-idf implementation #partial
   	- Stemming options:
     	  - nltk.stem.porter
	  - PorterStemmer / standalone #partial
	- Steps of Data Mining:
		1. Create Corpus #done
		2. Tokenize #done
		3. Stem #done
		4. Eliminate Stop words #partial
		5. Eliminate frequency words #partial
		6. Normalize Spelling/Case
		7. Eliminate Punctuation #partial
		8. Create Term Document Matrix
		   - [Document(Row)] X [Abbreviated Word List(Columns)]
		   - Use SVD's reduce dimensionality 
		     and expose underlying meaning
		   - Related to principal components analysis.
		9. Create Indices
		10. Extract Knowledge

   - Explore Search Engine / Indexing options: 
     - Lucene
     - Solr
     - lupyne
     - solrpy
     - ES #partial
     - sunburnt
    
   - Add to DocumentData.py for processing 
     plain text docs to extract topwords #partial
   - Add default 'arXiv_parsing_example.py' to tests #done
   - Add script to retrieve wikipedia/DuckDuckGo/Google 
     for search term #partial
   - Make db in django (NoSQL / SQL ??) 
   - Add paper.py (multithreaded batch processing jobs):
     Extract the ID's. segregate, and make a list by ID's.
     Then make shell / python script to batch process adding 
     of these papers to the database
   - Explore new data source options 
     - process dtd in XML from dblp
       - Try untangle module
     - ~1000 queries on Google Scholar (after that, IP is blacklisted)
     - 

   - A generic extract_data() function; specifying tags as args
     OR
     Make new class, that extracts data from different sources #partial
   - Represent the structure modulewise #done
   - improve run-tests.sh #partial
   - handle data_dict atribute error on response dissatisfaction #obsolete
   - handle query response strictness (exact match) #obsolete
   - ETL .. DBLP / CERN / arXiv .. data onto ES instance #obsolete
   - Run scripts to extract related data from arXiv (if no dump found). #done
     Check rate limits.
   - Integrate ES with MongoDB and write API script

   - Change query_parse so as to split data into chunks;
      then edit QueryES.DocumentOperations.DocumentUpload 
      so as to upload those chunks to ES instance with proper mapping

*) FUTURE
   - Unit testing methods integrations, Use Jenkins to keep track?
   - Develop aggregation methodologies for ES instance
   - DataSets - Comp. Sc. / Physics / ..