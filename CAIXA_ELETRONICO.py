from variaveis.variavel import *

print("")
print("iniciando seu caixa eletronico")  
time.sleep(0.9)
print("")

# confirmação de dados pessoais
def cadastro():
    global nome

    nome = input("Me Informe o seu Nome: ")
    time.sleep(0.5)
    print("")

    print("Seja Bem Vindo,", nome,"!")
    print("")
    time.sleep(0.5)

    cpf = int(input("Me Informe o Seu Cpf, Por Favor!: "))
    print("")
    time.sleep(0.5)

    # confirmação se o cpf ta certo

    print("Confirma Que o CPF a Seguir Está Correto?: ", cpf)
    print("")
    time.sleep(0.3)

    print("1 - Confirmo")
    print("2 - Escrever Novamente")
    print("")

    confirmação = input("Sua Resposta: ")
    time.sleep(1.5)
    print("")


    if confirmação == "1":
        print("")
        print("CPF Confirmado Com Sucesso!")
        time.sleep(0.4)

    elif confirmação == "2":
        print("")
        time.sleep(0.4)

        cpf = int(input("Me Informe o Seu Cpf, Por Favor!: "))
        print("cpf sendo atualizado")
        time.sleep(0.9)
        print("")

        print("Cpf atualizado com Sucesso")
        print("")

    else:
        print("")
        print("Opção Inválida")
        print("")

    print("Armazenando Seus Dados")
    time.sleep(1)
    print("")

    print("---------------------------------")
    print("")
    print("Confirme Seus Dados Abaixo")
    print("")

    print("nome:", nome)
    print("CPF:", cpf)
    print("")

    print("CONFIRME COM NUMEROS")
    print("")

    print("1 - Sim")
    print("2 - Não")
    print("")

    confirmação_geral = input("Os Dados Estão Corretos?: ")
    print("")

    contato = ""

    if confirmação_geral == "1":
        print("Perfeito, Vamos Para o Próximo Passo!")
        time.sleep(1)
        print("")

        print("Me Informe o Seu Contato")
        time.sleep(1)
        print("")

        contato = input("Escreva Aqui Seu Numero de Celular: ")
        print("")
        time.sleep(1)

        print("Estamos Salvando o Seu Contato")
        print("")
        time.sleep(1.5)

        print("Contato Salvo Com SUCESSO: ", contato)
        print("")

    elif confirmação_geral == "2":
        print("reabra o programa novamente")

    else:
        print("")
        print("Error")


    print("---------------------------------")
    print("")
    print("Seus dados")
    print("")

    print("nome:", nome)
    print("CPF:", cpf)
    print("Contato:", contato)
    print("")
    print("Seu Saldo Atual é: ", saldo)
    print("")
    print("---------------------------------")
    print("")
    
    menu() # chamando o menu

# funções / if 

def menu(): #função chamado pelo "cadastro"

    print("O Que Deseja Realizar Hoje,",nome,"?")
    print("")

    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Realizar Pix")
    print("4 - Sacar")

    print("")

    ação = input("Qual Vamos Prosseguir? ")  # todos os if / elif seguem o padrão do INPUT "ação"

    if ação == "1":
        ver_saldo() # função criada para ver o saldo
        redirector() # função criada para redirecionar para o menu sem precisar repitir função

    elif ação == "2":
        deposito() # função para aumentar o valor do deposito
        redirector() # função criada para redirecionar para o menu sem precisar repitir função

    elif ação == "3":
        pix()
        redirector()

    elif ação == "4":
        sacar() # função para sacar, dinimui o valor do saldo
        redirector() # função criada para redirecionar para o menu sem precisar repitir função


# funções 

def ver_saldo():
    print("Seu Saldo Atual é:", saldo)
    print("")

def deposito():
    global saldo
    valordep = int(input("Selecione o Valor a Ser Depositado: "))
    saldo += valordep
    print("Seu Saldo Atual é: ", saldo)

def pix():
    global saldo
    valorpix = int(input("Selecione o Valor: "))
    contapix = input("Digite a Chave Pix: ")
    print("BANCO TESTE, NOME: MATEUS", contapix)
    time.sleep(1.3)
    print("")
    print("BANCO: ", contapix)
    print("VALOR:", valorpix)
    print("")
    time.sleep(1)

    print("1 - SIM")
    print("2 - NÃO")
    print("")

    confirmapix = input("Confirma que os dados Acima Estão Corretos?: ")
    print("")

    if confirmapix == "1":
       print("Estamos Realizando a Transação..")
       print("")
       time.sleep(1)
       saldo -= valorpix
       print("Seu Saldo Atual é: ", saldo)
       print("Transação Realizada Com Sucesso")
       time.sleep(0.8)
       redirector()

    elif confirmapix == "2":
        print("")
        time.sleep(1)
        print("Reiniciando Processo Pix")
        print("")
        pix()

    else:
        ("")

def sacar():
    global saldo
    sacar = int(input("Selecione o Valor do Saque: "))
    saldo -= sacar
    print("Seu Saldo Atual é: ", saldo)

    
def redirector():
        time.sleep(3)
        print("")
        print("Redirecionando Para o Menu..")
        print("")
        time.sleep(1.8)
        menu()

cadastro()

