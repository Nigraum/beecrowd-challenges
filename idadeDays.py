days = int(input())

year = days // 365
days = days - year * 365

month = days // 30
days = days - month * 30

day = days
print('{} ano (s)'.format(year))
print('{} mes (es)'.format(month))
print('{} dia (s)'.format(day))
