#!/usr/bin/python

import csv2json
import os
import sys
from pathlib import Path
import json


def main():
    dumpFiles()

def dumpFiles():
    cwd = os.getcwd()
    csvfiles = []
    inFile = ''
    outFile = ''
    for entry in os.scandir(cwd):
        if Path(entry.path).suffix == '.csv':
            inFile = Path(entry.path).name
            outFile = Path(entry.path).stem + '.json'
            args = ['-i', inFile, '-o', outFile, '-f', 'pretty']
            csv2json.main(args)
    for entry in os.scandir(cwd):
        if Path(entry.path).suffix == '.json':
            inFile = Path(entry.path).name
            parseJsonForString(inFile,sys.argv[1])

def parseJsonForString(jsonPath,searchTerm):
    with open(jsonPath, 'r') as f:
        json_dict = json.load(f)
    for item in json_dict:
        if searchTerm not in item['Class']:
            continue
        else:
            try:
                print(item['Name'] + ':' + item['Class'])
            except KeyError as err:
                print(item['Unlocalised name'] + ':' + item['Class'])
                #print(err)
                #continue
            #finally:
                #print(item['Unlocalised name'] + ':' + item['Class'])



if __name__ == "__main__":
    main()
