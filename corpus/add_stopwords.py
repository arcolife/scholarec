#!/usr/bin/python

"""
This module helps a user add new words to the dicitonary of stopwords.
"""

import os
import pickle

def load_new(data):
    '''
    Read file object. And then,
    Safely evaluate an expression node or 
    a string containing a Python expression.
    '''    
    print "New input types allowed:"
    print "1) .txt (text) \n2) .p (WARNING: Use trusted pickled object-source)"
    print "3) .lst (list) \n4) 'abc xyz 123' (space-separated)"
    choices = [1, 2, 3, 4]
    try:
        choice = int(raw_input("\nEnter Choice {}: ".format(choices)))
        assert choice in choices
    except:
        quit("\nError: No such option! *Terminating execution*")

    try:
        if choice == 4:
            loaded = raw_input("\nEnter space-separated words: " ).split()
        else:
            fi = open(raw_input("\nEnter filename (with extension): "), 'rb')
            if choice == 1:
                loaded = fi.read().split('\n')
            elif choice == 2:
                loaded = pickle.load(fi)
            elif choice == 3:
                import ast
                loaded = ast.literal_eval(fi.read())
            fi.close()
    except:
        raise

    print "length of {} = %d".format('data')%(len(data))
    print "length of {} = %d".format('input_data')%(len(loaded))

    data = list(set(data))
    loaded = list(set(loaded) - set(data))
    data.extend(loaded)
    print "length of {} = %d".format('extended data')%(len(data))
    return data

if __name__ == '__main__':
    # Deal with pickle dumps / text formats.
    F_NAME = 'stopwords_combined.p'
    print "\n## This script outputs data in pickle file object\n"
    print "> Searching for file named 'stopwords_combined.p'"
    if os.path.exists(F_NAME):
        # Load previously saved object
        f = open(F_NAME,'rb')
        previous = pickle.load(f)
        print '> File loaded successfully: {} \n'.format(F_NAME)
        f.close()
        if bool(previous):
            pass
        else:
            previous = []
    else:
        print "> File Not Found: {} \n".format(F_NAME)
        previous = []
    
    # append new object
    modified = load_new(previous)
    # dump new object
    fo = open(F_NAME,'wb')        
    pickle.dump(modified, fo)
    fo.close()
