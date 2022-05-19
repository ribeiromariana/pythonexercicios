peso = float(input('Digite o seu peso: kg'))
altura = float(input('Digite a sua altura: m'))
imc = peso / altura ** 2
print(f'\033[34mO seu IMC é de {imc:.2f}.\033[m')
if imc < 18.5:
    print('\033[33mVocê está ABAIXO do peso normal!')
elif 18.5 <= imc <= 25:
    print('\033[32mParabéns, você está no PESO IDEAL!')
elif 25 < imc <= 30:
    print('\033[31mVocê está com SOBREPESO!')
elif 30 < imc <= 40:
    print('\033[31mVocê está com OBESIDADE!')
else:
    print('\033[31mCuidado, você está com OBESIDADE MÓBIDA!\033[m')
# corrigido
