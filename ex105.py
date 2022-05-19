def notas(*notas, sit=False):
    '''
    Serve para analizar notas de alunos
    :param notas: os valores das notas recebidos
    :param sit: pergunta se o usuário quer saber a situação: caso for True, mostra a situação, se não, não mostra
    :return: retorna o dicionário Turma com os dado analizados.
    09/12/2021
    '''
    print(notas)
    turma = dict()
    turma['total'] = len(notas)

    c = maior = menor = soma = 0
    for v in notas:
        soma += v
        if c == 0:
            maior = menor = v
        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v
        c += 1

    turma['maior'] = maior
    turma['menor'] = menor
    turma['media'] = soma / len(notas)

    if sit:
        if turma['media'] <= 5:
            turma['situação'] = 'Ruim'
        elif turma['media'] <= 6:
            turma['situação'] = 'Razoável'
        else:
            turma['situação'] = 'Boa'
    print(turma)


# programa principal
resp = notas(5.5, 2.5, 1.5, sit = True)
help(notas)
