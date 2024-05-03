# Agenda básica que aprendi utilizando da linguagem de programação Python.
# 

AGENDA = {}

AGENDA["Vinicius"] = {
    "Telefone": "(51) 90907070",
    "Email": "vinicunhasilvaz@gmail.com",
    "Endereço": "Rua 1",
}
AGENDA["Guilherme"] = {
    "Telefone": "(51) 999999999",
    "Email": "exemplo@gmail.com",
    "Endereço": "Rua 2",
}
AGENDA["Johnny"] = {
    "Telefone": "(51) 988888888",
    "Email": "exemplo1@gmail.com",
    "Endereço": "Rua 3",
}


def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contatos(contato)
            print("-------------------------------------------")
    else:
        print()
        print("Agenda vazia.")
        print()


def buscar_contatos(contato):
            try:
                print("Nome:", contato)
                print("Telefone:", AGENDA[contato]['Telefone'])
                print("Email:", AGENDA[contato]['Email'])
                print("Endereço:", AGENDA[contato]['Endereço'])
            except:
                 print()
                 print("Contato não registrado.")
                 print()
                 print("Retornando ao menu...")
                 print()

def ler_detalhes_contato():
    Telefone = input("Digite o número de telefone: ")
    Email = input("Digite o email: ")
    Endereço = input("Digite o endereço: ")
    return Telefone, Email, Endereço

def add_editar_contato(contato, Telefone, Email, Endereço):
    AGENDA[contato] = {
         "Telefone": Telefone,
            "Email": Email,
                "Endereço": Endereço,
       
       } 
    salvar()


def excluir_contato(contato):
        try:
            AGENDA.pop(contato)
            salvar()
            print()
            print(">>>>> Contato {} excluído com sucesso!".format(contato))
            print()
            print("Retornando ao menu...")
            print()
        except:
             print()
             print("Contato inexistente. Verifique se digitou o nome correto e tente novamente.")
             print()
             print("Retornando ao menu...")
             print()


def salvar():
     exportar_contatos('database.csv')


def load():
     try:
          with open('database.csv', "r") as arquivo:
               linhas = arquivo.readlines()
               for linha in linhas:
                    detalhes = linha.strip().split(',')
                    nome = detalhes[0]
                    Telefone = detalhes[1]
                    Email = detalhes[2]
                    Endereço = detalhes[3]
                    AGENDA[nome] = {
         "Telefone": Telefone,
            "Email": Email,
                "Endereço": Endereço,
                    }
          print(">> {} contatos carregados com sucesso! <<".format(len(AGENDA)))
     except FileNotFoundError:
          print()
          print(">> Arquivo não encontrado. <<")
          print()
     except Exception as error:
          print()
          print("Algum erro inesperado aconteceu. Erro: ")
          print(error)
          print()     

def imprimir_menu():
       print("-------------------------------------------")
       print("1 - Mostrar todos os contatos da agenda")
       print("2 - Buscar um contato")
       print("3 - Adicionar um contato")
       print("4 - Editar um contato")
       print("5 - Excluir um contato")
       print("6 - Exportar para CSV")
       print("7 - Importar arquivo CSV")
       print("0 - Sair da agenda.")
       print("-------------------------------------------")

def importar_contatos(nome_arquivo):
     try:
          with open(nome_arquivo, "r") as arquivo:
               linhas = arquivo.readlines()
               for linha in linhas:
                    detalhes = linha.strip().split(',')
                    nome = detalhes[0]
                    Telefone = detalhes[1]
                    Email = detalhes[2]
                    Endereço = detalhes[3]
                    add_editar_contato(nome, Telefone, Email, Endereço)     
     except FileNotFoundError:
          print()
          print(">> Arquivo não encontrado. <<")
          print()
     except Exception as error:
          print()
          print("Algum erro inesperado aconteceu. Erro: ")
          print(error)
          print()



def exportar_contatos(nome_arquivo):
     try:
          with open(nome_arquivo, 'w') as arquivo:
               for contato in AGENDA:
                    Telefone = AGENDA[contato]['Telefone']
                    Email = AGENDA[contato]['Email']
                    Endereço = AGENDA[contato]["Endereço"]
                    arquivo.write("{},{},{},{}\n".format(contato, Telefone, Email, Endereço))
          print("> Agenda exportada com sucesso.")
     except:
          print("> Algum erro ocorreu ao exportar os contatos. Caso o erro persista, contate o desenvolvedor.")

# Run
load()
while True:
    imprimir_menu()

    opção = input('Escolha uma opção: ')

    if opção == "1":
        mostrar_contatos()

    elif opção == "2":
        contato = input("Digite o nome do contato: ")
        print()
        print("Buscando contato...")
        print()
        buscar_contatos(contato)
    elif opção == "3":
        contato = input("Digite o nome do contato que deseja adicionar: ")
        try:
             AGENDA[contato]
             print("Contato já existe. Verifique se digitou o nome correto e tente novamente.")
        except:
            Telefone, Email, Endereço = ler_detalhes_contato()
            print("> Adicionando contato <")
            add_editar_contato(contato, Telefone, Email, Endereço)
            print()
            print("Contato adicionado com sucesso!")
            print()
            print("Retornando ao menu...")
            print()
    elif opção == "4":
        contato = input("Digite o nome do contato que deseja editar: ")
        try:
             AGENDA[contato]
             print("> Editando contato <")
             contato, Telefone, Email, Endereço = ler_detalhes_contato()
             add_editar_contato(contato, Telefone, Email, Endereço)
             print()
             print("Contato editado com sucesso!")
             print()
             print("Retornando ao menu...")
             print()
        except:
            print("Contato inexistente. Verifique se digitou o nome correto e tente novamente.")
    elif opção == "5":
        contato = input("Digite o nome do contato que deseja excluir: ")
        excluir_contato(contato)
    elif opção == "6":
         nome_arquivo = input("Digite o nome do arquivo a ser exportado: ")
         exportar_contatos(nome_arquivo)

    elif opção == "7":
         nome_arquivo = input("Digite o nome do arquivo a ser importado: ")
         importar_contatos(nome_arquivo)
         print()
         print("Contatos importados com sucesso!")
         print()
         print("Retornando ao menu...")
    elif opção == "0":
        print("Saindo da agenda...")
        print()
        break


    else:
        print("OPÇÃO INVÁLIDA!")
