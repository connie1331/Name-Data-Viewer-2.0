#******************************************************************************
# Author:           Khanh Vu
# Lab:              Lab_7: Database use in Python
# Date:             02.15.2022
# Description:      The Name class is stored in a module named Name (Name.py). This code use object(s) from the
#                   Database class to define a static method. This code defines a constructor that stores values
#                   for name, year, gender, and count for the object. This code also has setters and getters for
#                   the 4 properties above. Then,it defines a static method called readName()
#                   which call Database.readName() and return its results.
# Sources:          Murach's Python Programming - Beginner... Chapter 14_ How to define and use your own classes
#                   Murach's Python Programming - Beginner... Chapter 16_ Database
#                   CIS-133Y- Python Programming I Lecture Notes - Module 6: OOP
#                   CIS-133Y- Python Programming I Lecture Notes - Module 7: Database Development
#                   Lab 6 specification
#******************************************************************************

class Name:

    # A constructor that take values for name, year, gender and count.

    def __init__(self, name="n/a", year=1900, gender="M", count=0):
        self.__name = name  # property 1
        self.__year = year  # property 2
        self.__gender = gender  # property 3
        self.__count = count  # property 3

    # Defines getters and setters for all properties

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, updatedName):
        self.__name = updatedName

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, updatedYear):
        self.__year = updatedYear

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, updatedGender):
        self.__gender = updatedGender

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, updatedCount):
        self.__count = updatedCount

    # Defines a static method called readName() which call Database.readName() and return its result.

    @staticmethod
    def readNames(year, gender):
        from Database import Database

        listOfnameDict = Database.readNames(year, gender)    # a list of name dictionary objects

        nameDatabase = []                       # an empty list to store list of Name object

        for i in listOfnameDict:    # converting the list of dictionary objects to a list of Name objects
            nameDatabase.append(Name(i['name'],
                                     i['year'],
                                     i['gender'],
                                     i['count']))
        return nameDatabase


