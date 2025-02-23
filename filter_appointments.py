import random
import datetime
import file_handling

# name, date, time, and service type, hash (confirmation code)
# this structure comes from main data source,
# from appointments.txt file


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


def filter_by_name(name, d = file_handling.load_appointments()):
    #print('dataset', d)
    list_out = ''
    for k,v in enumerate(d):
        if name in v[0]: ## 0 field is name, eg James Smith
            list_out += ','.join(v) + '\n'
    return list_out


def filter_by_date(date, d = file_handling.load_appointments()):
    list_out = ''
    for k,v in enumerate(d):
        if date in v[1]: ## 1 field is date, eg 2025-02-25
            list_out += ','.join(v) + '\n'
    return list_out


def filter_by_hash(hash, d = file_handling.load_appointments()):
    list_out = ''
    for k,v in enumerate(d):        
        if hash in v[4]: ## 4 field is hash, eg 73p9wsx
            list_out += ','.join(v) + '\n'
    return list_out


def user_option4_interface():
    print("\nEnter the filtering option, with number:") 
    filter_menu_option = "1 - Filter by name, 2 - Filter by date, 0 - Back to the main menu: "
    try:
        user_choice = int(input(filter_menu_option))
        if user_choice == 1:
            user_input_name = input('Please enter the name: ')
            print('\n')
            print(filter_by_name(user_input_name))

        elif user_choice == 2:
            user_input_date = input('Please enter the date on format YYYY-MM-DD: ')
            print('\n')
            print(filter_by_date(user_input_date))

        elif user_choice == 0:
            return
        
        user_option4_interface()        
    except:
        print("There was error in inserted number")
        user_option4_interface()        
    return


if __name__ == "__main__":
    # print(make_hash())
    print(filter_by_name('James'))
    print(filter_by_date('2025-02-25'))
    # print(filter_by_hash('73p9wsx'))
    # print(date_today())
    # print(current_time_safe())
