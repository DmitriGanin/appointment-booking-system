# This is a User Menu module that handles how user menu looks like
# Created by Dmitri Ganin

menu_list = [
    "Exit",
    "Schedule new appointment(s)", 
    "View upcoming appointments", 
    "Cancel or reschedule an appointment", 
    "Filter appointments by date or client name", 
    "Save and load appointment data"
    ]

# to verify the string option selected by user against menu option number without potential type casting error
menu_index_as_str = [str(menu_list.index(item)) for item in menu_list]

def user_menu():
    """
    The function shows static user menu and selection of options
    Args: none
    Returns: selected user option as a digit
    """
    print("\nPlease choose an optin from the list:")
    for item in menu_list:
        if item != menu_list[0]:
            print(menu_list.index(item), '-', item)
    print(menu_list.index(menu_list[0]), '-', menu_list[0])
    while True:
        user_option = input("\nEnter the user option you want using one of digits above: ")
        if user_option.strip()[0] in menu_index_as_str:
            return int(user_option.strip()[0])
        else:
            print('Your input is not valid, please try again.')