#Criando o script (PESSOA)
import sqlite3 as conector
#importando o connector

try:
#Abrindo o bloco Try, exececão
    #Abertuta da conexão e  aquisição de cursor
    conexao = conector.connect('./meu_banco.db')
    cursor = conexao.cursor()

    #Execução de um comando SELECT_CREATE
    comando = '''CREATE TABLE Pessoa (
                    cpf INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    oculos BOOLEAN NOT NULL,
                    PRIMARY KEY (cpf)
                    );'''
    cursor.execute(comando)

    #Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    #atribuindo a exceção
    print("Error de Banco de Dados", err)
finally:
    #fechando a conexão
    if conexao:
        cursor.close()
        conexao.close()
