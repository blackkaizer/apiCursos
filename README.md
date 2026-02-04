
# API Cursos em Python

Uma **API REST simples em Python** para gerenciar cursos — ideal para estudos, protótipos ou como base para projetos maiores.

Este repositório contém um backend básico que serve endpoints para criar, listar e manipular cursos (CRUD).  
O projeto está em Python e preparado para execução local.

---

## 🔧 Tabela de Conteúdos

- [📌 Sobre](#-sobre)  
- [🚀 Começando](#-começando)  
- [📦 Requisitos](#-requisitos)  
- [▶️ Executando a API](#️-executando-a-api)  
- [📑 Endpoints](#-endpoints)  
- [🛠 Tecnologias](#-tecnologias)  
- [🤝 Contribuição](#-contribuição)  
- [📄 Licença](#-licença)

---

## 📌 Sobre

Esta API foi construída como um exemplo funcional em Python, ideal para:

- aprendizado de desenvolvimento backend,
- estudo de APIs REST,
- testes com **clientes HTTP** (como Postman ou Insomnia),
- base para futuros projetos.

O código está escrito de forma clara e simples, focando em organização e funcionalidade.

---

## 🚀 Começando

Siga os passos abaixo para rodar a API no seu computador.

### 🔁 Clone o repositório

```bash
git clone https://github.com/blackkaizer/apiCursos.git
cd apiCursos
````

## 📦 Requisitos

Certifique-se de ter instalado:

* Python 3.12+
* UV (gerenciador de pacotes) - https://github.com/astral-sh/uv

---

## ▶️ Executando a API

Instale as dependências:

```bash
uv sync
```

Inicie o MongoDB via Docker:

```bash
docker compose up -d
docker ps
```

Inicie o servidor:

```bash
uv run app.py
```

A API estará disponível em:

```
http://localhost:5000
```

---

## 📑 Endpoints

- Cursos

| Método   | Rota           | Descrição                   |
| -------- | -------------- |-----------------------------|
| `GET`    | `/courses`      | Lista todos os cursos       |
| `POST`   | `/courses`      | Cria um novo curso          |
| `GET`    | `/courses/{id}` | Retorna um curso específico |
| `PUT`    | `/courses/{id}` | Atualiza um curso existente |
| `DELETE` | `/courses/{id}` | Remove um curso             |

- Auth

| Método   | Rota          | Descrição                     |
|----------|---------------|-------------------------------|
| `POST`   | `/auth`       | Cria um novo usuário          |
| `PUT`    | `/auth`       | Atualiza usuário              |
| `POST`   | `/auth/login` | Realiza a autenticação        |
| `GET`    | `/auth/{id}`  | Retorna um usuário específico |
| `DELETE` | `/auth/{id}`  | Remove um usuário             |

---

## 🛠 Tecnologias

Este projeto utiliza:

* 🐍 **Python**
* 📦 **MongoDB / Via Docker**
* 📦 Gerenciador de dependências *(UV)*
* 🧠 Estrutura de API simples para aprendizado

---

## 🤝 Contribuição

Quer contribuir? 💡

1. Faça um fork deste repositório
2. Crie uma branch com sua feature (`git checkout -b feature/nome`)
3. Commit suas alterações (`git commit -m "Descrição"`)
4. Envie para a sua branch (`git push origin feature/nome`)
5. Abra um pull request!

---

## 📄 Licença

Distribuído sob a licença **MIT**. Veja `LICENSE` para mais detalhes.

---

✨ **Obrigado por visitar o projeto!**
Se tiver dúvidas sobre como rodar ou melhorar a API, me chama! 🚀
