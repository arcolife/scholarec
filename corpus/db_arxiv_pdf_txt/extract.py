## import general modules
import os
from urllib import \
    urlretrieve #, urlopen
from subprocess import \
    call
import json

def extract_pdfs(entries):
    """
    Downloads a document's pdf and dumps 
    the output, for analysis. 
    """
    _ids = entries.keys()[:10]
    try:
        if os.path.exists('abs'):
            pass
        else:
            os.mkdir('abs')
        count = 1
        for _id in _ids:
            doc_id = _id.split('http://arxiv.org/')[-1]
            dir_path = os.path.join('abs', doc_id )
            if os.path.exists(dir_path):
                pass
            else:
                os.makedirs(dir_path)
            # download pdf
            pdf_path = os.path.join( 'abs', \
                                     doc_id, \
                                     doc_id.split('/')[-1] + '.pdf' )
            if os.path.exists(pdf_path):
                continue
            else:
                print "\nExtracting entry #{}: %s".format(count) \
                    % (pdf_path)
                for link in entries[_id]['links']:
                    try:
                        if link['title'] == 'pdf':
                            print 'pdf link: %s' % link['href']
                            urlretrieve(link['href'], pdf_path)
                    except IOError as err:
                        print "\nI/O error({0}): {1}".\
                            format(err.errno, err.strerror)
                    except:
                        continue
                print "Done:"
                print "Converting: .pdf to .txt .."
                cmd = ['pdftotext', \
                       pdf_path, \
                       os.path.join( \
                                     dir_path, \
                                     doc_id.split('/')[-1] + '.txt' ) ]
                # execute shell
                call(cmd)
            count += 1
    except OSError as err:
        print "\nERROR: ", err
    except KeyboardInterrupt:
        print "\n\n\t\tYou've aborted the program! \n"
    except:
        raise

filenames = os.listdir('../data_arxiv_json/')

for filename in filenames:
    f = open('../data_arxiv_json/' + filename, 'rb')
    data = json.loads(f.read())
    extract_pdfs(data)
    f.close()
