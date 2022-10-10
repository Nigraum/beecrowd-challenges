import math

inputs = input().split()
a, b, c = inputs

maiorAB = (int(a) + int(b) + abs(int(a) - int(b))) / 2
total = (int(maiorAB) + int(c) + abs(int(maiorAB) - int(c))) / 2
print('%d eh o maior' %total)
