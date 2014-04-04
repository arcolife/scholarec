from pyes import *

conn = ES('localhost:9200')

print conn.get('arxiv', 'docs', 'G7AZiorURsuLenEWOQYQzQ')
