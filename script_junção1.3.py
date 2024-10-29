from modelo import Veiculo, Marca #Importando modelo da classe Veiculo

#Abrindo a conexão 
def recuperar_veiculos(conexao, cpf):
    cursor = conexao.cursor() #Criando o cursor

    comando = '''SELECT * FROM Veiculo 
             JOIN Marca ON Marca.id = Veiculo.marca
             WHERE Veiculo.proprietario = ?;''' #Comondo do Banco de Dados
    cursor.execute(comando, (cpf,)) #Execução do comando

    veiculos = []
    registros = cursor.fetchall()

    for registro in registros:  
        marca = Marca(*registro[6:])
        veiculo = Veiculo(*registro[:5], marca)
        veiculo.append(veiculo)
    
    cursor.close()
    return veiculos

