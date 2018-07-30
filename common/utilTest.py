import csv
import sys, getopt
import os
import re
import json
import datetime
import time
from util import *

def testLoadCSV():
    inputfile = "../resource/studentInfo.csv"
    load_csv(inputfile)

if __name__ == "__main__":
    testLoadCSV()	
