from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
db = client['sistema']

clientes = db['clientes']
produtos = db['produtos']
pedidos = db['pedidos']
funcionarios = db['funcionarios']

def inserir_cliente(cliente):
    clientes.insert_one(cliente)
    print("Cliente inserido com sucesso!")

def alterar_cliente(id_cliente, novo_cliente):
    clientes.update_one({'_id': ObjectId(id_cliente)}, {'$set': novo_cliente})
    print("Cliente atualizado com sucesso!")

def excluir_cliente(id_cliente):
    clientes.delete_one({'_id': ObjectId(id_cliente)})
    print("Cliente excluído com sucesso!")

def consultar_todos_clientes():
    return list(clientes.find())

def consultar_cliente_por_id(id_cliente):
    return clientes.find_one({'_id': ObjectId(id_cliente)})

# Produtos
def inserir_produto(produto):
    produtos.insert_one(produto)
    print("Produto inserido com sucesso!")

def alterar_produto(id_produto, novo_produto):
    produtos.update_one({'_id': ObjectId(id_produto)}, {'$set': novo_produto})
    print("Produto atualizado com sucesso!")

def excluir_produto(id_produto):
    produtos.delete_one({'_id': ObjectId(id_produto)})
    print("Produto excluído com sucesso!")

def consultar_todos_produtos():
    return list(produtos.find())

def consultar_produto_por_id(id_produto):
    return produtos.find_one({'_id': ObjectId(id_produto)})

def inserir_pedido(pedido):
    pedidos.insert_one(pedido)
    print("Pedido inserido com sucesso!")

def alterar_pedido(id_pedido, novo_pedido):
    pedidos.update_one({'_id': ObjectId(id_pedido)}, {'$set': novo_pedido})
    print("Pedido atualizado com sucesso!")

def excluir_pedido(id_pedido):
    pedidos.delete_one({'_id': ObjectId(id_pedido)})
    print("Pedido excluído com sucesso!")

def consultar_todos_pedidos():
    return list(pedidos.find())

def consultar_pedidos_por_cliente(id_cliente):
    return list(pedidos.find({'cliente_id': ObjectId(id_cliente)}))

# Funcionários
def inserir_funcionario(funcionario):
    funcionarios.insert_one(funcionario)
    print("Funcionário inserido com sucesso!")

def alterar_funcionario(id_funcionario, novo_funcionario):
    funcionarios.update_one({'_id': ObjectId(id_funcionario)}, {'$set': novo_funcionario})
    print("Funcionário atualizado com sucesso!")

def excluir_funcionario(id_funcionario):
    funcionarios.delete_one({'_id': ObjectId(id_funcionario)})
    print("Funcionário excluído com sucesso!")

def consultar_todos_funcionarios():
    return list(funcionarios.find())

def consultar_funcionario_por_id(id_funcionario):
    return funcionarios.find_one({'_id': ObjectId(id_funcionario)})

def consultar_funcionario_por_cargo(cargo):
    return list(funcionarios.find({'cargo': cargo}))

