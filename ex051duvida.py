primeiro_t = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
proximo_t = primeiro_t
for c in range(0, 10):
    print(proximo_t, end=' -> ')
    proximo_t = proximo_t + razao
    if c == 9:
        print('ACABOU!')
# + ou -
