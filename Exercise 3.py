print('exercise 3')

ICAOs = {'EFHK':'Helsinki-Vantaa Airport'}

choice = int(input('Enter "1" if you want to add a new airport, "2" to retrieve an existing airport, "3" to quit'))
while True:
    choice = int(input('Enter "1" if you want to add a new airport, "2" to retrieve an existing airport, "3" to quit'))
    if choice == 3:
        break
    if choice == 2:
        i = input('Enter airport name: ')
        n = input("Enter airport's ICAO code ")


