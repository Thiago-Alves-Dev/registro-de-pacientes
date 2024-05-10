"""_summary_

    REGISTRO DE PACIENTES
        ----------------------------------------------------
        Este módulo tem como objetivo registrar pacientes no terminal
        do python usando um while True com os seguintes dados:
        - nome completo
        - e-mail
        - cpf
        - rg
        - telefone
        - data de nascimento
        ------------------------------------------------------

        Após o registro o código faz:

            - Cálculo com base na data de nascimento
            para atualizar a idade atual do paciente.

            - Ajusta a idade caso o paciente ainda não tenha feito
            aniversário esse ano.

            - Caso o paciente tenha 65 anos ou mais o código adiciona
            um arquivo .txt com pacientes no grupo de risco.

            - Caso o paciente tenha menos de 65 anos o código adiciona
            um arquivo .txt com pacientes em um grupo normal.

        Extras:

            - Adição de duas funções que limpa o terminal do
            python para uma melhor visualização.

"""
from datetime import datetime
from os import name, system, path

pacientes = {}
diretorio_atual = path.dirname(__file__)
caminho_arquivo_1 = path.join(diretorio_atual, 'grupo_de_risco.txt')
caminho_arquivo_2 = path.join(diretorio_atual, 'pacientes.txt')


def cadastrar_paciente(nome, email, cpf, rg, tel, data_nasc, idade):
    if cpf in pacientes:
        print("CPF já cadastrado. Por favor, insira um CPF diferente.")
        return False

    # Adiciona o novo paciente ao dicionário de pacientes
    pacientes[cpf] = {
        'nome': nome,
        'email': email,
        'rg': rg,
        'tel': tel,
        'data_nascimento': data_nasc,
        'idade': idade
    }

    print("\n Paciente cadastrado com sucesso! \n")
    any_key()
    return True


def calcular_idade(data_nasc):
    # convertendo a data de nascimento para uma string
    data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y")

    # data atual
    data_atual = datetime.now()

    # calculando a idade
    idade = data_atual.year - data_nasc.year

    # Ajustando a idade se ainda não tiver feito aniversário este ano
    if data_atual.month < data_nasc.month or (
        data_atual.month == data_nasc.month and
        data_atual.day < data_nasc.day
    ):
        idade -= 1

    return idade


# Função para limpar o terminal
def clear_terminal():
    # Verifica o sistema operacional
    if name == 'nt':   # Windows
        system('cls')


# input para chamar a função clear_terminal()
def any_key():
    input('pressione qualquer tecla para continuar: ')
    clear_terminal()


while True:
    print('\n SISTEMA DE PACIENTES \n')
    print('1 - registrar pacientes')
    print('2 - lista de pacientes')
    print('3 - sair \n')
    inp = input('digite aqui: ')
    clear_terminal()

    if inp == '1':
        print('\n REGISTRO DE PACIENTES \n')
        nome = input('nome completo do paciente: ')
        email = input("Digite o email do paciente: ")
        cpf = input("Digite o CPF do paciente: ")
        rg = input("Digite o RG do paciente: ")
        tel = input('Digite o número de telefone: ')
        data_nasc = input("Digite a data de nascimento: ")
        idade = calcular_idade(data_nasc)
        clear_terminal()

        new_data = f"""
Registro geral n° {rg}

    nome do paciente: {nome}
    email: {email}
    cpf: {cpf}
    telefone: {tel}
    data de nascimento (ex: 00/00/0000): {data_nasc}
    idade: {idade} anos \n
"""

        if idade >= 65:
            with open(caminho_arquivo_1, 'a', encoding='utf-8') as rec_file:

                rec_file.write(new_data)
        else:
            with open(caminho_arquivo_2, 'a', encoding='utf-8') as rec_file:

                rec_file.write(new_data)

        cadastrar_paciente(nome, email, cpf, rg, tel, data_nasc, idade)
    elif inp == '2':
        clear_terminal()
        print('últimos pacientes cadastrados: \n')
        print(f'{pacientes} \n')
        any_key()
    elif inp == '3':
        break
    else:
        print('digite algo válido')
        any_key()
