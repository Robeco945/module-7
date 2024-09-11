print('exercise 2')
i = 0
names = set()
ini = len(names)
name = (input('enter a name or press enter to stop: '))
while name != '':
    name =(input('enter a name or press enter to stop: '))
    names.add(name)
    if len(names) > ini:
        print("new name")
  #  elif len(names) < i:
   #     print('existing name')
#the len only increases when a new name is added,
# we can know if its a new name or not by seeing
# if the len has increased
