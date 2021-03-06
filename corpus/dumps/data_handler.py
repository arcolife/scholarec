#!/usr/bin/python

import os 
import sys
import json
from subprocess import call

# path of directory containing all .json files
PATH_SOURCE = './data_arxiv_json/'
PATH_DEST = './sharded/'

def __write_json_files(path_source, path_dest, keyword):
    '''
    Create json chunks from a previous db dump (.json)
    '''
    # load dump 
    data = json.loads(open(path_source+'query_results'+keyword+'.json','rb').read())
    for key in data.keys():
        temp = data[key]
        temp['ID'] = key.split('/')[-1]
        temp['keyword'] = keyword
        #jEncoder = json.JSONEncoder()
        f = open(path_dest +temp['ID']+'.json','wb')
        json.dump(temp, f)
        f.close()

def __write_es_upload_script(path_dest):
    '''
    write content into bash script that
    is supposed to upload chunks to ElasticSearch instance
    '''
    #list of all json filenames
    filenames = os.listdir(path_dest) 
    FILE = open('es_upload', 'wb')
    # write shell commands
    FILE.write('#!/bin/bash\n')
    FILE.write('cd ' + path_dest + '\n')
    for filename in filenames:
        # develop a command to upload files
        CMD = ['curl','-XPOST',"'http://localhost:9200/arxiv/docs/" \
               #+ filename.strip('.json') \
               + "'",'-d ','@'+filename]
        FILE.write(' '.join(CMD) +"\n")
        #call(CMD)
        #print CMD
    FILE.close()

def __write_mongo_upload_script(path_dest):
    '''
    write content into bash script that
    is supposed to upload chunks to mongodb instance
    '''
    #list of all json filenames
    filenames = os.listdir(path_dest)
    FILE = open('mongo_upload', 'wb')
    # write shell commands
    FILE.write('#!/bin/bash\n')
    FILE.write('cd ' + path_dest + ' \n')
    passw = os.environ.get('mongo_scholarec_p')
    for filename in filenames:
        # develop a command to upload files
        FILE.write('mongoimport --db scholarec -u arco -p ' + passw + ' --collection docs --file '+ \
                filename + "\n")
               #+ filename.strip('.json') \
    FILE.close()

if __name__=='__main__':
    '''
    try:
        # creat directory to dump individual json files
        os.mkdir(PATH_DEST)
        file_ = open('searchWords.lst', 'rb')
        import ast
        keywords = ast.literal_eval(file_.read())
        file_.close()
        for word in keywords:
            __write_json_files(PATH_SOURCE, PATH_DEST, word)

    except OSError:
        print "Error: ", sys.exc_info()[1][1]
    __write_es_upload_script(PATH_DEST)
    '''
    __write_mongo_upload_script(PATH_DEST)
    '''
    # set executable permission to shell script: ./_User_sharded/post
    set_perm = ['chmod', '+x', 'es_upload']
    call(set_perm)
    # execute the script and upload json fiels to ES instance
    call_post = ['./es_upload']
    call(call_post)
    '''
