# 📱 Lista de Contatos em Python

Projeto desenvolvido em Python com o objetivo de praticar os principais conceitos de programação através da criação de uma **agenda de contatos pelo terminal**.

O sistema permite cadastrar, visualizar, pesquisar, editar e excluir contatos.

## 🚀 Funcionalidades

* ➕ Adicionar contatos
* 📋 Listar todos os contatos cadastrados
* 🔎 Pesquisar contatos pelo nome
* ✏️ Editar nome, telefone ou email
* 🗑️ Excluir contatos
* ⚠️ Informar quando um contato não foi encontrado
* 🚪 Encerrar o programa pelo menu

## 🛠️ Tecnologias utilizadas

* Python 3

## 📚 Conceitos praticados

Durante o desenvolvimento deste projeto foram utilizados:

* Variáveis
* `input()` e `print()`
* Estruturas condicionais `if`, `elif` e `else`
* Laço de repetição `while`
* Laço de repetição `for`
* Listas
* Dicionários
* Função `len()`
* Método `.lower()`
* Manipulação de dados
* Busca de informações
* Remoção de elementos de uma lista
* Variáveis de controle (`encontrado`)

## 💻 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/joseedmorais/Projetos-pyton.git
```

### 2. Entre na pasta do projeto

```bash
cd lista de contatos
```

### 3. Execute o programa

```bash
python main.py
```

## 🖥️ Menu do sistema

```text
-------- MENU PRINCIPAL --------
1 - Adicionar contato
2 - Listar contatos
3 - Pesquisar contato
4 - Editar contato
5 - Excluir contato
0 - Sair
```

## 📌 Exemplo de contato

Cada contato é armazenado utilizando um dicionário:

```python
contato = {
    "nome": "João",
    "telefone": "83999999999",
    "email": "joao@email.com"
}
```

Os contatos são armazenados dentro de uma lista:

```python
contatos = []
```

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido como parte dos meus estudos em **Ciência da Computação**, com o objetivo de melhorar minha lógica de programação e praticar a manipulação de listas e dicionários em Python.

## 🔮 Melhorias futuras

Algumas funcionalidades que podem ser adicionadas futuramente:

* [ ] Salvar os contatos em um arquivo `.json`
* [ ] Carregar os contatos automaticamente ao iniciar o programa
* [ ] Pesquisar por nome parcial
* [ ] Impedir contatos duplicados
* [ ] Adicionar endereço
* [ ] Adicionar data de nascimento
* [ ] Criar uma interface gráfica
* [ ] Utilizar funções para organizar melhor o código
* [ ] Criar um banco de dados para armazenar os contatos

## 👨‍💻 Autor

**José Eduardo**

Estudante de Ciência da Computação e desenvolvedor em formação, atualmente estudando Python e desenvolvendo projetos para aprimorar minhas habilidades de programação.
