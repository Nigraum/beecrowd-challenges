n = int(input())
hours = n // 60 ** 2
n = n - hours * 60 ** 2

minutes = n // 60
n = n -  minutes * 60

seconds = n

print('{}:{}:{}'.format(hours, minutes, seconds))
