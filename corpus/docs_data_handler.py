#!/usr/bin/python

import os 
import sys
import json
from subprocess import call
import grequests 
from json import dumps, loads

# path of directory containing all .json files
PATH_SOURCE = './data_arxiv_json/'
URL = 'http://localhost:9200/arxiv/docs'

def upload_doc(path_source, keyword):
    data = json.loads(open(path_source+'query_results'
                           +keyword+'.json','rb').read())
    reqs = []
    for key in data.keys():
        temp = data[key]
        temp['ID'] = key.split('/')[-1]
        temp['keyword'] = keyword
        reqs.append(grequests.post(URL, data=dumps(temp)))
        if len(reqs) % 100 == 0:
            grequests.map(reqs)
            reqs = []
        else:
            continue
    grequests.map(reqs)

try:
    file_ = open('searchWords.lst', 'rb')
    import ast
    keywords = ast.literal_eval(file_.read())
    file_.close()
    for word in keywords:
        upload_doc(PATH_SOURCE, word)
except OSError:
    print "Error: ", sys.exc_info()[1][1]

# def batch(iterable, n=1):
#     l = len(iterable)
#     for ndx in range(0,l,n):
#         yield iterable[ndx:min(ndx+n,l)]
# for x in batch(range(10),3):
#     print x
