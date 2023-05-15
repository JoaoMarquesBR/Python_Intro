from decimal import Decimal
from dataclasses import dataclass
from JSON_ConverterFile import User,JSONCreator
from BankInformation import TextReading
from bankInfo import Branch,UserBank
import json

# Checks if argument being passed is INT or not
def testArgs(id):
    if isinstance(id,int):
        print(f"Integer was passed, it is {id}")
    else:
        print("Value passed isn't an int")

#Creates and returns USER
def createUser(id,name,age,money):
    newUser = User(
        id = id,
        name = name,
        age = age,
        money = money
    )
    # print(f"User created = {newUser}")
    return newUser

#Create list of Users
userList = []
userList.append(createUser(1,"Joao",18,1400.53))
userList.append(createUser(2,"Pedroca",21,800.40))
userList.append(createUser(3,"Vini",25,2340.43))
userList.append(createUser(4,"Franco",15,1240.43))
userList.append(createUser(5,"Hype",23,5400.43))

# print(userList)
myJSON = JSONCreator("example.json")

for user in userList:
    print(user)
    myJSON.AddUserData(user)

myJSON.saveFile()

#READ BANKINFO.TXT and Print IT and FORMAT IT!

def readBankInfo(bankLine):
    userBank = UserBank(
        user_firstName  = bankLine[20:30].replace(" ",""),
        user_lastname   = bankLine[5:15].replace(" ",""),
        user_gross      = (Decimal(bankLine[30:37])),
        user_returns    = (Decimal(bankLine[37:43])),
        user_net        = (Decimal(bankLine[30:37])-Decimal(bankLine[37:43]))
    )
    return userBank
    

myBankJSON = JSONCreator("bankUsers.json")

#Create list of each line of bank TXT document
reading = TextReading
bankList = reading.getBankLines()
for userBank in bankList:
    myBankJSON.AddUserBankInfo(readBankInfo(userBank))

myBankJSON.saveFile()

# readBankInfo(bankList)



    
    








