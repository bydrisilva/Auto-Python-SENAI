garagem = []
# Lista para guardar os dicionários de cada carro cadastrado.


# Exibe boas-vindas e o menu principal na tela.
print("Bem-vindo ao sistema de gerenciamento de garagem!")
print(" 1. Cadastrar veículo")
print(" 2. Atualização de veículo")
print(" 3. Remoção de veículo")
print(" 4. Listar veículos")

# Lê a opção digitada pelo usuário e a guarda na memória.
escolha = input("Digite a opção desejada: ")

# Converte a escolha para número inteiro e verifica se a opção foi a 1
if int(escolha) == 1:
    print("Cadastro de veículo")
    
    # Solicita a primeira rodada de dados do veículo ao usuário
    modelo = input("Digite o modelo do veículo: ")
    cor = input("Digite a cor do veículo: ")
    km = input("Digite a quilometragem do veículo: ")
    ano = input("Digite o ano do veículo: ")
    marca = input("Digite a marca/fabricante do veículo: ")
    placa = input("Digite a placa do veículo: ")  
    
    # Tenta verificar se a quilometragem ou o ano são negativos
    if int(km) < 0 or int(ano) < 0:
        print("A quilometragem e/ ou ano não pode ser negativa. Valor inválido")
    if int(ano) < 2000:
        print("O ano do veículo não pode ser anterior a 2000. Valor inválido")
        
    # Solicita o ano do veículo repetidamente (sem necessidade)
    ano = input("Digite o ano do veículo: ")
    
    # Solicita a marca e a placa do veículo repetidamente (sem necessidade)
    marca = input("Digite a marca/fabricante do veículo: ")
    placa = input("Digite a placa do veículo: ")
    
    if modelo.strip() == "" or cor.strip() == "" or km.strip() == "" or ano.strip() == "" or marca.strip() == "" or placa.strip() == "":
        print("Todos os campos são obrigatórios. Por favor, preencha todos os dados.")
        exit()
        
    veiculo = {
        "modelo": modelo,   
        "cor": cor,
        "km": km,
        "ano": ano,
        "marca": marca,
        "placa": placa
    }
    garagem.append(veiculo)
    
    print(f"Veículo {veiculo['modelo']} cadastrado com sucesso!")
    
    print(garagem)
        
# Abrimos o terminal para fazer o versionamento do código. 
# GIT INIT - para iniciar o repositório local.
# GIT ADD . - para adicionar os arquivos ao stage.