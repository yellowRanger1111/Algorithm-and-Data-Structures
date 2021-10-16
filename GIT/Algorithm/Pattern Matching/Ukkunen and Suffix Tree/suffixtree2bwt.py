from ukkonen import *
import sys, os
sys.path.append(os.path.abspath(".."))
sys.path.append(os.path.abspath("."))
'''
By: Owen 30039096
'''

def make_bwt(string):
    a = ukkonnen(string)
    bwt = ""
    for suffix in a.get_elem_in_order():
        bwt += string[(len(string)-len(suffix)-1)% len(string)]
    return bwt


def readFiles(pfn):
    patFile = open(pfn, "r")
    pat = patFile.read()
    patFile.close
    return pat

def writeFile (data, fn):
    file = open(fn, 'w+')
    file.write(data)
    file.close()
    


if __name__ == "__main__":
    fileName = sys.argv[1]

    string1 = readFiles(fileName)
    bwt = make_bwt(string1 + "$")
    
    writeFile(bwt,'output_bwt.txt')

