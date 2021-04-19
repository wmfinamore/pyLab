"""
Este é o módulo "iteratelist.py", e fornece uma função chamada
print_lol() que imprime listas que podem ou não
incluir listas aninhadas
"""
def print_lol(the_list, level=0):
    """
    Esta função requer um argumento posicional
    chamdo "the_list", que é qualquer lista
    Python(de possíveis listas aninhadas).
    Cada item de dados na lista fornecida
    é (recursivamente) impresso na tela em
    sua própria linha
    Um segundo argumento chamado "level"
    é usado para inserir tabulações quando
    uma lista aninhada é encontrada.
    """
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level+1)
        else:
            """
            Usa o valor de "level" para 
            controlar o número de tabulações
            a serem usadas
            """
            for tab in range(level):
                """
                Exiba um caracter TAB
                para cada nível de recuo
                """
                print("\t", end='')
            print(each_item)