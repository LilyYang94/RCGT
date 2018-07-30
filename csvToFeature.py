import csv
import xlrd
from string import Template
import sys, getopt
import os
import re
import json
import hashlib
from common.util import *

reload(sys)
sys.setdefaultencoding('utf-8')

inputfile = "./resource/studentInfo.csv"
outputfile = "./feature/"
totalDict = load_csv(inputfile)
# print json.dumps(totalDict, indent=4)

