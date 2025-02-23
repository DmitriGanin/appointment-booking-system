import random
import datetime

# name, date, time, and service type, hash (confirmation code), creation time
# this structure comes from main data source,
# eg from database or appointments.txt file

data_newlines_plaintext = """
James Smith,2025-02-25,0930,1,r7z47dy,2025-02-23_105123
Katie Everdeen,2025-02-25,1000,2,73p9wsx,2025-02-23_105223
Ella Purnell,2025-03-02,1130,1,jhnw4g7,2025-02-23_105323
Mikey Madison,2025-03-02,1300,1,wwfht88,2025-02-23_105423
"""


def dataset():
    return data_newlines_plaintext.strip().splitlines()
    ## splits full datamassive to the list by newlines


def make_hash(len = 7):
    hOut = ''
    aTxt = "a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s, t, u, v, w, x, y, z"
    aList = aTxt.split(', ')
    nList = [2, 3, 4, 5, 6, 7, 8, 9]
    fMatrix = [aList, nList] # 2D lists, to have letters and numbers evenly
    for i in range(0,len):
        hOut += str(random.choice(random.choice(fMatrix)))
    return hOut
    ## makes hashes on format eg r7z47dy
    ## use for confirmation codes to have some unique identificator


def date_today():
    return datetime.datetime.now().strftime('%Y-%m-%d')
    ## date format on YYYY-MM-DD


def current_time_safe():
    return datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    ## current datetime format YYYY-MM-DD_HHMMSS


def filter_by_name(name, d = dataset()):
    list_out = ''
    for k,v in enumerate(d):
        el = v.split(',')
        if name in el[0]: ## 0 field is name, eg James Smith
            list_out += v + '\n'
    return list_out


def filter_by_date(date, d = dataset()):
    list_out = ''
    for k,v in enumerate(d):
        el = v.split(',')
        if date in el[1]: ## 1 field is date, eg 2025-02-25
            list_out += v + '\n'
    return list_out


def filter_by_hash(hash, d = dataset()):
    list_out = ''
    for k,v in enumerate(d):
        el = v.split(',')
        if hash in el[4]: ## 4 field is hash, eg 73p9wsx
            list_out += v + '\n'
    return list_out


if __name__ == "__main__":
    # print(make_hash())
    print(filter_by_name('James'))
    print(filter_by_date('2025-02-25'))
    print(filter_by_hash('73p9wsx'))
    # print(date_today())
    # print(current_time_safe())
