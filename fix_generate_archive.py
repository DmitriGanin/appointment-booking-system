""" Current script is generating the pseudorandom
    appointment data to have needed amount for running
    statistics script "fiy_statistics_table_output.py"

    appointmentsArchive.txt file is standalone, archive type backward looking data 
    archive file is separate from live data, which is supposed to be updated on
    appointments.txt, which is more about inserting, searching and updating
"""

from names_generator import generate_name
from random import choice, randrange, randint
from datetime import timedelta, datetime
from filter_appointments import make_hash
from pathlib import Path
import time
tp_start = int(time.time()*1000.0);

def rd(s = '2022-01-01', e = '2025-03-08'): # makes random date within given range
    start = datetime.strptime(s, '%Y-%m-%d') # s - start date
    end = datetime.strptime(e, '%Y-%m-%d') # e - end date
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    randDate = start + timedelta(seconds=random_second)
    return str(randDate.strftime('%Y-%m-%d'))

checkSet = set()
tMor = [10.00, 10.30, 11.00, 11.30, 12.00, 12.30, 13.00]
tAfter = [13.30, 14.00, 14.30, 15.00,13.30, 14.00, 14.30, 15.00]
tEveng = [15.30, 16.00, 16.30, 17.00, 17.30, 15.30, 16.00, 16.30, 17.00, 17.30, 15.30, 16.00, 16.30, 17.00, 17.30]
timesAll = tMor + tAfter + tEveng
servType = [1,1,1,1,2,2,2,3,3,4]
for i in range(4*365*3*16): # service types * annual days * years * times on day
    timeOut = rd() + "," + str("{:.2f}".format(choice(timesAll))).replace('.', '')+ "," +str(choice(servType)) #randint(1,4)
    checkSet.add(timeOut)

timesList = list(checkSet) # convert set to list, to be able sort
timesList.sort() # now it is list, can do sorting

allListOut = ''
for i in timesList:
    thisLine = generate_name(style='capital')+','+i+','+make_hash()
    allListOut += thisLine + '\n'

thisDir = Path(__file__).parent.absolute() # get script location in file folders
fullPath = Path(thisDir,"appointmentsArchive.txt") # make full path
print('full path of datafile is', fullPath)
f = open(fullPath, "w") # handle file writing
f.write(allListOut)
f.close()

print('Pseudorandom data is created and written to file')

tp_end = int(time.time()*1000.0); 
tp_diff = tp_end - tp_start
#print('\nScript was running ' + str(tp_diff) + ' ms')

