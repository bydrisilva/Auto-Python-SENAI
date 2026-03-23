# Se o sistema estiver em ambiente de produção mude para True.
# Deixando em False, ele já carrega o Uno, Opala e Fuscão do professor para facilitar seus testes!
prod = False 

if prod == False:
    garagem = [
        {"modelo": "Uno", "cor": "Branco", "km": "0", "ano": "2016", "marca": "Fiat", "placa": "ABC1234"},
        {"modelo": "Opala 74", "cor": "Cinza", "km": "200", "ano": "2018", "marca": "Chevrolet", "placa": "XYZ2026"},
        {"modelo": "Fuscão", "cor": "Preto", "km": "120000", "ano": "2020", "marca": "Volkswagen", "placa": "ABC1234"}
    ]
else:
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
        # --- CÓDIGO DO PROFESSOR ADICIONADO AQUI ---
        print("=" * 10)
        print("Alterando dados do veiculo..")
        placa = input("Digite a placa do veiculo: ")
        for veiculo in garagem:
            if veiculo["placa"] == placa:
                index = garagem.index(veiculo)
                for chave, valor in veiculo.items():
                    print("-" * 10)
                    novo_valor = input(f"Escolha um novo valor para {chave} (valor atual: {valor}): ")
                    if novo_valor.strip() != "":
                        garagem[index][chave] = novo_valor                
                break
        else:
            print("Veiculo não encontrado.")
    
    elif int(escolha) == 3:
        # --- CÓDIGO DO PROFESSOR ADICIONADO AQUI ---
        print("=" * 10)
        print("Removendo veiculo..")
        placa = input("Digite a placa do veiculo: ")
        for veiculo in garagem:
            if veiculo["placa"] == placa:
                garagem.remove(veiculo)
                print("Veiculo removido com sucesso!")
                break
        else:
            print("Veiculo não encontrado!")
        
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
                print(f"Placa: {veiculo['placa']}") # Adicionado placa para conferência
                print("-" * 20)
            
    elif int(escolha) == 5: 
        print("Saindo do sistema. Até mais!")
        break 
        # Quebra o loop While True e encerra o programa.
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")


# =======================================
# GUIA DEFINITIVO: CICLO DE VIDA DA AULA 
# =======================================

# --- PASSO 1: CHEGUEI NA MÁQUINA ---
# CD DOCUMENTS             - Entra na pasta Documentos.
# MKDIR NOME_DA_PASTA      - Cria sua pasta do dia (ex: adrielle-projetos).
# CD NOME_DA_PASTA         - Entra na pasta criada.
# GIT CLONE <URL>          - Baixa seu repositório que já existe no GitHub.
# LS                       - Lista as pastas para ver o nome do projeto baixado.
# CD NOME_DO_PROJETO       - ENTRA na pasta do projeto (Obrigatório para o Git funcionar).
# CODE . -R                - Abre o projeto no VS Code.

# --- PASSO 2: SINCRONIZAÇÃO (ANTES DE COMEÇAR) ---
# GIT PULL ORIGIN MAIN     - Traz atualizações feitas em casa ou em outra máquina.

# --- PASSO 3: DESENVOLVIMENTO ---
# Digite seu código, crie seus arquivos e realize as atividades.
# CLS                      - Limpa o terminal para tirar a poluição visual.

# --- PASSO 4: REVISÃO E STATUS ---
# GIT STATUS               - Verifica o que você alterou ou criou.
# GIT LOG                  - Vê o histórico de commits e quem mexeu por último.

# --- PASSO 5: FINALIZAÇÃO (ENVIAR PARA O GITHUB) ---
# GIT ADD .                - Adiciona as mudanças ao "palco" (stage).
# GIT COMMIT -M "Mensagem" - Carimba a versão com uma descrição do que foi feito.
# GIT PUSH ORIGIN MAIN     - Sobe tudo para o seu GitHub.

# --- PASSO 6: SAÍDA SEGURA ---
# CD ..                    - Sai da pasta do projeto.
# RM -RF NOME_DA_PASTA     - Apaga sua pasta da máquina pública (Cuidado!).


# ==============================================
# CRIANDO UM REPOSITÓRIO DO ZERO (PROJETO NOVO)
# ==============================================

# 1. NO GITHUB: Clique em "New", dê um nome e clique em "Create repository".
# 2. NO TERMINAL (Dentro da pasta do seu novo projeto):

# GIT INIT                 - Inicia o Git nesta pasta nova.
# GIT ADD .                - Adiciona os primeiros arquivos.
# GIT COMMIT -M "Initial"  - Cria o primeiro commit da história.
# GIT BRANCH -M MAIN       - Renomeia a ramificação para o padrão 'main'.
# GIT REMOTE ADD ORIGIN <URL> - Conecta a pasta local ao link do GitHub.
# GIT REMOTE -V            - Confirma se o link foi colado corretamente.
# GIT PUSH -U ORIGIN MAIN  - Envia pela primeira vez e conecta as pontas.





