print('exercise 3')

ICAOs = {'EFHK':'Helsinki-Vantaa Airport'}

choice = int(input('Enter "1" if you want to add a new airport,\n "2" to retrieve an existing airport,\n "3" to quit\n '))
while choice != '' or choice != 2 or choice != 1:
    if choice == 3:
        break
    elif choice == 1:
        i = input('Enter airport name: ')
        n = input("Enter airport's ICAO code ")
        ICAOs[n] = i
    elif choice == 2:
        req = input('Enter airport ICAO code: ')
        if req in ICAOs:
            print(f'the airport with that ICAO code is {ICAOs[req]}\n')
    choice = int(input('Enter "1" if you want to add a new airport,\n "2" to retrieve an existing airport,\n "3" to quit\n '))

