nota1 = float(input('\033[35mPrimeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print(f'\033[mCom as notas {nota1:.1f} e {nota2:.2f} a média do aluno é de {media:.1f}!')
corac = '\033[31m<3\033[m'
if media < 5:
    print(f'\033[31mVocê foi REPROVADO! \n\033[36mTente se esforçar mais na próxima! {corac}')
elif 5 <= media < 7:
    print(f'\033[33mVocê está de RECUPERAÇÃO!\033[32m \nBoa sorte! {corac}')
else:
    print(f'\033[34mVocê foi APROVADO!\033[33m \nParabéns, continue assim! {corac}')
# CORRIGIDO
