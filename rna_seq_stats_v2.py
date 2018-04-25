#!/usr/env/python

from Bio import SeqIO
from pandas import DataFrame
import os 
import sys
import statistics as stat
import argparse

LENLIST = []

def get_args():
	parser = argparse.ArgumentParser(description="parses transcripts", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-i', '--input', type=str, help='Insert fasta file', required=True)
	
	args = parser.parse_args()
	INPUT = args.input
		
	return INPUT
INPUT = get_args()

with open('RNA_stats.txt', 'w') as STATS: 

	for RECORD in SeqIO.parse(INPUT, 'fasta'):
			LENLIST.append(len(RECORD.seq))
#Calculates the total base pairs and writes to file
	print('Length in base pairs = ' + str(sum(LENLIST)) + '.')
	STATS.write('Length in base pairs = ' + str(sum(LENLIST)) + '.\n')

#Calculates the transript length 
	print ('Transcript length = ' + str(len(LENLIST)) + '.')
	STATS.write('Transcript length = ' + str(len(LENLIST)) + '.\n')

#Calculates the mean of the length of the transcript
	print('Mean transcript length = ' + str(stat.mean(LENLIST)) + '.')
	STATS.write('Mean transcript length = ' + str(stat.mean(LENLIST)) + '.\n')

def median():
    n = len(LENLIST)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(LENLIST)[n//2]
    else:
            return sum(sorted(LENLIST)[n//2-1:n//2+1])/2.0
			
NFIFTY = median()
print ('The incorrect N50 = ' + str(NFIFTY) + '.')

#STATS.write('N50 = ' + str(NFIFTY) + '.\n')
#Might calculate N50 but I doubt it
