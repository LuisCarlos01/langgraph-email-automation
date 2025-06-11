from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from src.structure_outputs import *
from src.prompts import *
from db.database import SessionLocal
from db.models import Email, EmailStatus
from db.crud import buscar_similares

class Agents():
    def __init__(self):
        # Choose which LLMs to use for each agent
        llm = ChatOpenAI(model_name="gpt-4", temperature=0.1)
        
        # Configure embeddings for semantic search
        self.embeddings = OpenAIEmbeddings()
        
        # Database session
        self.db = SessionLocal()

        # Categorize email chain
        email_category_prompt = PromptTemplate(
            template=CATEGORIZE_EMAIL_PROMPT, 
            input_variables=["email"]
        )
        self.categorize_email = (
            email_category_prompt | 
            llm.with_structured_output(CategorizeEmailOutput)
        )

        # Used to design queries for RAG retrieval
        generate_query_prompt = PromptTemplate(
            template=GENERATE_RAG_QUERIES_PROMPT, 
            input_variables=["email"]
        )
        self.design_rag_queries = (
            generate_query_prompt | 
            llm.with_structured_output(RAGQueriesOutput)
        )
        
        # Generate answer to queries using RAG and database context
        qa_prompt = ChatPromptTemplate.from_template(GENERATE_RAG_ANSWER_PROMPT)
        self.generate_rag_answer = (
            {"context": self._get_similar_emails, "question": RunnablePassthrough()}
            | qa_prompt
            | llm
            | StrOutputParser()
        )

        # Used to write a draft email based on category and related informations
        writer_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", EMAIL_WRITER_PROMPT),
                MessagesPlaceholder("history"),
                ("human", "{email_information}")
            ]
        )
        self.email_writer = (
            writer_prompt | 
            llm.with_structured_output(WriterOutput)
        )

        # Verify the generated email
        proofreader_prompt = PromptTemplate(
            template=EMAIL_PROOFREADER_PROMPT, 
            input_variables=["initial_email", "generated_email"]
        )
        self.email_proofreader = (
            proofreader_prompt | 
            llm.with_structured_output(ProofReaderOutput) 
        )

    def _get_similar_emails(self, query: str) -> str:
        """
        Recupera e-mails similares do banco de dados usando embeddings.
        """
        try:
            # Gera embedding para a consulta
            query_embedding = self.embeddings.embed_query(query)
            
            # Busca e-mails similares usando a função do crud
            similar_emails = buscar_similares(self.db, query_embedding)
            
            # Formata o contexto
            context = []
            for email in similar_emails:
                context.append(f"Assunto: {email.assunto}\nPergunta: {email.conteudo}\nResposta: {email.resposta_editada or email.resposta_gerada}")
            
            return "\n\n".join(context) if context else "Nenhum e-mail similar encontrado."
            
        except Exception as e:
            print(f"Erro ao buscar e-mails similares: {e}")
            return "Erro ao buscar e-mails similares."