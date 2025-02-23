from pathlib import Path
#saves appointments to a .txt file from a list for example: appointment = ["Andres Käär", "2025-02-25", "14:00", "Haircut"]
#appointment = [["Andres Käär", "2025-02-25", "14:00", "teenus","räsi"], ["Andres Käär", "2025-02-25", "14:00","Haircut","räsi"]]

def save_appointments(appointments, filename="appointments.txt"):
    with open(filename, "a") as file: #new appointments are added not overwritten
        for appointment in appointments:
            file.write(f"{appointment[0]},{appointment[1]},{appointment[2]},{appointment[3]}, {appointment[4]}\n")
    print("Appointments saved!")

#save_appointments(appointment, filename="test.txt")


#Loads appointments form a file (for example: filename="appointments.txt) to an appointments list

def load_appointments(filename="appointments.txt"):
    appointments = []
    thisDir = Path(__file__).parent.absolute()
    fullPath = Path(thisDir,filename)
    #print(fullPath)
    try:
        with open(fullPath, "r") as file:
            for line in file:
                name, date, time, service, rasi = line.strip().split(",")
                appointments.append([name, date, time, service, rasi])
        #print("Appointments loaded!")
    except BaseException as e:
        print("Error on file handling", str(e))
    return appointments

#loaded_appointments = load_appointments(filename="test.txt")
#print(loaded_appointments)
#print(loaded_appointments[1][2])

