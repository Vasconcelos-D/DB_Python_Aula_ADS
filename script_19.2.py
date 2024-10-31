import sqlite3 as conector #Importando a biblioteca sqlite3 com o apelido conector
from modelo import Veiculo #Importando modelo da classe Veiculo

#Abrindo a conexão 
conexao = conector.connect("./meu_banco.db") #Conectando com Banco de Dados
cursor = conexao.cursor() #Criando o cursor

comando = '''SELECT
                Veiculo.placa, Veiculo.ano, Veiculo.cor, 
                Veiculo.motor, Veiculo.proprietario,
                Marca.nome FROM Veiculo JOIN Marca ON Marca.id = Veiculo.marca;''' #Comondo do Banco de Dados
cursor.execute(comando) #Execução do comando

reg_veiculos = cursor.fetchall()

for reg_veiculo in reg_veiculos:
    veiculo = Veiculo(*reg_veiculo)
    print("Placa: ", veiculo.placa, ", Marca: ", veiculo.marca)
    
cursor.close()
conexao.close()

