from crewai import LLM

def get_gemini_llm(api_key):
    llm = LLM(
        model="gemini/gemini-2.0-flash",
        temperature=0.7,
        api_key=api_key  # Passando a chave de API diretamente
    )
    return llm


