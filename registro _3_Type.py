# Importando a biblioteca sqlite3 com um apelido 'conector' e importando a classe 'Pessoa' do módulo 'modelo'
import sqlite3 as conector
from modelo import Pessoa

# Estabelecendo conexão com um banco de dados SQLite. Se o arquivo 'meu_banco.db' não existir, ele será criado.
# O parâmetro 'detect_types' com 'conector.PARSE_DECLTYPES' permite o uso de tipos personalizados.
conexao = conector.connect("./meu_banco.db", detect_types=conector.PARSE_DECLTYPES)
cursor = conexao.cursor()  # Criação de um cursor para execução de comandos SQL

# Definindo uma função que converte um valor numérico (0 ou 1) para um valor booleano (False ou True).
def conv_boll(dado):
    return True if dado == 1 else False

# Registrando a função de conversão para interpretar valores da coluna BOOLEAN no banco de dados como booleanos.
conector.register_converter("BOOLEAN", conv_boll)

# Definindo o comando SQL para selecionar todos os registros da tabela 'Pessoa' onde a coluna 'oculos' é igual ao valor passado por parâmetro.
comando = '''SELECT * FROM Pessoa WHERE oculos = :usa_oculos;'''
# Executando o comando SQL, substituindo ':usa_oculos' pelo valor True (ou seja, onde o campo 'oculos' é verdadeiro).
cursor.execute(comando, {"usa_oculos": True})

# Recuperando todos os registros retornados pela consulta SQL.
registros = cursor.fetchall()

# Iterando sobre cada registro retornado.
for registro in registros:
    # Criando uma instância de 'Pessoa' com os valores do registro retornado do banco.
    pessoa = Pessoa(*registro)
    # Exibindo os valores de cada atributo de 'Pessoa' e seus respectivos tipos.
    print("cpf: ", type(pessoa.cpf), pessoa.cpf)
    print("nome: ", type(pessoa.nome), pessoa.nome)
    print("nascimento: ", type(pessoa.data_nascimento), pessoa.data_nascimento)
    print("oculos: ", type(pessoa.usa_oculos), pessoa.usa_oculos)

# Fechando o cursor e a conexão com o banco de dados, liberando os recursos.
cursor.close()
conexao.close()
