#******************************************************************************
# Author:           Khanh Vu
# Lab:              Lab_7: Database use in Python
# Date:             02.22.2022
# Description:      The main (main.py) contains the main code of the program. This code imports the Name class
#                   from the Name module. The main code asks user to enter value for the search criteria
#                   and use the readNames() method from Name module to fetch the matching Name objects.
#                   Then, it should write those objects to the console.
#                   The program need to validate user inputs. Gender should be restricted to M or F, Year
#                   should be a whole number between 1915 and 2014, Name should be non-empty, and NameCount should
#                   be a whole number between 5 and 200,000.
# Inputs:           A List of Name objects whose properties are str name, str gender, int year, int count
#                   int year, str gender (user inputs)
# Outputs:          str name, str gender, int year, int count
# Sources:          Murach's Python Programming - Beginner... Chapter 14_ How to define and use your own classes
#                   Murach's Python Programming - Beginner... Chapter 16_ Database
#                   CIS-133Y- Python Programming I Lecture Notes - Module 6: OOP
#                   CIS-133Y- Python Programming I Lecture Notes - Module 7: Database Development
#                   Lab 6 specification
#******************************************************************************

from Name import Name


def main():
    print("NAME DATABASE")
    print("=============")
    print()
    # Ask user to input year
    while True:
        try:
            year = int(input("Select a year between 1915 and 2014: "))
        except ValueError:
            print("Invalid! Enter integer only. ")
            continue
        if year < 1915 or year > 2014:
            print ("The year must be between 1915 and 2014! Try again")
        else:
            break

    # Ask user to input year
    while True:
        gender = input("Enter gender: ")
        if gender.lower() == "m" or gender.lower() == "f":
            break
        else:
            print ("Please type M or F!")

    # Fetch name data from the Database by calling Name.readNames() method
    listOfNameObjects = Name.readNames(year, gender) # the readNames() method from the Name object return a list of Name objects

    # Print out the name data
    print()
    print("20 most popular names for", gender,  " babies in ", year, ":")
    print()
    print("{:<6} {:<15} {:8} {:<10}".format("Year", "Name", "Gender", "Count"))  # Print header

    for i in listOfNameObjects:             # each "i" is a Name object
        print("{:<6} {:<15} {:8} {:<10}".format(i.year, i.name, i.gender, i.count))


if __name__ == "__main__":
    main()
