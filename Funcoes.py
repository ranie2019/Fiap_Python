def perguntar():
    return input('<I> - Para Inserir Um Usuario \n'
                 '<P> - Para Pesquisar Um Usuario \n'
                 '<E> - Para Excluir Um Usuario \n'
                 '<L> - Para Listar Um Usuario \n'
                 'Oque Deseja realizar? ').upper()


def inserir(dicionario):
    dicionario[input('Digite o Login: ').upper()] = [input('Digite o nome: ').upper(),
                                                     input('Digite a Ultima Data de Acesso: '),
                                                     input('Qual a Ultima estação De Acesso: ').upper()]
