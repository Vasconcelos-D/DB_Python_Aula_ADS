#Criando Script (VEICULO)
import sqlite3 as conector
#importando conector

#Abertura de conexcão e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

#Executando Comando:
comando = '''DROP TABLE Veiculo;'''
cursor.execute(comando)

#Efetivando o comando
conexao.commit()

#Fechando as conexões
cursor.close()
conexao.close()