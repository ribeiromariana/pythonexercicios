print('=' * 10, 'lOJAS MARIANA', '=' * 10)
valor = float(input('\033[35mValor das compras: R$'))
print('\033[1;36mFORMAS DE PAGAMENTO: \033[m')
print('[1]: à vista dinheiro/cheque. \n[2]: à vista cartão. \n[3]: 2x no cartão. \n[4]: 3x ou mais no cartão.')
pagamento = int(input('\033[35mQual foi a opção escolhida?\033[m '))
if pagamento == 1:
    print(f'Pagando À VISTA NO DINHEIRO/CHEQUE, o preço final fica: R${valor - valor * 10 / 100:.2f}!')
elif pagamento == 2:
    print(f'Pagando À VISTA NO CARTÃO, o preço final fica: R${valor - valor * 5 / 100:.2f}!')
elif pagamento == 3:
    print(f'Pagando em 2x NO CARTÃO, cada parcela vai custar R${valor / 2:.2f}, SEM JUROS!!')
    print(f'O valor final da compra fica R${valor:.2f}!')
elif pagamento == 4:
    parcelas = int(input('Em quantas vezes? '))
    valor_final = valor + valor * 20 / 100
    print(f'Pagando em {parcelas}x NO CARTÃO, cada parcela vai ficar \033[33mR${valor_final / parcelas:.2f}\033[m. ')
    print(f'O valor final do produto fica \033[36mR${valor_final:.2f}, COM JUROS\033[m!')
else:
    print('\033[31mOpção inválida. Tente novamente.\033[m')
# corrigido
