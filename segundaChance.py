qtd_alunos = int(input())

alunos = []
for i in range(qtd_alunos):
    aluno = {}

    aluno['nota_original'] = float(input())
    aluno['nota_final'] = aluno['nota_original']

    alunos.append(aluno)

notas_alteradas = 0
for aluno in alunos:
    aluno['nota_nova'] = float(input())

    if aluno['nota_nova'] == 10:
        aluno['nota_final'] = aluno['nota_original'] + 2
        if aluno['nota_final'] > 10:
            aluno['nota_final'] -= aluno['nota_final'] % 10

    if aluno['nota_final'] != aluno['nota_original']:
        notas_alteradas += 1

    else:
        aluno['nota_final'] = aluno['nota_original']

print(f'NOTAS ALTERADAS: {notas_alteradas}')
i = 1
for aluno in alunos:
    if aluno['nota_final'] != aluno['nota_original']:
        print('* ', end='')
    else:
        print('- ', end='')
    print(
        f'({i:03d}) original: {aluno["nota_original"]} | final: {aluno["nota_final"]}')
    i += 1
