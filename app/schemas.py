from pydantic import BaseModel
from typing import List, Optional

# Modelo para a pesquisa do Pesquisador
class ResearchResult(BaseModel):
    title: str
    content: str
    references: Optional[List[str]] = []

# Modelo para o artigo do Redator
class Article(BaseModel):
    title: str
    content: str
    references: Optional[List[str]] = []

    class Config:
        # Configuração para garantir que os dados sejam formatados corretamente
        min_anystr_length = 1
        anystr_strip_whitespace = True
