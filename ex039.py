from datetime import date
sexo = str(input('Você é do sexo \033[36mmasculino\033[m ou \033[35mfeminino\033[m? ')).strip().lower()
if sexo == 'masculino':
    print('Para os homens o alistamento é \033[4mobrigatório\033[m. Vamos verificar o seu!')
    ano_nascimento = int(input('\033[32mDigite o seu ano de nascimento: '))
    idade = date.today().year - ano_nascimento
    print(f'\033[35mQuem nasceu em {ano_nascimento} tem {idade} anos em {date.today().year}.')
    if idade < 18:
        print(f'\033[33mFaltam {18 - idade} anos para você se alistar ao serviço militar!\033[36m \nSeu alistamento '
              f'será em {ano_nascimento + 18}.')
    elif idade == 18:
        print(f'\033[34mJá está na hora de você se alistar!')
    else:
        print(f'\033[33mVocê já deveria ter se alistado há {idade - 18} anos.\033[36m \nSeu alistamento foi em '
          f'{ano_nascimento + 18}.')
elif sexo == 'feminino':
    print('Você não precisa fazer o alistamento, é obrigatório somente aos homens.')
else:
    print('\033[31mOpção inválida. Tente novamente.\033[m')
# corrigido
