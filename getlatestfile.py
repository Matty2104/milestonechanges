#!/usr/bin/python
import os
import glob
import shutil

# looking up for the latest files in the download directory
FILEPATH = r'/home/mvrchota/Documents/Assignments/Mark/170531/compare'
FP = '/home/mvrchota/Documents/Assignments/Mark/170531/compare'
# takes latest file and makes copy in Archive and then moves file into Ongoing (file2)
newest = max(glob.glob('%s/*.txt' % FILEPATH), key = os.path.getctime)
newestFile = newest.replace('%s/' % FILEPATH,"")
shutil.copy(newest, '%s/archive/%s' % (FILEPATH, newestFile))
os.rename(newest, '%s/ongoing/file2.txt' % FILEPATH)
print('%s has been backed up and moved to Ongoing directories' % newestFile)
latestFileName = newestFile
print latestFileName
print(" - name of the latest file, that will stay in the root folder for tommorow's diff")
# takes latest file and makes copy in Archive and then moves file into Ongoing (file1)
newest = max(glob.glob('%s/*.txt' % FILEPATH), key = os.path.getctime)
newestFile = newest.replace('%s/' % FILEPATH,"")
shutil.copy(newest, '%s/archive/%s' % (FILEPATH, newestFile))
os.rename(newest, '%s/ongoing/file1.txt' % FILEPATH)
print('%s has been backed up and moved to Ongoing directories' % newestFile)
# copies the latest file back from Ongoing to root folder
copiedFile = r'/home/mvrchota/Documents/Assignments/Mark/170531/compare/%s' % latestFileName
shutil.copy('%s/ongoing/file2.txt' % FILEPATH, '%s/%s' % (FILEPATH, latestFileName))
print('%s has been copied back to root compare directory' % latestFileName)
