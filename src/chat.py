import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from src.search import searchQuestion

load_dotenv()

def main():
    question = input("Pergunta: ").strip()
    if not question:
        print("Digite uma pergunta.")
        return

    results = searchQuestion(question)
    context = "\n\n---\n\n".join(doc.page_content for doc, _ in results)

    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="""Responda somente com base no
  CONTEXTO: {context}. 
  Nunca invente ou use conhecimento externo.
  Nunca produza opiniões ou interpretações além do que está escrito.
  Se a informação não estiver explicitamente no CONTEXTO, responda:
  Não tenho informações necessárias para responder sua pergunta.
  Pergunta: {question}
""",
    )

    llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

    chain = prompt_template | llm | StrOutputParser()

    response = chain.invoke({"context": context, "question": question})
    print(f"Resposta: {response}")

if __name__ == "__main__":
    main()
