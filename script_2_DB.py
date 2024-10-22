#Criadno o script(MARCA)
import sqlite3 as conector

#Abrindo conexão
conexao = conector.connect('./meu_banco.db')
cursor = conexao.cursor()

#Execução de um comando 
comando = '''CREATE TABLE Marca (
                id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                sigla CHARACTER(2) NOT NULL,
                PRIMARY KEY(id)
                );'''
cursor.execute(comando)

#Efetivação do comando
conexao.commit()
#Fechando as conexões
cursor.close()
conexao.close()

