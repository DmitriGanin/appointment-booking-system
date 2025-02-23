# This is a main file for launching the appointment booking system
# It will import functions created by student from other modules (.py files) and will use those in the main code
import user_menu

menu_list = user_menu.menu_list # for convenience of others the menu list (and its index as an option digit) is available in main .py code

def launch_booking_system():
    """
    Initiates the main loop of menu selection for chosen actions until Exit is chosen
    """
    print("\nWelcome to the Appointment Booking System!")
    while True:
        user_option = user_menu.user_menu()
        if user_option == 0:
            print("\nGood bye!\n")
            exit()
        elif user_option == 1:  # Schedule new appointment(s)
            pass # placeholder for the modular function
        elif user_option == 2:  # View upcoming appointments
            pass # placeholder for the modular function
        elif user_option == 3:  # Cancel or reschedule an appointment
            pass # placeholder for the modular function
        elif user_option == 4:  # Filter appointments by date or client name
            pass # placeholder for the modular function
        elif user_option == 5:  # Save and load appointment data
            pass # placeholder for the modular function

launch_booking_system()
