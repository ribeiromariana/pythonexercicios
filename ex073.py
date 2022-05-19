times = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Fortaleza EC', 'Bragantino', 'Fluminense', 'Corinthians',
         'Internacional', 'Athletico-PR', 'Cuiabá', 'Atlético Goianiense', 'São Paulo', 'Ceará', 'Santos', 'Bahia',
         'Juventude', 'Grêmio', 'América-MG', 'Sport', 'Chapecoense')
print(f'Os CINCO PRIMEIROS colocados são: {times[:5]}')
print(f'Os ÚLTIMOS QUATRO colocados são: {times[-4:]}')
print(f'Times em ORDEM ALFABÉTICA: {sorted(times)}')
print(f'O time da Chapeconence está em {times.index("Chapecoense") + 1}ª colocado.')
