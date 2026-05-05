from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

CAMINHO_DB= 'db'

promt_template = """
Responda a pergunrta do usuário:
{pergunta}
com base nessas informações abaixo:
{base_conhecimento}
 """

def perguntar():
    pergunta= input("Escreva sua pergunta: ")

    funcao_embbeding = OpenAIEmbeddings()
    db=Chroma(persist_directory=CAMINHO_DB, embedding_function=funcao_embbeding )

    resultados = db.similarity_search_with_relevance_scores(pergunta, k=3)
    if len(resultados) == 0 or resultados[0][1] < 0.7:
        print("Nenhuma informação relevante na base")
        return
    textos_resultado = []
    for resultado in resultados:
        texto = resultado[0].page_content
        textos_resultado.append(texto)

    base_conhecimento = "\n\n----\n\n".join(textos_resultado)
    prompt = ChatPromptTemplate.from_template(promt_template)
    prompt = prompt.invoke({"pergunta": pergunta, "base_conhecimento": base_conhecimento})

    modelo = ChatOpenAI()
    texto_resposta = modelo.invoke(prompt).content
    print("Resposta da IA:", texto_resposta)

perguntar()