# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar livros usando FastAPI. Ao concluir a atividade, você saberá definir endpoints, validar dados com modelos Pydantic e retornar respostas HTTP apropriadas.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description
Complete o arquivo `starter-code.py` e execute a aplicação localmente com Uvicorn. Comece criando a aplicação FastAPI e um endpoint de verificação de saúde.

#### Requirements
O programa concluído deve:

- Criar uma instância de `FastAPI` com um título descritivo
- Implementar `GET /health` retornando `{"status": "ok"}`
- Permitir que a aplicação seja iniciada com `uvicorn starter-code:app --reload`


### 🛠️ List and Filter Books

#### Description
Implemente o endpoint que lista os livros armazenados em memória. Adicione um filtro opcional por gênero usando um parâmetro de consulta.

#### Requirements
O programa concluído deve:

- Implementar `GET /books`
- Retornar uma lista de objetos contendo `id`, `title`, `author` e `genre`
- Aceitar `genre` como parâmetro opcional e retornar apenas os livros correspondentes, sem diferenciar maiúsculas de minúsculas
- Retornar uma lista vazia quando nenhum livro corresponder ao filtro


### 🛠️ Create Books with Validation

#### Description
Crie um modelo Pydantic para os dados recebidos e implemente o endpoint de criação. A API deve rejeitar dados incompletos ou inválidos automaticamente.

#### Requirements
O programa concluído deve:

- Implementar `POST /books`
- Exigir `title`, `author` e `genre` como strings não vazias
- Gerar um `id` inteiro único para cada novo livro
- Retornar o livro criado com status HTTP `201`

Exemplo de requisição:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien",
  "genre": "fantasy"
}
```


### 🛠️ Update and Delete Books

#### Description
Complete os endpoints de atualização e remoção para transformar a API em um CRUD. Use erros HTTP claros quando o `id` não existir.

#### Requirements
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para substituir os dados de um livro
- Implementar `DELETE /books/{book_id}` e retornar status HTTP `204` sem conteúdo
- Retornar status HTTP `404` para IDs inexistentes
- Manter os dados atualizados disponíveis em chamadas posteriores a `GET /books`