# name, date, time, and service type, hash, creation time
# this structure comes from main data source,
# eg from database or appointments.txt file

data_newlines_plaintext = """
James Smith,2025-02-25,0930,1,7321155854573071151,2025-02-23_105123
Katie Everdeen,2025-02-25,1000,2,2209036143931983137,2025-02-23_105223
Ella Purnell,2025-03-02,1130,1,7707875287172062920,2025-02-23_105323
Mikey Madison,2025-03-02,1300,1,329652982296378014,2025-02-23_105423
"""


def dataset():
    return data_newlines_plaintext.strip().splitlines()
    ## splits full datamassive to the list by newlines


import datetime
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


if __name__ == "__main__":
    # print(hash(current_time_safe()))
    print(filter_by_name('James'))
    print(filter_by_date('2025-02-25'))
    # print(date_today())
    # print(current_time_safe())
