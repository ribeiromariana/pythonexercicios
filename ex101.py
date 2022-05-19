def voto(nasc):
    """Tem como objetivo identificar a idade do usuário e descobrir qual o estado de voto dessa pessoa.
    :param nasc: serve para ler o ano de nascimento
    :return: Retorna o estado de voto do indivíduo
    04/12/2021"""
    from datetime import date
    from time import sleep
    print('¬¬' * 33)
    idade = date.today().year - nasc
    print(f'Com \033[36m{idade} anos\033[m...')
    sleep(0.5)
    if idade < 16:
        return "\033[93mNegado\033[m"
    elif idade < 18 or idade > 65:
        return "\033[92mOpcional\033[m"
    elif idade < 65:
        return '\033[35mObrigatório\033[m'


data = int(input('Digite a sua data de nascimento para saber o seu direito de voto: '))
c = voto(data)
print(f'O seu estado de voto é {c}')
help(voto)
