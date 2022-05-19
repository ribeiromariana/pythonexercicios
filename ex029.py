velocidade = float(input('Digite a velocidade do veículo: Km'))
if velocidade > 80:
    print('Você foi multado!')
    multa = (velocidade - 80) * 7.00
    print(f'O valor da multa é de R${multa:.2f}. Tenha mais atenção na próxima!')
else:
    print('Está na velocidade correta, não ultrapasse 80km/h!')
print('Tenha um bom dia! E Dirija com segurança!')
# Corrigido
