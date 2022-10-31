a = input()
b = input()
c = input()

if a == 'vertebrado' and b == 'ave' and c == 'carnivoro':
    d = 'aguia'

if a == 'vertebrado' and b == 'ave' and c == 'onivoro':
    d = 'pomba'

if a == 'vertebrado' and b == 'mamifero' and c == 'onivoro':
    d = 'homem'

if a == 'vertebrado' and b == 'mamifero' and c == 'herbivoro':
    d = 'vaca'

if a == 'invertebrado' and b == 'inseto' and c == 'hematofago':
    d = 'pulga'

if a == 'invertebrado' and b == 'inseto' and c == 'herbivoro':
    d = 'lagarta'

if a == 'invertebrado' and b == 'anelideo' and c == 'hematofago':
    d = 'sanguessuga'

if a == 'invertebrado' and b == 'anelideo' and c == 'onivoro':
    d = 'minhoca'

print(d)
