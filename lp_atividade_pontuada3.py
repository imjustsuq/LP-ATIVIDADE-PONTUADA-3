import os

os.system('cls')

# Vetores
vetor_aviao = ['', '', '', '']
vetor_assentos = ['', '', '', '']
reservas = []
MAX_RESERVAS = 20

# Função que exibe o menu de opções
def mostrar_menu():
    print("""
                            MENU DE OPÇÕES

        Código  |       Opções                                                      |
            1   |  Registrar o número de cada avião                                 |
            2   |  Registrar o quantitativo de assentos disponíveis em cada avião   |
            3   |  Reservar passagem aérea                                          |
            4   |  Realizar consulta por avião                                      |
            5   |  Realizar consulta por passageiro                                 |
            6   |  Encerrar sistema                                                 |
    """)

# Função para registrar aviões
def registrar_avioes():
    print('Passageiro escolheu: Registrar o número do avião.')
    for i in range(4):
        vetor_aviao[i] = int(input(f'Registre o número do {i + 1}° avião: '))

# Função para registrar os assentos
def registrar_assentos():
    print('Passageiro escolheu: Registrar o quantitativo de assentos disponíveis em cada avião')
    for i in range(4):
        vetor_assentos[i] = int(input(f'Registre a quantidade de assentos para o avião {vetor_aviao[i]}: '))

# Função para realizar a reserva de passagem
def reservar_passagem():
    if len(reservas) >= MAX_RESERVAS:
        print('Limite de reservas atingido!')
        return
    
    numero_aviao = int(input('Digite o número do avião para a reserva: '))
    if numero_aviao not in vetor_aviao:
        print("Este avião não existe!")
        return
    
    indice_aviao = vetor_aviao.index(numero_aviao)
    if vetor_assentos[indice_aviao] <= 0:
        print("Não há assentos disponíveis para este avião!")
        return
    
    nome_passageiro = input('Digite o nome do passageiro: ')
    
    # Criar a reserva
    reservas.append((numero_aviao, nome_passageiro))

    vetor_assentos[indice_aviao] -= 1
    print("Reserva realizada com sucesso!")

# Função para consultar reservas por avião
def realizar_consulta_aviao():
    numero_aviao = int(input('Digite o número do avião para consulta: '))
    if numero_aviao not in vetor_aviao:
        print("Este avião não existe!")
        return
    
    reservas_aviao = [nome for num, nome in reservas if num == numero_aviao]
    
    if reservas_aviao:
        print(f'Reservas para o avião {numero_aviao}:')
        for nome in reservas_aviao:
            print(f'- {nome}')
    else:
        print("Não há reservas realizadas para este avião!")

# Função para consultar reservas por passageiro
def realizar_consulta_passageiro():
    nome_passageiro = input('Digite o nome do passageiro para consulta: ')
    aviões_reservados = [num for num, nome in reservas if nome == nome_passageiro]

    if aviões_reservados:
        print(f'{nome_passageiro} tem reservas nos seguintes aviões:')
        for numero in aviões_reservados:
            print(f'- Avião {numero}')
    else:
        print("Não há reservas realizadas para este passageiro!")

# Função principal para controlar o menu e loop
def main():
    while True:
        mostrar_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida! Digite um número entre 1 e 6.")
            continue
        if opcao == 1:
            registrar_avioes()
        elif opcao == 2:
            registrar_assentos()
        elif opcao == 3:
            reservar_passagem()
        elif opcao == 4:
            realizar_consulta_aviao()
        elif opcao == 5:
            realizar_consulta_passageiro()
        elif opcao == 6:
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Iniciar o sistema
if __name__ == '__main__':
    main()

