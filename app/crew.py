from crewai import Crew, Task
from app.agents import researcher, writer
from app.schemas import ResearchResult, Article

def create_crew(query: str) -> Crew:
    # Tarefa do Pesquisador
    task_research = Task(
        description=f"Pesquisar sobre o tema: {query}. Use fontes como Wikipédia.",
        expected_output="Resumo detalhado com links úteis(referências), no minimo 500 palavras",
        agent=researcher
    )

    # Tarefa do Redator
    task_write = Task(
        description=f"Escrever um artigo sobre '{query}' com no MINIMO 300 palavras, baseado na pesquisa anterior.",
        expected_output="Artigo completo com título, conteúdo(apenas os paragrafos, e no mínimo 300 palavras) e referências.",
        agent=writer,
        output_pydantic=Article,
    )

    # Criando o Crew com agentes e tarefas
    crew = Crew(
        agents=[researcher, writer],
        tasks=[task_research, task_write],
        verbose=True
    )

    return crew
