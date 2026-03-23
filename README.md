# AUTO PYTHON - Sistema de Gestão de Concessionária

Este projeto consiste em um sistema de gerenciamento de inventário para concessionárias, desenvolvido em Python. O software permite o controle de entrada, saída e manutenção de dados de veículos, garantindo a organização e a integridade das informações através de uma interface de terminal.

O projeto foi desenvolvido como parte das atividades práticas no SENAI Taguatinga, integrando conceitos de Engenharia de Software aplicados na UCB (Universidade Católica de Brasília).

## Funcionalidades Técnicas

### 1. Cadastro com Validação de Dados
O sistema implementa regras de negócio para assegurar a qualidade dos dados inseridos:
* **Validação de Ano:** Restrição de cadastro para veículos fabricados a partir de 2016 (ou 2000, conforme configuração local).
* **Integridade Numérica:** Verificação de valores negativos para quilometragem e ano, interrompendo o registro em caso de inconsistência.
* **Tratamento de Strings:** Utilização do método `.strip()` para evitar campos vazios ou preenchidos apenas com espaços.

### 2. Atualização Dinâmica de Registros
Permite a modificação individual de cada atributo do veículo (modelo, cor, km, ano, marca e placa). 
* **Lógica de Preservação:** Caso o usuário não deseje alterar um campo específico, o sistema permite manter o valor original ao pressionar "Enter".
* **Mapeamento por Índice:** Utiliza o método `.index()` para localizar a posição exata do objeto na memória antes da alteração.

### 3. Remoção por Identificador Único
A exclusão de veículos é realizada através da placa. O sistema executa uma busca linear na lista de dicionários e utiliza o método `.remove()` ao localizar a correspondência exata.

### 4. Listagem e Monitoramento de Pátio
Exibição formatada de todos os veículos disponíveis. O sistema inclui uma verificação de estado (`if not garagem`) para informar o usuário caso o inventário esteja vazio.

## Destaques de Implementação
* **Variável de Ambiente (Ambiente de Teste):** O código possui uma variável de controle (`prod`) que, quando configurada como `False`, carrega automaticamente uma base de dados fictícia (Uno, Opala, Fuscão) para agilizar os testes de desenvolvimento.
* **Estrutura de Dados Complexa:** Utilização de uma lista global contendo múltiplos dicionários, simulando o comportamento de uma tabela de banco de dados (CRUD).



## Tecnologias Utilizadas
* Linguagem: Python 3.x.
* Estruturas de Dados: Listas e Dicionários.
* Lógica de Programação: Estruturas de repetição (`while`, `for`) e condicionais compostas.

## Instruções para Execução

1. Clone o repositório para o seu diretório local:
   ```bash
   git clone [https://github.com/bydrisilva/Auto-Python-SENAI.git](https://github.com/bydrisilva/Auto-Python-SENAI.git)