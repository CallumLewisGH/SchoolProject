#User system
import os

os.chdir("C:\\Users\\callu\\Desktop\\A-Levels\\Computer-Science\\Python Code\\Python\\School_Important\\Project\\Brewerys")


def signup():
    logbook = open("logbook.txt", "a")

    breweryName = input("Enter the name of your brewery: ")
    uniquePasscode = input("Enter your passcode: ")
    breweryLocation = input("Please enter the location of your brewery E.G Stoke-On-Trent: ")
    breweryPostcode = input("Please enter the postcode of your brwewery: ")
    breweryRating = "N/A"

    logbook.write((f"{breweryName}|{uniquePasscode}|{breweryLocation}|{breweryPostcode}|{breweryRating}\n"))
    print("Signup successful your data is now in our system")

    logbook.close()

def login():
    logbook = open("logbook.txt", "r")
    
    breweryName = input("Enter the name of your brewery: ")
    uniquePasscode = input("Enter your passcode: ")

    for i in logbook:
        tempList1 = i.split("|")

    if  tempList1[0] == breweryName and tempList1[1] == uniquePasscode:
        account = breweryName
        print(f"Login Successful {breweryName}")

    else:
        print(f"Login Unsuccessfull, are you sure you have signed up?")

    logbook.close()

    return account

def addBrew():
    logbook = open("logbook.txt", "r")



