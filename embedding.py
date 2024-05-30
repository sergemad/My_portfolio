from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)

def get_embedding_function():
    #embeddings = BedrockEmbeddings(credentials_profile_name="default", region_name="us-east-1")
    #embeddings = OllamaEmbeddings(model="nomic-embed-text")
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings