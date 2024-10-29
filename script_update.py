import sqlite3 as conector  
#Abrindo a conexão
conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

#Atribuindo comandos
comando1 = '''UPDATE Pessoa SET oculos = 1;'''
cursor.execute(comando1)

comando2 = '''UPDATE Pessoa SET oculos = ? WHERE cpf = 100000000;'''
cursor.execute(comando2,(False,))

comando3 = '''UPDATE Pessoa SET oculos = :usa_oculos WHERE "cpf" = :cpf;'''
cursor.execute(comando3, {"usa_oculos": False, "cpf":300000000})

conexao.commit()


cursor.close()

conexao.close()
