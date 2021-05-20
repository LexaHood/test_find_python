import sys
import argparse
import os
import fnmatch


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--path', '-p', help='directory path')
    parser.add_argument ('--name', '-n', default='*', help='file name')
    parser.add_argument ('--delete', '-d', action='store_true', default=False, help='delete found files')
    parser.add_argument ('--info', '-i', action='store_true', default=False, help='debug information')    
 
    return parser


def treatment_path(space):
    if space.path == None:
        space.path = os.path.abspath('')
    else:
        space.path = os.path.abspath(space.path)

    return {
        'exsist': os.access(space.path, os.F_OK),
        'record': os.access(space.path, os.W_OK)
    }


def find_item(space):
    items = []
    for root, dirnames, filenames in os.walk(space.path):
        for filename in fnmatch.filter(filenames, space.name):
            items.append(os.path.abspath(os.path.join(root, filename)))
    
    return items


def find(space, session_acess):
    if (session_acess['exsist']):
        items = find_item(space)
        if (space.delete and len(items) > 0):
            if (session_acess['record']):
                for item in items:
                    try:
                        os.remove(item)
                        print('deleted: %s' %item)
                    except OSError as err:
                        print('failed to delete file')
                        print("OS error: {0}".format(err))
                    except:
                        print("Unexpected error:", sys.exc_info()[0])
                        raise
            else:
                print('no access rights to change directory')
        else:
            if (len(items) > 0): 
                for item in items:
                    print('found: %s'%item)
            else: 
                print('nothing was found') 
    else:
        print('path not available')
        

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    session_acess = treatment_path(namespace) 

    find(namespace, session_acess)  

    if (namespace.info):
        print('{}'.format(namespace))
        print(session_acess)
