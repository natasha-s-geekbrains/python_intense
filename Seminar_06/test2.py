# my_str = 'Раз, два, три'
#
# a, b, c = str.split(',')
# print(a, b, c)

full_date = '15.4.2022'

date, month, year = (int(item) for item in full_date.split('.'))
print(date, month, year)
