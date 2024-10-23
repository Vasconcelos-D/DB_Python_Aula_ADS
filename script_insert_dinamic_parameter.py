import sqlite3 as conector  # Importa a biblioteca sqlite3 e a renomeia como "conector"
from modelo import Pessoa  # Importa a classe Pessoa do módulo modelo

# Abrindo uma conexão com o banco de dados SQLite.
# Se o arquivo 'meu_banco.db' não existir, ele será criado.
conexao = conector.connect("./meu_banco.db")

# Cria um cursor para realizar operações no banco de dados.
cursor = conexao.cursor()

# Cria uma instância da classe Pessoa com os valores fornecidos:
# CPF: 200000000, Nome: 'José', Data de nascimento: '1993-01-21', Usa óculos: False
pessoa = Pessoa(300000000, 'Silva', '1997-08-22', True)

# O comando SQL que será executado. Esse comando insere valores na tabela 'Pessoa'.
# Os campos esperados são: cpf, nome, data de nascimento e se a pessoa usa óculos.

comando = '''INSERT INTO Pessoa VALUES (:cpf, :nome, :data_nascimento, :usa_oculos);'''

# Aqui os valores estão sendo passados como parâmetros nomeados (:cpf, :nome, etc.)
# Isso ajuda a evitar problemas de SQL injection e torna o código mais legível.

cursor.execute(comando, vars(pessoa))
print(pessoa)

# Confirma (efetiva) as mudanças no banco de dados. Sem isso, os dados não serão salvos.
conexao.commit()

# Fecha o cursor após a execução dos comandos SQL, liberando recursos.
cursor.close()

# Fecha a conexão com o banco de dados.
conexao.close()
