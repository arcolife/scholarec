#!/usr/bin/python

import sys, json, grequests 
from json import dumps, loads

# path of directory containing all .json files
PATH_SOURCE = './data_arxiv_json/'
URL = 'http://localhost:9200/arxiv/docs'

def batch(iterable, n=1):
    """ Batch function from StackOverflow answers."""
    l = len(iterable)
    for ndx in range(0,l,n):
        yield iterable[ndx:min(ndx+n,l)]

def convert_and_post_request(path_source, keyword):
    data = json.loads(open(path_source+'query_results'
                           +keyword+'.json','rb').read())
    reqs = []
    for key in data.keys():
        temp = data[key]
        temp['ID'] = key.split('/')[-1]
        temp['keyword'] = keyword
        reqs.append(grequests.post(URL, data=dumps(temp), stream=True))
    grequests.map(reqs)
    #print "built"
    #return reqs

def main1(keywords):
    for word in keywords:
        convert_and_post_request(PATH_SOURCE, word)

def main2(keywords):
    reqs = []
    for word in keywords:
        reqs.extend(convert_and_post_request(PATH_SOURCE, word))
    print len(reqs)
    for x in batch(reqs,50):
        print "called"
        grequests.map(x, size=50)
        print "done"
        

if __name__=='__main__':
    try:
        f = open('searchWords.lst', 'rb')
        import ast
        keywords = ast.literal_eval(f.read())
        f.close()
    except OSError:
        print "Error: ", sys.exc_info()[1][1]

    main1(keywords)
    #main2(keywords)
