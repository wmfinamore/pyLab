"""
Este é o módulo "iteratelist.py", e fornece uma função chamada
print_lol() que imprime listas que podem ou não
incluir listas aninhadas
"""
def print_lol(the_list, tab=False, level=0):
    """
    Esta função requer um argumento posicional
    chamdo "the_list", que é qualquer lista
    Python(de possíveis listas aninhadas).
    Cada item de dados na lista fornecida
    é (recursivamente) impresso na tela em
    sua própria linha.
    Um segundo argumento indica se será usada
    tabulação entre is niveis da lista(boolean).
    Um terceiro argumento chamado "level"
    é usado para inserir tabulações quando
    uma lista aninhada é encontrada.
    """
    l = level
    t = tab
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item,t, l+1)
        else:
            """
            Usa o valor de "level" para 
            controlar o número de tabulações
            a serem usadas.
            """
            if t:
                for tab in range(l):
                    """
                    Exiba um caracter TAB
                    para cada nível de recuo
                    """
                    print("\t", end='')
            print(each_item)