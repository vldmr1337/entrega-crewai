from crewai import Agent
from app.llm import get_gemini_llm
from app.tools import WikipediaTool
from app.schemas import ResearchResult, Article
from dotenv import load_dotenv
import os

# Carregar as variáveis do arquivo .env
load_dotenv()

api_key = os.getenv("GEMINI_KEY")
llm = get_gemini_llm(api_key)

# Ferramenta personalizada para Wikipedia
wikipedia_tool = WikipediaTool()

# Função que usa o WikipediaTool para buscar informações
def researcher_search(query: str) -> ResearchResult:
    search_result = wikipedia_tool.search(query)
    # Criando um ResearchResult Pydantic
    return ResearchResult(title=query, content=search_result)

# Criando o agente Pesquisador
researcher = Agent(
    role="Pesquisador",
    goal="Pesquisar informações detalhadas e confiáveis na Wikipédia",
    backstory="Especialista em buscar e validar conteúdo.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[wikipedia_tool]
)

# Criando o agente Redator
writer = Agent(
    role="Redator",
    goal="Escrever um artigo completo com base nas informações do pesquisador",
    backstory="Especialista em transformar dados em texto coeso.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

