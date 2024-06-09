from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from src.config import settings
from src.common.service.chroma_db import similarity_search_with_score


PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def query_rag(query_text: str):
    results = similarity_search_with_score(query_text)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(model="llama2", base_url=settings.OLLAMA_BASE_URL)
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"

    formatted_sources = extract_unique_items_docs_names(sources)

    res = {
        "response": response_text,
        "sources": formatted_sources,
        "formatted_response": formatted_response,
    }

    return res


def extract_unique_items_docs_names(source_list: list[str]) -> set[str]:
    # Set para armazenar valores únicos
    unique_items = set()

    for item in source_list:
        # Dividir a string no primeiro espaço após 'data\'
        parts = item.split("data\\", 1)
        if len(parts) == 2:
            # Extrair a parte após 'data\'
            file_part = parts[1]
            # Remover a parte do final ':x:x'
            file_name = file_part.rsplit(".pdf:", 1)[0]
            # Adicionar ao set
            unique_items.add(file_name)

    return unique_items
