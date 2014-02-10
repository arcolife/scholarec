---------
**About**
This software has been built due to a need felt for a proper recommendation system for publicly available scholarly/research works. It classifies documents and uses personalization features to suggest/recommend similar ones, possibly of interest to the user.
An older project 'researchlei' [cs.stanford.edu/people/karpathy/researchlei/] has been used for getting an idea of data representation and basic architecture #BSD Licensed

------------------
**Specifications**

- Data conversion from XML to JSON as well as representation in XML itself.
- Dataset currently taken from DBLP, arXiv
- Use ElasticSearch to store data; possible integration with MongoDB

-----------------
**Documentation**

To parse XML dataset (arXiv: using search API) and store the results onto elasticsearch instance