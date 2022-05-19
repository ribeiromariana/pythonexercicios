import webbrowser
try:
    test = webbrowser.open('http://www.pudim.com.br')
except:
    print('\033[31mNão consegui acessar o site do pudim :(\033[m')
else:
    print('\033[92mConsegui acessar o site do pudim!\033[m')

