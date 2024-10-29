import sqlite3 as conector  
#Abrindo a conexão
conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

#Atribuindo comandos
comando = '''DELETE FROM Pessoa WHERE cpf = 300000000;'''
cursor.execute(comando)
#Validando comando
conexao.commit()
#Fechando as conexões
cursor.close()
conexao.close()
