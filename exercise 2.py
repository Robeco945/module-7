print('exercise 2')
i = 0
names = set()
ini = len(names)
name = (input('enter a name or press enter to stop: '))
while name != '':
    name =(input('enter a name or press enter to stop: '))
    if name in names:
        print('Existing name')
    elif name not in names:
        names.add(name)
        print('New name')

