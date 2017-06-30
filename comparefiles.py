#!/usr/bin/python
import difflib
import datetime
import os

FILEPATH = r'/home/mvrchota/Documents/Assignments/Mark/170531/compare/ongoing'
FILEPATH2 = r'/home/mvrchota/Documents/Assignments/Mark/170531/compare/'

datenow = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

FILE1 = open('%s/file1.txt' % FILEPATH, 'r')
FILE2 = open('%s/file2.txt' % FILEPATH, 'r')
OUTPUT = open('%s/output/compare-output-%s.txt' % (FILEPATH2, datenow), 'w')

RESULT = difflib.context_diff(FILE1.readlines(), FILE2.readlines(),
         fromfile='previous version', tofile='current version', n=0)

print('Results in output file (%s)' % OUTPUT)
OUTPUT.write(''.join(RESULT))
OUTPUT.close()
if os.stat('%s/output/compare-output-%s.txt' % (FILEPATH2, datenow)).st_size is 0:
    OUTPUT = open('%s/output/compare-output-%s.txt' % (FILEPATH2, datenow), 'w')
    OUTPUT.write('%s' % datenow)
    OUTPUT.write('\nNo changes since last download')
    OUTPUT.close()
    
FILE1.close()
FILE2.close()


# WORKING :-)
