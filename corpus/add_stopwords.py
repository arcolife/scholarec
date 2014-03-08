import os
import pickle

def load_new_data(data):
    '''
    Read file object. And then,
    Safely evaluate an expression node or 
    a string containing a Python expression.
    '''    
    print "New input types allowed:"
    print "1) .txt (text) 2) .p (pickle)\n 3) .lst (list)\n"
    try:
        choice = int(raw_input("Enter Choice (1/2/3): "))
        assert choice in [1,2,3]
    except:
        quit("\nError: No such option! *Terminating execution*")

    try:
        f = open(raw_input("\nEnter filename (with extension): "), 'rb')
        if choice == 1:
            input_data = f.read().split('\n')
        elif choice ==2:
            input_data = pickle.load(f)
        else:
            import ast
            input_data = ast.literal_eval(f.read())
        f.close()
    except:
        raise

    print "length of {} = %d".format('data')%(len(data))
    print "length of {} = %d".format('input_data')%(len(input_data))

    new_data = list(set(input_data) - set(data))
    data.extend(new_data)
    print "length of {} = %d".format('extended data')%(len(data))
    return data

if __name__ == '__main__':
    # Deal with pickle dumps / text formats.
    filename = 'stopwords_combined.p'
    print "This script outputs data in pickle file object\n"
    print "Searching for file named 'stopwords_combined.p' ..\n"
    if os.path.exists(filename):
        # Load previously saved object
        file = open(filename,'rb')
        data_old = pickle.load(file)
        print 'File load successful: {} \n'.format(filename)
        file.close()
        if bool(data_old):
            pass
        else:
            data_old = []
    else:
        print "File Not Found: {} \n".format(filename)
        data_old = []
    
    # append new object
    data = load_new_data(data_old)
    # dump new object
    file = open(filename,'wb')        
    pickle.dump(data, file)
    file.close()        
