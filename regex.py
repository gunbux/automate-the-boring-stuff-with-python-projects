#!python3
#regex.py - Renames files with American MMDDYYYY date format with European DDMMYYYY date format using regex.

import shutil, os, re

#TODO: Create a regex that matches the filenames with the American date format.

datePattern = re.compile(r"""(.*?) #all text before the date
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)?\d\d)
    (.*?)$
""", re.VERBOSE)

#TODO: Loop over the files in the working directory

for amerFilename in os.listdir():

    mo = datePattern.search(amerFilename)

    #Skip files without a date
    if mo == None:
        continue

    #Get different parts of the filename

    beforePart - mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart = mo.group(4)
    afterPart = mo.group(5)

    euroFilename = beforepart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    #get full absolute paths

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWrokingDir,amerFilename)
    euroFilename = os.path.join(absWorkingDir,euroFilename)

    print('Renaming %s to %s' % (amerFilename,euroFilename))

    shutil.move(amerFilename,euroFilename)
