import sqlite3 as conector #Importando a biblioteca sqlite3 com o apelido conector
from modelo import Veiculo, Marca #Importando modelo da classe Veiculo

#Abrindo a conexão 
conexao = conector.connect("./meu_banco.db") #Conectando com Banco de Dados
cursor = conexao.cursor() #Criando o cursor

comando = '''SELECT * FROM 
                Veiculo JOIN Marca ON Marca.id = Veiculo.marca;''' #Comondo do Banco de Dados
cursor.execute(comando) #Execução do comando

registros = cursor.fetchall()

for registro in registros:
    print(registro)
    marca = Marca(*registro[6:])
    veiculo = Veiculo(*registro[:5], marca)
    print("Placa:", veiculo.placa, ", Marca:", veiculo.marca.nome)
    
cursor.close()
conexao.close()

