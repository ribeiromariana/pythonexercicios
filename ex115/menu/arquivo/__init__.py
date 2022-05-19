def arquivoexiste(nome):
    try:
        open(nome, 'rt')
    except:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Ocorreu um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
        print(a.read())
        a.close()
    except:
        print('Ocorreu um erro e não conseguimos ler o arquivo solicitado.')


# 'a' = Escrita. Insere os novos dados no final do arquivo


def escrevearquivo(nome, txt):
    try:
        arq = open(nome, 'a')
        arq.write(f'{txt}\n')
        arq.close()
        lerarquivo(nome)
    except:
        print('algo de errado aconteceu!')


def organizararq(nome, pessoa, idade):
    try:
        arq = open(nome, 'a')
        arq.write(f'{pessoa:<30} \t{idade} anos\n')
        arq.close()
    except:
        print('Erro!')
    else:
        print(f'{pessoa} foi cadastradx com sucesso!')


def resetararq(nome):
    try:
        arq = open(nome, 'w')
        arq.close()
    except:
        print('Erro!')
