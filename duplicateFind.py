
import os, sys
import hashlib


def hashfile(path, blocksize = 65536):
    hash = hashlib.md5()

    with open (path,'rb') as afile:
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hash.update(buf)
            buf = afile.read(blocksize)
    return hash.hexdigest()


def duplicateFind(parent):
    dups = {}

    for dirName, subdirs, fileList in os.walk(parent):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            path = os.path.join(dirName, filename)
            file_hash = hashfile(path)
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups


def printRes(dict):
    results = list(filter(lambda x: len(x) > 1, dict.values()))

    if len(results) > 0:
        print('Duplicates Found!')
        print(' Name could differ, but content is identical:')
        for result in results:
                for subresult in result:
                    print('\t\t%s' % subresult)
                print('\t\t__________________')
    else:
        print('No duplicate.')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        folder = sys.argv[1:]
        dups={}
        for i in folder:
            if os.path.exists(i):
               dups=duplicateFind(i)
            else:
                print('%s Is not a valid path!' % i)
                sys.exit()
        printRes(dups)
    else:
        print('Please enter  folder!')