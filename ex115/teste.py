from ex115.menu.interface import *
from ex115.menu.arquivo import *

arq = 'pessoas.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

menu(['Pessoas cadastradas', 'Adicionar nova pessoa', 'Encerrar programa', 'Resetar arquivo'])

#escrevearquivo(arq, 'Maria Dolores, 57 anos')
