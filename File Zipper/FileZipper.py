from tkinter import *
from tkinter.filedialog import askdirectory
import os
import time

source1 = askdirectory()
print(source1)
source = [str(source1)]
target_dir = '/Users/Dlucidone/Documents/'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
comment = "zippingDir"#input('Enter a comment --> ')
if len(comment) == 0:

   target = today + os.sep  + '.zip'
else:
     target = today + os.sep  + '_' + \
         comment.replace(' ', '_') + '.zip'
if not os.path.exists(today):
    os.mkdir(today)
print('Successfully created directory', today)

zip_command = "zip -r {0} {1}".format(target,' '.join(source))

print("Zip command is:")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')