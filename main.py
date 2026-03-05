garagem = []
# [] é uma lista.
# Lista guarda dicionários de cada carro cadastrado.
# {} é um dicionário. 
# {} usa chave - valor. ex: "modelo": "intruder", "cor": "azul". É usado "" e :.



while True:
# WHILE TRUE cria um loop infinito para o menu sempre voltar.
# Para sair, escolha 5 que ativará o BREAK (no final do código).
    print("Bem-vindo ao sistema de gerenciamento de garagem!")
    print(" 1. Cadastrar veículo")
    print(" 2. Atualização de veículo")
    print(" 3. Remoção de veículo")
    print(" 4. Listar veículos")
    print(" 5. Sair")
    # Exibe todas as mensagens acima de uma vez.




    escolha = input("Digite a opção desejada: ")
    # O INPUT lê a opção digitada pelo usuário e a guarda na memória.
    # O INPUT também é como um PRINT, com o plus de capturar o que você digita.


    if int(escolha) == 1:
        print("Cadastro de veículo")
    # O IF SEMPRE EXIGE UMA LINHA INDENTADA DEPOIS, POIS O IF É UM BLOCO DE CÓDIGOS.
    # INT() transforma o INPUT ESCOLHA que o usuário digitou em um número inteiro e verifica se a opção foi a 1.
    # == significa igual a.
    # o PRINT está indentado pois é parte do IF. 
    # Ex: print("Bem-vindo ao sistema!") -> Apenas informa.
    # escolha = input("Opção: ") -> Informa e já guarda a resposta.
        modelo = input("Digite o modelo do veículo: ")
        cor = input("Digite a cor do veículo: ")
        km = input("Digite a quilometragem do veículo: ")
        ano = input("Digite o ano do veículo: ")
        marca = input("Digite a marca do veículo: ")
        placa = input("Digite a placa do veículo: ")  
    # INDENTAÇÃAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO!!!! TAB TAB TAB TAB.
    
        if float(km) < 0 or int(ano) < 0:
            print("A quilometragem e/ ou ano não pode ser negativa. Valor inválido")
    # Validação para o usuário burro não digitar um número negativo.
    # Coloque o PRINT para mostrar a cagada do usuário burro.
        if int(ano) < 2000:
            print("O ano do veículo não pode ser anterior a 2000. Valor inválido")
    # Validação para o usuário burro não digitar um ano anterior a 2000 pois só aceitamos veículos mais recentes.
    # Coloque o PRINT para mostrar a cagada do usuário burro.

        ano = input("Digite o ano do veículo: ")     
    # Solicita o ano do veículo repetidamente (sem necessidade)
        
        
        marca = input("Digite a marca/do veículo: ")
        placa = input("Digite a placa do veículo: ")
    # Solicita a marca e a placa do veículo repetidamente (sem necessidade)
    
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
        
    elif int(escolha) == 2:
        pass
    
    elif int(escolha) == 3:
        pass
    
    elif int(escolha) == 4:
        pass
    if int(escolha) == 5:
        print("Saindo do sistema. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")   
    
            
    # Abrimos o terminal para fazer o versionamento do código. 
    # GIT INIT - para iniciar o repositório local.
    # GIT ADD . - para adicionar os arquivos ao stage.
    # GIT STATUS - para verificar o status dos arquivos.
    # GIT COMMIT -M "Mensagem do commit" - para criar um commit com a mensagem especificada.
    # GIT LOG - para visualizar o histórico de commits e quem é o autor.

    # Para criar um repositório remoto no GitHub, siga os seguintes passos:
    # 1. Acesse o GitHub e faça login na sua conta.
    # 2. Clique no botão "New" para criar um novo repositório.
    # 3. Preencha o nome do repositório, adicione uma descrição (opcional) e escolha se deseja que o repositório seja público ou privado.
    # 4. Clique no botão "Create repository" para criar o repositório.
    # 5. Após criar o repositório, você verá uma página com instruções para conectar seu repositório local ao repositório remoto no GitHub. 
    # Siga as instruções fornecidas para adicionar o repositório remoto e fazer o push do seu código para o GitHub.
    # GIT REMOTE ADD ORIGIN <URL do repositório remoto> - para adicionar o repositório remoto.
    # GIT PUSH -U ORIGIN MAIN - para enviar o código para o repositório remoto no GitHub.
    # Agora, sempre que fizer alterações no código, basta seguir os passos de adicionar, commitar e fazer push para manter o repositório remoto atualizado com as últimas mudanças.



    