# 1. CRIAR VARÍAVEL GARAGEM PARA GUARDAR OS VEÍCULOS CADASTRADOS.
garagem = []
# [] é uma lista. Guarda cada carro cadastrado.

#2. CRIAR O MENU DE OPÇÕES PARA O USUÁRIO INTERAGIR COM O SISTEMA.
while True:
    # WHILE TRUE cria um loop infinito para o menu sempre voltar.
    # Para sair, escolha 5 que ativará o BREAK (no final do código).
    print("Bem-vindo ao sistema de gerenciamento de garagem!\nVamos começar?")
    print(" 1. Cadastrar veículo")
    print(" 2. Atualização de veículo")
    print(" 3. Remoção de veículo")
    print(" 4. Listar veículos")
    print(" 5. Sair")
    # Exibe todas as mensagens acima de uma vez.
    # \n é uma quebra de linha para textos. 

    # 3. LER A OPÇÃO DIGITADA PELO USUÁRIO E GUARDAR NA MEMÓRIA PARA VER SE É VÁLIDA.
    escolha = input("Digite a opção desejada: ")
    # O INPUT lê a opção digitada pelo usuário e a guarda na memória.
    # O INPUT também é como um PRINT, com o plus de capturar o que você digita.

    # 4. VERIFICAR QUAL OPÇÃO FOI DIGITADA NO MENU E EXECUTAR A AÇÃO CORRESPONDENTE.
    # 4.1 COLETANDO OS DADOS:
    if int(escolha) == 1:
        print("\nCadastro de veículo")
        # O IF precisa de um bloco de código indentado.
        # INT() transforma a variável ESCOLHA que o usuário digitou em um número inteiro e verifica se a opção foi a 1.
        # O dado era STRING pois todo dado coletado do usuário pelo INPUT é STRING, mesmo que seja um número. 
        # == significa igual a.
        # o PRINT está indentado pois é parte do IF. 
        # Ex: print("Bem-vindo ao sistema!") -> Apenas informa, escolha = input("Opção: ") -> Informa e já guarda a resposta.
        modelo = input("Digite o modelo do veículo: ")
        cor = input("Digite a cor do veículo: ")
        km = input("Digite a quilometragem do veículo: ")
        ano = input("Digite o ano do veículo: ")
        marca = input("Digite a marca do veículo: ")
        placa = input("Digite a placa do veículo: ")  
        # INDENTAÇÃAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO!!!! TAB TAB TAB TAB.
        # Tudo aqui está dentro do IF lá de cima.

        # 4.2 VERIFICANDO SE OS DADOS SÃO VÁLIDOS ANTES DE SALVAR:
        if float(km) < 0 or int(ano) < 0:
        # Validação para o usuário burro não digitar um número negativo.
        # Declaramos o tipo da variável pois o INPUT sempre retorna uma string (não dá para comparar letras e números). 
            print("A quilometragem e/ ou ano não pode ser negativa. Valor inválido")
            # Coloque o PRINT para mostrar se o usuário digitou um valor inválido.
            continue 
            # Volta para o início do menu para não salvar dado errado.

        if int(ano) < 2000:
            print("O ano do veículo não pode ser anterior a 2000. Valor inválido")
            # Validação para o usuário burro não digitar um ano anterior a 2000 pois só aceitamos veículos mais recentes.
            # Coloque o PRINT para mostrar a cagada do usuário burro.
            continue # Interrompe o cadastro e volta ao menu.

        # Verificamos se há campos vazios usando .strip() (remove espaços).
        if modelo.strip() == "" or cor.strip() == "" or km.strip() == "" or ano.strip() == "" or marca.strip() == "" or placa.strip() == "":
            print("Todos os campos são obrigatórios. Por favor, preencha todos os dados.")
            continue # Em vez de exit(), usamos continue para o programa não fechar na cara do usuário.
            
        veiculo = {
            "modelo": modelo,   
            "cor": cor,
            "km": km,
            "ano": ano,
            "marca": marca,
            "placa": placa
        }
        # {} é um dicionário. 
        # {} usa chave - valor. ex: "modelo": "intruder", "cor": "azul". É usado "" e :.
        garagem.append(veiculo)
        
        print(f"Veículo {veiculo['modelo']} cadastrado com sucesso!")
        
    elif int(escolha) == 2:
        print("Opção de atualização em desenvolvimento...")
        pass
    
    elif int(escolha) == 3:
        print("Opção de remoção em desenvolvimento...")
        pass
    
    #ESCOLHA 4:   
    elif int(escolha) == 4:
        print("\nListando veículos cadastrados:")
        # O len(garagem) == 0 conta quantos itens tem na lista. Se for 0, está vazia.
        if len(garagem) == 0:
            # Se o TAMANHO da garagem for igual a 0 (vazia)...
            print("Nenhum veículo cadastrado.")
        # ELIF(senão se) = ELSE+IF   
        else: 
            # O 'for' percorre a lista 'garagem' e extrai cada 'veiculo' (dicionário) para mostrar na tela.
            for veiculo in garagem:
                print("-" * 20)
                print(f"Modelo: {veiculo['modelo']}")
                print(f"Cor: {veiculo['cor']}")           
                print(f"Marca: {veiculo['marca']}")
                print(f"Ano: {veiculo['ano']}")
                print("-" * 20)
            
    elif int(escolha) == 5: 
        print("Saindo do sistema. Até mais!")
        break # Quebra o loop While True e encerra o programa.
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")   
    
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