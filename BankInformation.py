from io import open

class TextReading:  
    def __init__(self):
        pass

    def getBankLines():
        bankLines = []
        with open('bankinfo.txt','r') as file:
         for line in file.readlines():
            bankLines.append(line)
        return bankLines
            




