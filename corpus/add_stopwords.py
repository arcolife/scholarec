#!/usr/bin/env python
# -*- coding: utf-8 -*- 

## This file is part of ScholaRec.
## A recommendation engine for Scholarly works.
## Copyright (C) 2014  Archit Sharma <archit.py@gmail.com>
##
## ScholaRec is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## ScholaRec is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>

""" This module helps a user add new words 
to the dicitonary of stopwords."""

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
    except ValueError as err:
        print err
    except:
        quit("\nError: No such option! *Terminating execution*")

    try:
        if choice == 4:
            loaded = raw_input("\nEnter space-separated words: " ).split()
        else:
            file_ = open(raw_input("\nEnter filename (with extension): "), 'rb')
            if choice == 1:
                loaded = file_.read().split('\n')
            elif choice == 2:
                loaded = pickle.load(file_)
            elif choice == 3:
                import ast
                loaded = ast.literal_eval(file_.read())
            file_.close()
    except IOError as err:
        print "ERROR: %s" % (err)
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
    print "> Searching for file named '{}'".format(F_NAME)
    if os.path.exists(F_NAME):
        # Load previously saved object
        FILE_ORIG = open(F_NAME,'rb')
        PREVIOUS = pickle.load(FILE_ORIG)
        print '> File loaded successfully: {} \n'.format(F_NAME)
        FILE_ORIG.close()
        if bool(PREVIOUS):
            pass
        else:
            PREVIOUS = []
    else:
        print "> File Not Found: {} \n".format(F_NAME)
        PREVIOUS = []    

    # append new object
    MODIFIED = load_new(PREVIOUS)
    # dump new object
    FILE = open(F_NAME,'wb')        
    pickle.dump(MODIFIED, FILE)
    FILE.close()
