from pyes import *

#Creating a connection:
conn = ES('localhost:9200') #an instance created for testing purpose

#Deleting an index:
try:
    conn.indices.delete_index("test-index")
except:
    pass

#Create an index:
conn.indices.create_index('test-index')

#Creating a mapping:
mapping = { u'parsedtext': {'boost' : 1.0,
                            'index' : 'analyzed' ,
                            'store' : 'yes',
                            'type' : u'string',
                            "term_vector" : "with_positions_offsets"},
            u'name': {'boost': 1.0,
                      'index': 'analyzed',
                      'store': 'yes',
                      'type': u'string',
                      "term_vector" : "with_positions_offsets"},
            u'title': {'boost': 1.0,
                       'index': 'analyzed',
                       'store': 'yes',
                       'type': u'string',
                       "term_vector" : "with_positions_offsets"},
            u'pos': {'store': 'yes',
                     'type': u'integer'},
            u'uuid': {'boost': 1.0,
                      'index': 'not_analyzed',
                      'store': 'yes',
                      'type': u'string'}}

conn.indices.put_mapping("test-type", {'properties':mapping}, ["test-index"])

#Index some documents:
conn.index({"name":"arcolife", "parsedtext":"arcolife the philosopher", "uuid":"1", "position":1}, "test-index", "test-type", 1)
conn.index({"name":"archit", "parsedtext":"@arcolife", "uuid":"2", "position":2}, "test-index", "test-type", 2)

#Refresh an index:
conn.indices.refresh(["test-index"])

#Execute a query
q = TermQuery("name", "arcolife")
results = conn.search(query = q)

#Iterate on results:
for r in results:
    print r
