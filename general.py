import os

def create_dir(directory):                        #Create a directory for all the websites that are scanned
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
