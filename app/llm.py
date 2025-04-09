from crewai import LLM

def get_gemini_llm(api_key):
    llm = LLM(
        model="gemini/gemini-1.5-pro-latest",
        temperature=0.7,
        api_key=api_key  # Passando a chave de API diretamente
    )
    return llm


