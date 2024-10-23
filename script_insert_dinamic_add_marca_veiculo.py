import sqlite3 as conector  # Importa a biblioteca sqlite3 e a renomeia como "conector"
from modelo import Marca, Veiculo #Importando as Classes MARCA E VEICULO.

# Abrindo uma conexão com o banco de dados SQLite.
# Se o arquivo 'meu_banco.db' não existir, ele será criado.
conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys = on")

# Cria um cursor para realizar operações no banco de dados.
cursor = conexao.cursor()



comando1 = '''INSERT INTO Marca (nome, sigla) VALUES  (:nome, :sigla);'''

marca1 = Marca(1, "Marca A", "MA")
cursor.execute(comando1, vars(marca1))
marca1.id = cursor.lastrowid

marca2 = Marca(2, "Marca B", "MB")
cursor.execute(comando1, vars(marca2))
marca2.id = cursor.lastrowid

 # Inserção de dados na tabela Veiculo
comando2 = '''INSERT INTO Veiculo VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca);'''

veiculo1 = Veiculo("AAA0001", 2001, "Prata", 1.0, 10000000099, marca1.id)
veiculo2 = Veiculo("BAA0002", 2002, "Preto", 1.4, 10000000099, marca1.id)
veiculo3 = Veiculo("CAA0003", 2003, "Branco", 2.0, 20000000099, marca2.id)
veiculo4 = Veiculo("DAA0004", 2004, "Azul", 2.2, 30000000099, marca2.id)

cursor.execute(comando2, vars(veiculo1))
cursor.execute(comando2, vars(veiculo2))
cursor.execute(comando2, vars(veiculo3))
cursor.execute(comando2, vars(veiculo4))


# Confirma (efetiva) as mudanças no banco de dados. Sem isso, os dados não serão salvos.
conexao.commit()

# Fecha o cursor após a execução dos comandos SQL, liberando recursos.
cursor.close()

# Fecha a conexão com o banco de dados.
conexao.close()
