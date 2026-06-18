# FinTrack — Gerenciador de Transações Financeiras

O **FinTrack** é uma aplicação em Python integrada a um banco de dados **PostgreSQL** desenvolvida para gerenciar transações financeiras (receitas e despesas). O projeto implementa um ciclo completo de **CRUD** (Create, Read, Update, Delete) com foco em boas práticas de desenvolvimento, segurança contra SQL Injection e estruturação profissional de histórico no Git.

Este projeto serve como um excelente portfólio para demonstrar habilidades em desenvolvimento backend, manipulação de bancos de dados relacionais e controle de versão.

---

## 🛠️ Tecnologias e Ferramentas

- **Linguagem:** Python 3.x
- **Banco de Dados:** PostgreSQL
- **Driver de Conexão:** `psycopg2-binary`
- **Controle de Versão:** Git & GitHub

---

## 🏗️ Arquitetura do Projeto

A estrutura do código foi projetada separando as responsabilidades de conexão com o banco de dados da lógica de execução das operações:

```text
fintrack/
│
├── database.py          # Gerenciamento da conexão com o Postgres e DDL (criação da tabela)
├── main.py              # Lógica do CRUD, funções de agregação e interface/fluxo do usuário
├── .gitignore           # Arquivos e pastas ignorados pelo Git (ex: venv, __pycache__)
└── README.md            # Documentação completa do projeto