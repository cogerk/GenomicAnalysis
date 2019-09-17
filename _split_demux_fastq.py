#!/usr/bin/env python

import io
import sys
import random

### _split_demux_fastq.py split usearch demux reads into different fastq files:
        #   -f <fastq_merged_reads>
        #   -m <map_file>
            # sample_identifier \t output_file_label

#------------------------------------------------------------------#
# functions
#------------------------------------------------------------------#


def ParseOptions (aList):
    count = 0
    mode = ''
    for i in range(1, len(aList)):
        if aList[i] == '-f':
            fastq = aList[i+1]
            count += 1
        elif aList[i] == '-m':
            mapping = aList[i+1]
            count += 1
    if count != 2:
        print("usage:\n\t-f <fastq_merged_reads>"+
              "\n\t-m <map_file>")
        quit()
    return(fastq, mapping)

def ReadMappingFile (mapping):
    print("reading mapping file: " + mapping)
    map_dict = {}
    file_names = {}
    fIN = io.open(mapping)
    for line in fIN:
        line = line.strip().split('\t')
        sample_id = line[0]
        output_name = line[1]
        map_dict[sample_id] = output_name
        if output_name not in file_names:
            file_names[output_name] = []
    fIN.close()
    return(map_dict, file_names)

def SortFastq (map_dict, file_names, fastq):
    print("sorting fastq file: " + fastq)
    fIN = io.open(fastq)
    header = ""
    seq = ""
    space = ""
    qual = ""
    n = 0
    for line in fIN:
        n += 1
        line = line.strip()
        if n == 1:
            header = line
            h = header.split('sample=')
            h = h[1]
            sample_id = h[:-1]
        elif n == 2:
            seq = line
        elif n == 3:
            space = line
        elif n == 4:
            qual = line
            rec = (header,seq,space,qual)
            output_name = map_dict[sample_id]
            file_names[output_name].append(rec)
            header = ""
            h = ""
            sample_id = ""
            seq = ""
            qual = ""
            rec = ""
            n = 0
    fIN.close()
    return(file_names)

def WriteFastq (file_names):
    print("writing fastq files")
    for output_name in file_names:
        outFile = output_name+".fastq"
        print("\t-> "+outFile+"\t"+str(len(file_names[output_name])))
        fOUT = io.open(outFile, 'a')
        for i in range(len(file_names[output_name])):
            (header,seq,space,qual) = file_names[output_name][i]
            fOUT.write(header+"\n"+seq+"\n"+space+"\n"+qual+"\n")
        fOUT.close()
    return()


#------------------------------------------------------------------#
# Main
#------------------------------------------------------------------#

if __name__ == '__main__':
    (fastq, mapping) = ParseOptions(sys.argv)
    (map_dict, file_names) = ReadMappingFile(mapping)
    file_names = SortFastq(map_dict, file_names, fastq)
    WriteFastq(file_names)
    
    
    
