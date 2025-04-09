import requests
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class WikipediaToolInput(BaseModel):
    """Input schema for WikipediaTool."""
    query: str = Field(..., description="Termo de pesquisa para buscar na Wikipedia.")

class WikipediaTool(BaseTool):
    name: str = "Wikipedia"
    description: str = "Consulta informações da Wikipedia com base em uma pesquisa fornecida usando a API oficial."
    args_schema: type[BaseModel] = WikipediaToolInput

    def _run(self, query: str) -> str:
        """Busca o conteúdo da Wikipedia para o termo fornecido usando a API da Wikipedia."""
        url = f"https://pt.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "exintro": True,
            "titles": query,
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            pages = data.get("query", {}).get("pages", {})
            if not pages:
                return f"Nenhuma página encontrada para '{query}'."

            page = list(pages.values())[0]
            extract = page.get("extract", "Conteúdo não encontrado.")
            return extract
        except requests.exceptions.RequestException as e:
            return f"Erro ao consultar a Wikipedia: {e}"

