
# Sistema Multiagente para Geração de Artigos Utilizando CrewAI

Este projeto utiliza o framework **CrewAI** para automatizar a criação de artigos com base em informações extraídas da **Wikipedia**. Ele envolve agentes que realizam pesquisas e geram artigos com pelo menos 300 palavras sobre um determinado tema.

## Funcionalidades

- **Pesquisador**: Realiza a pesquisa sobre o tema desejado, utilizando a Wikipedia.
- **Redator**: Escreve um artigo completo baseado nas informações coletadas pelo pesquisador.
- **API**: A aplicação expõe uma API utilizando **FastAPI** para gerar artigos.

## Requisitos

- **Python 3.9+**
- **FastAPI** para a criação da API.
- **CrewAI** para gerenciamento de agentes e execução das tarefas.
- **Uvicorn** como servidor ASGI.
- **Pydantic** para validação de dados.
- **requests** para interagir com a Wikipedia.

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

2. Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
# Para Windows
venv\Scripts\activate
# Para Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` para armazenar suas variáveis de ambiente (como a chave da API do Gemini, se necessário).

## Como usar

### Executar a API

1. Após configurar o ambiente, inicie a aplicação:

```bash
uvicorn app.main:app --reload
```

2. Acesse a API em `http://127.0.0.1:8000`.

### Gerar um Artigo

1. Envie uma requisição GET para o endpoint `/generate`, passando o `query` com o tema do artigo.

Exemplo de URL:
```
http://127.0.0.1:8000/generate?query=Brasil
```

### Exemplo de resposta:

```json
{
  "title": "Brasil: História, Cultura e Geografia",
  "content": "O Brasil é um país localizado na América do Sul. Com uma história rica, o Brasil..."
}
```

## Estrutura do Projeto

```
.
├── app/
│   ├── agents.py         # Definições dos agentes (Pesquisador e Redator)
│   ├── crew.py           # Gerenciamento das tarefas e criação da equipe
│   ├── llm.py            # Função para obter o LLM (Gemini)
│   ├── main.py           # Arquivo principal da API FastAPI
│   ├── schemas.py        # Modelos Pydantic
│   └── tools.py           # Ferramenta da Wikipedia
├── .env                  # Variáveis de ambiente
├── requirements.txt      # Dependências do projeto
└── README.md             # Este arquivo
```

## Dependências

- **FastAPI**: Framework para criação de APIs.
- **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.
- **CrewAI**: Framework para criação e gerenciamento de agentes inteligentes.
- **Pydantic**: Utilizado para a validação e estruturação dos dados.
- **requests**: Biblioteca para fazer requisições HTTP, usada para integrar com a Wikipedia.
- **python-dotenv**: Para carregar variáveis de ambiente de um arquivo `.env`.

## Contribuição

Sinta-se à vontade para fazer contribuições neste projeto. Se você tiver sugestões de melhorias, correções ou novas funcionalidades, crie um **pull request**.

1. Faça um fork deste repositório.
2. Crie uma branch para a sua funcionalidade (`git checkout -b feature/MinhaFuncionalidade`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin feature/MinhaFuncionalidade`).
5. Crie um **pull request**.

## Licença

Este projeto é licenciado sob a MIT License - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
