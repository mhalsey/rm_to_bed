#!/usr/env/python
###############################################################
#Python scripts that takes RM.out files and converts it to .bed file
#With:
#	1. Chromosome name/contig/scaffold
#	2. Chromosome start
#	3. Chromosome end
#	4. TE name
#	5. TE class/family
#	6. Size of the insertion
#	7. K2P distance
#
#	By: Michaela Halsey
#	Contact : michaela.k.halsey@gmail.com
################################################################

import os 
import sys
import pandas as pd

av = pd.read_csv('aVAN.csv', dtype=str)
#reads in the input file

av.drop(av.index[[0,1,2]], inplace=True)
#removes first 3 lines

avan = av.drop(av.columns[[0,1,2,3,7,11,12,13,14]], axis=1)
#removes the selected columns and assigns new object

avan.columns =["Chromosome", "Start", "End", "Strand", "TE", "Family", "Divergence"]
#renames remaining columns

avan["Divergence"] = avan["Divergence"].str.replace("kimura=", "")
#search and replace command

avan["Family"]= avan["Family"].str.replace("/", "\t")
#search and replace command

aVan = (avan["End"] - avan["Start"])
#gets length of TE 

aVan.to_csv("test.bed", sep="\t", header = True, index = False)
#produces csv file that is in bed format