# Menu do sistema
def menu():
    while True:
        print("\nSistema de Gerenciamento")
        print("1. Clientes")
        print("2. Produtos")
        print("3. Pedidos")
        print("4. Funcionários")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_clientes()
        elif opcao == '2':
            menu_produtos()
        elif opcao == '3':
            menu_pedidos()
        elif opcao == '4':
            menu_funcionarios()
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_clientes():
    while True:
        print("\nClientes")
        print("1. Inserir")
        print("2. Alterar")
        print("3. Excluir")
        print("4. Consultar todos")
        print("5. Consultar por ID")
        print("6. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            email = input("Email: ")
            telefone = input("Telefone: ")
            inserir_cliente({"nome": nome, "idade": idade, "email": email, "telefone": telefone})
        elif opcao == '2':
            id_cliente = input("ID do cliente: ")
            nome = input("Novo nome: ")
            idade = int(input("Nova idade: "))
            email = input("Novo email: ")
            telefone = input("Novo telefone: ")
            alterar_cliente(id_cliente, {"nome": nome, "idade": idade, "email": email, "telefone": telefone})
        elif opcao == '3':
            id_cliente = input("ID do cliente: ")
            excluir_cliente(id_cliente)
        elif opcao == '4':
            for cliente in consultar_todos_clientes():
                print(cliente)
        elif opcao == '5':
            id_cliente = input("ID do cliente: ")
            cliente = consultar_cliente_por_id(id_cliente)
            if cliente:
                print(cliente)
            else:
                print("Cliente não encontrado.")
        elif opcao == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_produtos():
    while True:
        print("\nProdutos")
        print("1. Inserir")
        print("2. Alterar")
        print("3. Excluir")
        print("4. Consultar todos")
        print("5. Consultar por ID")
        print("6. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))
            inserir_produto({"nome": nome, "preco": preco, "estoque": estoque})
        elif opcao == '2':
            id_produto = input("ID do produto: ")
            nome = input("Novo nome: ")
            preco = float(input("Novo preço: "))
            estoque = int(input("Novo estoque: "))
            alterar_produto(id_produto, {"nome": nome, "preco": preco, "estoque": estoque})
        elif opcao == '3':
            id_produto = input("ID do produto: ")
            excluir_produto(id_produto)
        elif opcao == '4':
            for produto in consultar_todos_produtos():
                print(produto)
        elif opcao == '5':
            id_produto = input("ID do produto: ")
            produto = consultar_produto_por_id(id_produto)
            if produto:
                print(produto)
            else:
                print("Produto não encontrado.")
        elif opcao == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_pedidos():
    while True:
        print("\nPedidos")
        print("1. Inserir")
        print("2. Alterar")
        print("3. Excluir")
        print("4. Consultar todos")
        print("5. Consultar por Cliente")
        print("6. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cliente_id = input("ID do cliente: ")
            itens = []
            while True:
                produto_id = input("ID do produto (ou 'fim' para terminar): ")
                if produto_id.lower() == 'fim':
                    break
                quantidade = int(input("Quantidade: "))
                itens.append({"produto_id": ObjectId(produto_id), "quantidade": quantidade})
            total = float(input("Total: "))
            data = input("Data (YYYY-MM-DD): ")
            inserir_pedido({"cliente_id": ObjectId(cliente_id), "itens": itens, "total": total, "data": data})
        elif opcao == '2':
            id_pedido = input("ID do pedido: ")
            cliente_id = input("Novo ID do cliente: ")
            itens = []
            while True:
                produto_id = input("Novo ID do produto (ou 'fim' para terminar): ")
                if produto_id.lower() == 'fim':
                    break
                quantidade = int(input("Nova quantidade: "))
                itens.append({"produto_id": ObjectId(produto_id), "quantidade": quantidade})
            total = float(input("Novo total: "))
            data = input("Nova data (YYYY-MM-DD): ")
            alterar_pedido(id_pedido, {"cliente_id": ObjectId(cliente_id), "itens": itens, "total": total, "data": data})
        elif opcao == '3':
            id_pedido = input("ID do pedido: ")
            excluir_pedido(id_pedido)
        elif opcao == '4':
            for pedido in consultar_todos_pedidos():
                print(pedido)
        elif opcao == '5':
            id_cliente = input("ID do cliente: ")
            for pedido in consultar_pedidos_por_cliente(id_cliente):
                print(pedido)
        elif opcao == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_funcionarios():
    while True:
        print("\nFuncionários")
        print("1. Inserir")
        print("2. Alterar")
        print("3. Excluir")
        print("4. Consultar todos")
        print("5. Consultar por ID")
        print("6. Consultar por Cargo")
        print("7. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))
            inserir_funcionario({"nome": nome, "cargo": cargo, "salario": salario})
        elif opcao == '2':
            id_funcionario = input("ID do funcionário: ")
            nome = input("Novo nome: ")
            cargo = input("Novo cargo: ")
            salario = float(input("Novo salário: "))
            alterar_funcionario(id_funcionario, {"nome": nome, "cargo": cargo, "salario": salario})
        elif opcao == '3':
            id_funcionario = input("ID do funcionário: ")
            excluir_funcionario(id_funcionario)
        elif opcao == '4':
            for funcionario in consultar_todos_funcionarios():
                print(funcionario)
        elif opcao == '5':
            id_funcionario = input("ID do funcionário: ")
            funcionario = consultar_funcionario_por_id(id_funcionario)
            if funcionario:
                print(funcionario)
            else:
                print("Funcionário não encontrado.")
        elif opcao == '6':
            cargo = input("Cargo: ")
            for funcionario in consultar_funcionario_por_cargo(cargo):
                print(funcionario)
        elif opcao == '7':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o sistema
if __name__ == "__main__":
    menu()
