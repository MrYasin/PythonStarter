"""
calendar command line application
"""

from time import (sleep, strftime)

CALENDAR = {}


def show_welcome(username):
    """Greet user with a welcome message."""

    print("Welcome {}.".format(username))
    sleep(1)
    print("Today is: {}".format(strftime("%A %B %d %Y")))
    print("Hour is: {}".format(strftime("%H %M %S")))
    sleep(1)
    print("What would you like to do?")


def ask_choice():
    """Ask for a choice from user."""

    msg = "A to Add, U to Update, V to View, D to Delete, X to Exit: "
    return raw_input(msg).upper()


def view_events():
    """Print the contents of the calender on screen."""

    # check if the calendar is empty
    if not CALENDAR:
        print("Calendar is empty.")
        return
    print(CALENDAR)


def add_event():
    """Create a new event in the calendar."""

    event = raw_input("Enter event: ")
    date = raw_input("Enter date (MM/DD/YYYY): ")

    # validate the provided date input
    if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print("You can't add to previous years.")
        try_again_msg = "Try Again? Y for Yes, N for No: "
        try_again = raw_input(try_again_msg).upper()
        if try_again != "Y":
            return False
        return True

    # create the event in the calendar
    CALENDAR[date] = event
    print("Success")
    view_events()
    return True


def update_event():
    """Change an existing entry in the calendar."""

    date = raw_input("What date?: ")
    update = raw_input("Enter the update: ")

    # check if there is an event with the provided date
    # present in the calendar
    if date not in CALENDAR:
        print("Update Failed: event with the date '{}' not found!".format(date))
        return False

    # update the event
    CALENDAR[date] = update
    print("Update successful.")
    view_events()
    return True


def delete_event():
    """Delete an existing event from calendar."""

    # check if the calendar is empty
    if not CALENDAR:
        print("Calendar is empty.")
        return True

    # prompt event
    event = raw_input("What event?: ")

    # look for the event in the calendar
    found = None
    for date in CALENDAR:
        if CALENDAR[date] == event:
            found = date
            break

    # event not found in the calendar
    if not found:
        print ("Invalid date.")
        return False

    # delete the event
    del CALENDAR[found]
    print ("Date successfully deleted.")
    view_events()
    return True


def _run():
    show_welcome("Yasin")

    again = True
    while again:
        choice = ask_choice()
        if choice == "V":
            view_events()
        elif choice == "U":
            again = update_event()
        elif choice == "A":
            again = add_event()
        elif choice == "D":
            again = delete_event()
        elif choice == "X":
            again = False
        else:
            print("Invalid command.")
            again = False


if __name__ == "__main__":  # entrypoint
    _run()
