noteAll = input().split()
n1, n2, n3, n4 = noteAll

media = ((float(n1) * 2) + (float(n2) * 3) + (float(n3) * 4) + (float(n4) * 1)) / 10
print('Media: %.1f' %media)
if media >= 7:
    print('Aluno aprovado')
if media <= 5:
    print('Aluno reprovado')
if 5.0 <= media <= 6.0:
    print('Aluno em exame.')
    n5 = float(input())
    print('Nota do exame: %.1f' %n5)
    mediaFinal = (n5 + media) / 2
    if mediaFinal >= 5:
        print('Aluno aprovado.')
        print('Media final: %.1f' %mediaFinal)
    else:
        print('Aluno reprovado.')
        print('Media final: %.1f' %mediaFinal)
