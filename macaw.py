import random
import string
import os
import json

# Authors: Kodle, Giiltham
# https://github.com/Lunarly

class macaw:
    
    def __init__(self, Fpath):
        self.data = self.loadJsonFile(Fpath)
        self.path = Fpath
    
    def createJsonFile(self, path):
        f = open(path,"a+")
        f.seek(0)
        if f.read() == "":
            f.write("{}")    
        f.close()
        
    def loadJsonFile(self, path):
        self.createJsonFile(path)
        f = open(path,"r+")
        self.data = json.loads(f.read())
        f.close()
        return self.data

    def saveJson(self,path):
        f = open(self.path,"w")
        json.dump(self.data,f)

    def randChar(self,x):
        return random.sample(string.ascii_letters, x)
        
    def randNum(self,y):
        digits = []
        for i in range(y):
            digits.append(str(random.randint(1,9)))
        return digits

    def randSymb(self,z):
        special = []
        for i in range(z):
            special.append(random.choice('!$%&()*+,-.:;<=>?@[]^_`{|}~'))
        return special

    def createPass(self, title):
        if title in self.data:
            print('Password already exist, use modify command.')
            return
        self.generatePass(title)
        
    def modifyPass(self, title):
        if (not title in self.data):
            print('Password doesn\'t exist')
            return
        self.generatePass(title)

    def deletePass(self, title):
        if title in self.data:
            del self.data[title]
            print(title+' has been deleted.')
            self.saveJson(self.path)  
        else:
            print('Password doesn\'t exist.')       
            
    def generatePass(self, title):
        char = input('Characters > ')
        num = input('Numbers > ')
        symb = input('Symbols > ')

        passw = self.randChar(int(char)) + self.randNum(int(num)) + self.randSymb(int(symb))
        random.shuffle(passw)
        
        self.savePass(title, passw)

    def savePass(self, title, passw):
        self.data[title] = ''.join(passw)

        print('\n' + title + ' : ' + ''.join(passw) + '\n' + 'Saved in pass.json')

        self.saveJson(self.path)

    def searchPass(self,title):
        if title in self.data:
            print(title + ' : ' + self.data[title])
        else:
            print('Password doesn\'t exist')

    def listPass(self):
        for key in self.data.keys():
            print(key)

    def commands(self):
        print('create - generate password \nmodify - modify password \ndelete - delete a password \nsearch - search a password \nlist - list of password \nexit - exit command')

jsonFileName = 'pass.json'

_init = macaw(jsonFileName)
createPass = _init.createPass
modifyPass = _init.modifyPass
deletePass = _init.deletePass
searchPass = _init.searchPass
listPass = _init.listPass
commands = _init.commands