import sqlite3 as conector
from modelo import Pessoa

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

comando = '''SELECT nome, oculos FROM Pessoa;'''
cursor.execute(comando)

registros = cursor.fetchall()
print("Tipo retornado pelo fetchall():", type(registros))

for registro in registros:
    print("Tipo: ", type(registro), " - Conteúdo:", registro)

cursor.close()
conexao.close()