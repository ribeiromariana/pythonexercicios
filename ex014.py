celsius = float(input('\033[31mQual a temp\033[34meratura? C°:\033[m'))
cor = '\033[31m'
if celsius < 27:
    cor = '\033[34m'
fahrenheit = celsius * 1.8 + 32
print(f'A temperatura {cor}{celsius:.1f}C°\033[m, equivale a \033[35m{fahrenheit:.1f}F°\033[m!')
