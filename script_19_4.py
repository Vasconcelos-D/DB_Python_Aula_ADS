from modelo import Veiculo, Marca  # Importando modelo da classe Veiculo

# Abrindo a conexão 
def recuperar_veiculos(conexao, cpf):

    cursor = conexao.cursor()  # Criando o cursor

    comando = '''SELECT * FROM Veiculo v
                 JOIN Marca m ON m.id = v.marca 
                 WHERE v.proprietario = ?;'''  # Comando do Banco de Dados
    cursor.execute(comando, (cpf,))  # Execução do comando
   

    veiculos = []
    registros = cursor.fetchall()
   
    
    for registro in registros:  
        marca = Marca(*registro[6:])  # Cria uma instância de Marca com os dados apropriados
        veiculo = Veiculo(*registro[:5], marca)  # Cria uma instância de Veiculo, associando a Marca
        veiculos.append(veiculo)  # Adiciona o Veiculo à lista

    cursor.close()
    return veiculos
