from pathlib import Path
import time
tp_start = int(time.time()*1000.0);

thisDir = Path(__file__).parent.absolute() # get script location in file folders
fullPath = Path(thisDir,"appointmentsArchive.txt") # make full path
with open(fullPath,'r',encoding='utf-8') as appointmentsArchive:
    content_from_file = appointmentsArchive.read().splitlines()

# the line structure is name, date, time, service type, hash
# Agitated Lichterman,2022-01-01,1130,3,ptse8c3

statDict = {}
statTime = {}
statServ = {}
for i in content_from_file:
    el = i.split(',')
    dArr = el[1].split('-')
    thisMon = str(dArr[0]) + str(dArr[1])
    if thisMon in statDict.keys():
        statDict[thisMon] +=1
    else:
        statDict[thisMon] = 1

    if el[2] in statTime.keys():
        statTime[el[2]] +=1
    else:
        statTime[el[2]] =1

    if el[3] in statServ.keys():
        statServ[el[3]] +=1
    else:
        statServ[el[3]] =1 


def sort_stat_lists(list_in):
    tmpList = sorted(list_in.items(), key=lambda x: x[1], reverse=True)
    totSum = sum(int(x[1]) for x in tmpList) # sums up all second elements, x[1] 
    for k,v in enumerate(tmpList):
        percent = round(v[1]/totSum*100, 1) # calculate this line percent from total sum
        print(v[0], v[1], percent, '%')

print("\nMonthly statistics (month YYYYMM and how many appointments are on this timeframe):")
sort_stat_lists(statDict)

print("\nMost Booked Timeslots (time of the day and how many times it has been booked during last 3 years):")
sort_stat_lists(statTime)

print("\nMost demanded services (service type and how many times is booked):")
sort_stat_lists(statServ)

## end of table output
exit(); 
""" Comment out the exit to run proceeding matplotlib charting
    solution for visualizing the data table on bar diagram
"""
import matplotlib.pyplot as plt
# Number of preferences for different libraries
library = list(statServ.keys())
library.sort(reverse=True)
chosen_by = list(statServ.values())
chosen_by.sort(reverse=False)

plt.barh(library, chosen_by, color='skyblue')
plt.xlabel('Which services are used')
plt.ylabel('Service code')
plt.title('Which are most used services?')
plt.show()

tp_end = int(time.time()*1000.0); 
tp_diff = tp_end - tp_start
#print(tp_start)
#print(tp_end)
print('\nScript was running ' + str(tp_diff) + ' ms')