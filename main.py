array_opcao={}
array_txt={}
arquivo_txt = "lista.txt"
arquivo_opcoes = "opcoes.txt"

def menu():
  print("--- MENU --- ")
  with open(arquivo_opcoes,'r') as op:
    opcao=1
    conteudo=op.readlines()
    for contem in conteudo:
      print(f"opcao {opcao}: {contem}",end='')
      # array_opcao[opcao]={contem}
      array_opcao[opcao]=contem
      opcao+=1
  selecionar_opcao()
  
#for i in rang(len(rr)):

def selecionar_opcao():
  print("\n\nSelecione uma opcao ",end='')
  opcao=input(": ")
  if int(opcao) in array_opcao:
    if opcao == '1':
      ler_txt()
    elif opcao == '2':
      editar_txt()
    elif opcao == '3':
      apagar_txt()
    elif opcao == '4':
      copiar_txt()
    else:
      print("Ainda nao foi implementado")
  else:
    print(f"{opcao} inválida")
    
def editar_txt():
  if len(array_txt) == 0:
    with open(arquivo_txt,'r') as rf:
      conteudo=rf.readlines()
      for index,contem in enumerate(conteudo):
        array_txt[index]=contem
  opcao = input("Qual item a editar: ")
  print(f"\nEditando a opcao {array_opcao[int(opcao)]}")
  novo_txt = input("Texto para substituir: ")
  novo_txt=novo_txt + "\n"
  array_txt[int(opcao)] = novo_txt 
  with open(arquivo_txt,'w') as wf:
    for line_array in array_txt.values():
      wf.write(line_array)
  Sair_ou_menu()
  
def Sair_ou_menu():
  opcao = input("Deseja sair [S | N]: ")
  if str(opcao) == 'S':
    # break()
    exit
  elif str(opcao) == 'N':
    menu()
  else:
    print("opcao errada")
    Sair_ou_menu()


def ler_txt():
  with open(arquivo_txt,'r') as rf:
    conteudo=rf.readlines()
    for index,contem in enumerate(conteudo):
      print(f"opcao {index}: {contem}",end='')
      array_txt[index]=contem
    print("")
    Sair_ou_menu()
    
def copiar_txt():
  print("funcao copiar ...")

def apagar_txt():
  apagar = input("qual item deseja apagar: ")
  print(array_txt[int(apagar)])
  del array_txt[int(apagar)]
  print("apagado...")
  Sair_ou_menu()

menu()
