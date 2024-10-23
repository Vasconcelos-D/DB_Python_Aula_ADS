import sqlite3 as conector  # Importa a biblioteca sqlite3 e a renomeia como "conector"
from modelo import Pessoa  # Importa a classe Pessoa do módulo modelo

# Abrindo uma conexão com o banco de dados SQLite.
# Se o arquivo 'meu_banco.db' não existir, ele será criado.
conexao = conector.connect("./meu_banco.db")

# Cria um cursor para realizar operações no banco de dados.
cursor = conexao.cursor()

# Cria uma instância da classe Pessoa com os valores fornecidos:
# CPF: 200000000, Nome: 'José', Data de nascimento: '1993-01-21', Usa óculos: False
pessoa = Pessoa(200000000, 'José', '1993-01-21', False)

# O comando SQL que será executado. Esse comando insere valores na tabela 'Pessoa'.
# Os campos esperados são: cpf, nome, data de nascimento e se a pessoa usa óculos.
comando = '''
INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
VALUES (:cpf, :nome, :data_nascimento, :usa_oculos);'''
# Aqui os valores estão sendo passados como parâmetros nomeados (:cpf, :nome, etc.)
# Isso ajuda a evitar problemas de SQL injection e torna o código mais legível.

# Executa o comando SQL, substituindo os parâmetros nomeados pelos valores do objeto 'pessoa'.
cursor.execute(comando, {
    "cpf": pessoa.cpf,  # Substitui o parâmetro ':cpf' pelo valor de 'pessoa.cpf'
    "nome": pessoa.nome,  # Substitui ':nome' pelo valor de 'pessoa.nome'
    "data_nascimento": pessoa.data_nascimento,  # Substitui ':data_nascimento' pelo valor de 'pessoa.data_nascimento'
    "usa_oculos": pessoa.usa_oculos  # Substitui ':usa_oculos' pelo valor de 'pessoa.usa_oculos'
})

# Confirma (efetiva) as mudanças no banco de dados. Sem isso, os dados não serão salvos.
conexao.commit()

# Fecha o cursor após a execução dos comandos SQL, liberando recursos.
cursor.close()

# Fecha a conexão com o banco de dados.
conexao.close()
