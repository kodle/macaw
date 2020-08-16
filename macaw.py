import random
import string
import os
import json

# Author: Kodle, Giiltham
# https://github.com/Lunarly

print('Hello world! Welcome on Macaw.\nWrite help to see commands.\n')


def createJsonFile(path):
    f = open(path,"a+")
    f.seek(0)
    if f.read() == "":
        f.write("{}")    
    f.close()
    
def loadJsonFile(path):
    f = open(path,"r+")
    data = json.loads(f.read())
    f.close()
    return data

def saveJson(path):
    f = open(path,"w")
    json.dump(data,f)

def randChar(x):
    return random.sample(string.ascii_letters, x)
    
def randNum(y):
    digits = []
    for i in range(y):
        digits.append(str(random.randint(1,9)))
    return digits

def randSymb(z):
    special = []
    for i in range(z):
        special.append(random.choice('!$%&()*+,-.:;<=>?@[]^_`{|}~'))
    return special

def createPass():
    title = input('Name > ')
    if title in data:
        print('Password already exist, use modify command.')
        return
    generatePass(title)
    
def modifyPass():
    title = input('Name > ')
    if (not title in data):
        print('Password doesn\'t exist')
        return
    generatePass(title)

def deletePass():
    delete = input('Delete > ')
    if delete in data:
        del data[delete]
        print(delete+' has been deleted.')
        saveJson('pass.json')  
    else:
        print('Password doesn\'t exist.')       
        
def generatePass(title):
    char = input('Characters > ')
    num = input('Numbers > ')
    symb = input('Symbols > ')

    passw = randChar(int(char)) + randNum(int(num)) + randSymb(int(symb))
    random.shuffle(passw)
    
    savePass(title, passw)
    
def savePass(title, passw):
    data[title] = ''.join(passw)

    print('\n' + title + ' : ' + ''.join(passw) + '\n' + 'Saved in pass.json')

    saveJson(jsonFileName)

def searchPass():
    search = input('Search > ')
    if search in data:
        print(search + ' : ' + data[search])
    else:
        print('Password doesn\'t exist')

def listPass():
    for key in data.keys():
        print(key)
    
def help():
    print('create - generate password \nmodify - modify password \ndelete - delete a password \nsearch - search a password \nlist - list of password \nexit - exit command')

jsonFileName = "pass.json"

createJsonFile(jsonFileName)

data = loadJsonFile(jsonFileName)
    
    
while(True):
    cmd = input('Command > ')

    if cmd == 'create':
        createPass()
        
    elif cmd == 'modify':
        modifyPass()

    elif cmd == 'delete':
        deletePass()

    elif cmd == 'search':
        searchPass()
        
    elif cmd == 'list':
        listPass()

    elif cmd == 'help':
        help()

    elif cmd == 'exit':
        print('Goodbye!')
        break

    else:
        print('Command doesn\'t exist. Use help to show commands.')