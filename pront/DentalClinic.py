import datetime
import re


print("Welcome to Dental Clinic. Select your profile:")
print("\t[1] Patient")
print("\t[2] Doctor")

profile = ""
while profile != "1" and profile != "2":
    profile = input("Selection: ")
    
if profile == "1":
    # It is a patient
    patientId = ""
    while not patientId:
        patientId = input("Enter patient's ID: ")
        
    # Check in DB if patient exists
    # print(f"Patient {patientId} logged on")
    # If not, create as follows:
    """ 
    print("Patient does not exist. Create one")
    patient = dict()
    patient["DNI"] = patientId
    patient["name"] = input("Enter name: ")
    patient["surname"] = input("Enter surname: ")
    patient["address"] = input("Enter address: ")
    patient["phoneNumber"] = input("Enter phone number: ")
    patient["birthdate"] = input("Enter birthdate: ")
    patient["medicalRecords"] = list()
    print(f"Patient {patientId} created with following data:\n{patient}\n")
    """   
         
    operation = "0"
    while operation != "X":
        print("\nSelect an operation, o press [X] to exit")
        print("\t[1] Update profile")
        print("\t[2] Get profile")
        operation = input("Selection: ")
        
        while operation not in ["1","2","3","4","X"]: 
            operation = input("Selection: ")
        
        match operation:                   
            case "1":
                # Update patient's profile
                print("\nYou chose 'Update profile'")
                patient = dict()
                patient["address"] = input("Enter address: ")
                patient["phoneNumber"] = input("Enter phoneNumber: ")
                print(f"Patient {patientId} updated with following data:\n{patient}\n")             

            case "2":
                # Get patient's profile
                print("\nYou chose 'Get profile'")
    
        continue  
else:
    # It is a doctor
    doctor = ""
    while not doctor:
        doctor = input("Enter doctor's ID: ")
        
    operation = "0"
    while operation != "X":
        print("\nSelect an operation, o press [X] to exit")
        print("\t[1] Create patient")
        print("\t[2] Update patient")
        print("\t[3] Get patient")
        print("\t[4] Update patient's medical record")
        operation = input("Selection: ")
        
        while operation not in ["1","2","3","4","X"]: 
            operation = input("Selection: ")
        
        match operation:
            case "1":
                # Create patient
                print("\nYou chose 'Create patient'") 
                patient = dict()
                patient["DNI"] = input("Enter patient ID: ")
                patient["name"] = input("Enter name: ")
                patient["surname"] = input("Enter surname: ")
                patient["address"] = input("Enter address: ")
                patient["phoneNumber"] = input("Enter phone number: ")
                patient["birthdate"] = input("Enter birthdate: ")
                patient["medicalRecords"] = list()
                patient["upperJawPieces"] = input("Enter number of pieces in upper jaw: ")
                patient["lowerJawPieces"] = input("Enter number of pieces in lower jaw: ")
                patient["allergies"] = re.split(r",\s*", input("Allergies (separated by commas): "))
                #print(f"Patient {patient["DNI"]} created with following data:\n{patient}\n")
                    
            case "2":
                # Update patient
                print("\nYou chose 'Update patient'")
                patient = dict()        #--- TO DO: retrieve patient from DB by patientId; error if does not exist
                patientId = input("Enter patient ID: ")
                patient["upperJawPieces"] = input("Enter number of pieces in upper jaw: ")
                patient["lowerJawPieces"] = input("Enter number of pieces in lower jaw: ")
                patient["allergies"] = re.split(r",\s*", input("Allergies (separated by commas): "))
                print(f"Patient {patientId} updated with following data:\n{patient}\n")             

            case "3":
                # Get patient
                print("\nYou chose 'Get patient'")
                    
            case "4":
                # Update medical record
                print("\nYou chose 'Update patient\'s medical record'")
                patientId = input("Enter patient's ID: ")
                patient = dict()   #--- TO DO: retrieve patient from DB by patientId; error if does not exist
                patient["medicalRecords"] = list()  ### obtained from patient retrieved
                record = dict()
                record["doctor"] = doctor
                record["date"] = datetime.datetime.now().strftime("%c")
                record["diagnosis"] = input("Enter diagnosis: ")
                record["treatment"] = input("Enter treatment: ")                    
                patient["medicalRecords"] += [record]
                print(f"Patient's {patientId} medical record updated with following data:\n{record}\n")
        
        continue 
    