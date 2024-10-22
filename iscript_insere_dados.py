import sqlite3 as conector

#Abrindo a conexão e aquisição do cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

#Execução do comando (INSERT)
comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
      VALUES (123456789, 'João', '2000-01-31', 1);'''
cursor.execute(comando)

#Efetivação do comando
conexao.commit()

#Fechando a conexão
cursor.close()
conexao.close()