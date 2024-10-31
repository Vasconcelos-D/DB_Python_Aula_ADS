#Criando Script (VEICULO)
import sqlite3 as conector
#importando conector

#Abertura de conexcão e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

#Executando Comando:
comando = '''CREATE TABLE Veiculo (
                placa CHARACTER(7) NOT NULL,
                ano INTEGER NOT NULL,
                cor TEXT NOT NULL,
                proprietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
                PRIMARY KEY (placa),
                FOREIGN KEY(marca) REFERENCES Marca(id)
                );'''
cursor.execute(comando)

#Efetivando o comando
conexao.commit()

#Fechando as conexões
cursor.close()
conexao.close()