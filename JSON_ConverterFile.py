from decimal import Decimal
from dataclasses import dataclass
from bankInfo import UserBank

import json

@dataclass
class User:
    id : int
    name : str
    age : int
    money : Decimal



class JSONCreator:
    def __init__(self,filename) :
        self.filename = filename
        self.data = []

    def AddUserData(self, user: User):
        user_data =  {
            "id" : user.id,
            "name" : user.name,
            "age" : user.age,
            "money" : user.money
        }
        self.data.append(user_data)

    def AddUserBankInfo(self, userBank : UserBank):
        user_bank =  {
            "firstName" : userBank.user_firstName,
            "lastName" : userBank.user_lastname,
            "Gross" : str(userBank.user_gross),
            "Returns" : str(userBank.user_returns),
            "Net" : str(userBank.user_net)
        }
        self.data.append(user_bank)

    def saveFile(self):
        with open(self.filename,'w') as file:
            json.dump(self.data,file,indent=4)
