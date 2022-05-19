distance = float(input('Digite a distância da sua viagem: Km'))
if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45
print(f'O preço da passagem para uma viagem de {distance:.1f}Km é de: R${price:.2f}. \nTenha uma ótima viagem!!')
# Corrigido
