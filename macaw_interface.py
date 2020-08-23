import macaw

print('Hello world! Welcome on Macaw.\nWrite \'commands\' to see commands.\n')

while(True):
    cmd = input('Command > ')

    if cmd == 'create':
        title = input('Name > ')
        macaw.createPass(title)
        
    elif cmd == 'modify':
        title = input('Name > ')
        macaw.modifyPass(title)

    elif cmd == 'delete':
        title = input('Delete > ')
        macaw.deletePass(title)

    elif cmd == 'search':
        title = input('Search > ')
        macaw.searchPass(title)
        
    elif cmd == 'list':
        macaw.listPass()

    elif cmd == 'commands':
        macaw.commands()

    elif cmd == 'exit':
        print('Goodbye!')
        break

    else:
        print('Command doesn\'t exist. Use \'commands\' to get a list of all the commands.')