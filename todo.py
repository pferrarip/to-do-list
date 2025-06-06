import os
tarefas = []
def adicionar_tarefa():
   os.system("cls")
   print('\n ---------Adição de Tarefas-------')
   new_tarefa = input("qual tarefa você tem que realizar? ") 
   tarefas.append(new_tarefa)
   os.system("cls")

def consulta_tarefa():
   os.system("cls")
   print('\n ---------Consulta de Tarefas-------')
   if not tarefas:
      print("Você não tem tarefas, adicione alguma para ser exibida")
   else:
      for consulta in enumerate(tarefas, start=1):
         print("{0}".format(consulta))

def excluir_tarefa():
   os.system("cls")
   print('\n ---------Exclusão de Tarefas-------')
   consulta_tarefa()
   excluir = int(input("digite o numero da tarefa que você deseja excluir "))
   if not tarefas: 
      print('Você não tem tarefas, adicione alguma para ser exibida')
   elif excluir < 1 or excluir > len(tarefas):
      print('numero de tarefa inválida')
   else:
      especifica = tarefas.pop(excluir - 1)
      print('A tarefa {} foi removida com sucesso'.format(especifica))

def atualizar_tarefa():
   os.system("cls")
   print('\n ---------Atualização de Tarefas-------')
   consulta_tarefa()
   indice = int(input('Qual o NÚMERO da tarefa que voce deseja atualizar '))
   if not tarefas:
      print("Não há tarefas para serem atualizadas")
   elif indice < 1 or indice > len(tarefas):
      print("Indice inválido de tarefas")
   else:
      atualizar = str(input('Digite a nova descrição para a tarefa '))
      antiga = tarefas[indice - 1]
      tarefas[indice - 1] = atualizar
      
      print('a tarefa {0} foi atualizada para {1}' .format(antiga,atualizar))
      os.system("cls")


while True:
   print("\n --------- To-Do List-------")
   print("1- Adcionar tarefa")
   print("2- Consultar tarefa")
   print("3- Atualizar tarefa ")
   print("4- Excluir tarefa")
   print("5- Sair do Programa")

   escolha = input('Escolha uma das opcões ')

   match escolha:
      case '1':
         adicionar_tarefa()
      case '2': 
         consulta_tarefa()
      case '3':
         atualizar_tarefa()
      case '4':
         excluir_tarefa()
      case '5': 
          print ("saindo do progama")
          break
         