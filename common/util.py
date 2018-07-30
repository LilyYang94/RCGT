import csv
import sys, getopt
import os
import re
import json
import hashlib
import collections
import datetime
import time
from logger import logger

reload(sys)
sys.setdefaultencoding('utf-8')

def load_csv(inputfile):
	totalDict = []
	with open(inputfile,'r') as csv_file:
		reader = csv.reader(csv_file)
		head_row = []
		for header_col in next(reader):
			head_row.append(header_col.strip().replace(" ","").replace("\n",""))
		for row in reader:
			dataDict = {}
			for index in range(len(head_row)):
				key = head_row[index]
				value = row[index]
				dataDict[key] = value
			totalDict.append(dataDict)
	logger.info("read %s gives %s" % (inputfile, totalDict))
	return totalDict


    
