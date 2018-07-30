import csv
import xlrd
from string import Template
import sys, getopt
import os
import re
import json
import hashlib

reload(sys)
sys.setdefaultencoding('utf-8')

inputfile = "./resource/TotalFeature.csv"
