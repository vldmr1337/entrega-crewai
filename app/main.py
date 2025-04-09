from fastapi import FastAPI, Query, HTTPException
from app.schemas import Article  # Modelo Article já existente
from app.crew import create_crew

app = FastAPI()

@app.get("/generate", response_model=Article)
async def generate_article(query: str = Query(..., description="Tema do artigo")):
    """
    Gera um artigo com base no tema fornecido, buscando informações na Wikipedia
    e gerando um artigo com no mínimo 300 palavras.
    """
    # Cria o Crew com as tarefas de pesquisa e redação
    crew = create_crew(query)
    result = crew.kickoff()  # Executa o Crew e obtém o resultado

    if result.raw is None:
        raise HTTPException(status_code=500, detail="A saída gerada é None. Verifique a execução do crew.")
    
    generated_text = result.pydantic

    # Se não houver conteúdo gerado, lançar erro
    if not generated_text:
        raise HTTPException(status_code=500, detail="Não foi possível gerar o artigo. Verifique os agentes.")
    
    # Agora apenas retornamos o resultado como Article
    return generated_text
