import sqlite3 as conector 
from modelo import Pessoa
from script_4 import recuperar_veiculos

conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

comando = '''SELECT * FROM Pessoa;'''
cursor.execute(comando)

pessoas = []

reg_pessoas = cursor.fetchall()

for reg_pessoa in reg_pessoas:
    pessoa = Pessoa(*reg_pessoa)
    pessoa.veiculos = recuperar_veiculos(conexao, pessoa.cpf)
    pessoas.append(pessoa)
    
for pessoa in pessoas:
    print(pessoa.nome)
    for veiculo in pessoa.veiculo:
        print('\t', veiculo.placa, veiculo.marca.nome)

cursor.close()
conexao.close()
