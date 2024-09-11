print('exercise 1')
seasons = ('spring', 'summer', 'fall', 'winter')
month = int(input('enter a month in the year: '))
if month == 12 or 2>=month>=1:
    print(f'{month} is during season: {seasons[3]}')
elif 5 >= month >= 3:
    print(f'{month} is during season: {seasons[0]}')
elif 8 >= month >= 6:
    print(f'{month} is during season: {seasons[1]}')
elif 11 >= month >= 9:
    print(f'{month} is during season: {seasons[2]}')
