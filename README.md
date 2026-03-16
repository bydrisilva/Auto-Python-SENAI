# AUTO PYTHON - Sistema de Gestão de Concessionária.
Este projeto foi desenvolvido durante o curso de Python no **SENAI Taguatinga**, com o objetivo de gerenciar o fluxo de entrada, saída e atualização de veículos em uma garagem de forma eficiente e segura.
##  Funcionalidades Técnicas
### 1. Cadastro com Validação Rigorosa:
O sistema não aceita qualquer dado. Ele garante a integridade da base de dados através de:
* **Limite de Ano:** Só são aceitos veículos fabricados a partir de 2016.
* **Validação Numérica:** Impede o cadastro de quilometragem ou anos negativos.
* **Campos Obrigatórios:** Utiliza o método `.strip()` para garantir que nenhum campo (Modelo, Cor, Marca, Placa) fique vazio ou contenha apenas espaços.
### 2. Atualização de Dados (Em desenvolvimento)
Permite a alteração de informações de veículos já cadastrados, mantendo as mesmas regras de validação do cadastro inicial.
### 3. Remoção Inteligente:
A exclusão é feita através da **Placa** do veículo (identificador único). O sistema percorre a lista, localiza o dicionário correspondente e utiliza o método `.remove()` para atualizar o estoque.
### 4. Listagem e Visualização:
Exibe todos os veículos presentes na garagem de forma formatada. Caso a garagem esteja vazia, o sistema informa o usuário através de uma verificação de lista (`if not garagem`).
## Tecnologias Utilizadas:
* **Python 3.x**
* **Dicionários e Listas:** Para estruturação complexa de dados.
* **Estruturas de Repetição:** `while True` para o menu e `for...in` para buscas.
* **Tratamento de Strings:** Métodos de limpeza e formatação de dados.
## Como Executar o Projeto:
1. Clone o repositório em sua máquina:
   ```bash
   git clone [https://github.com/bydrisilva/Auto-Python-SENAI.git](https://github.com/bydrisilva/Auto-Python-SENAI.git).