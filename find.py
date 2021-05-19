import sys
import argparse
import os
import glob 


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--path', '-p')
    parser.add_argument ('--name', '-n', default='*')
    parser.add_argument ('--delete', '-d', action='store_true', default=False)
    parser.add_argument ('--info', '-i', action='store_true', default=False)    
 
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
    items = glob.glob(space.path + '/' + space.name)
    if (len(items) > 0): 
        for item in items:
            print('found: %s'%item)
    else: 
        print('nothing was found')
    
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
                    except Exception:
                        pass
            else:
                print('no access rights to change directory')
    else:
        print('path not available')
        

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    session_acess = treatment_path(namespace) 

    find(namespace, session_acess)  

    if (namespace.info):
        # print test value
        print ("{}".format (namespace))
        print(session_acess)
