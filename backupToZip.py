#! python3
# backupToZip.py - Copies an entire folder and its content into
# a ZIP file whose file increments

import zipfile, os

def backupToZip(folder):
    # Backup the entire content of the folder into the ZIP file

    folder = os.path.abspath(folder) #make sure folder path is absolute

    # Figure out the filename this code should be based on
    # what files already exist

    number = 1

    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    #TODO: Create the zip file

    print('Creating %s ...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename,'w')

    #TODO: Walk the entire folder tree and compress files in each folder. Print ('Done')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s ...' % (foldername))
        #Add the current folder to Zipfile
        backupZip.write(foldername)
        #Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # Don't backup Zip files
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
    print('Done.')

directory = input('Enter directory to backup: ')
backupToZip(str(directory))