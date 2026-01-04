# memory.py
import os

from dotenv import load_dotenv
from supabase import create_client, Client
from sentence_transformers import SentenceTransformer


load_dotenv()
model = SentenceTransformer("all-MiniLM-L6-v2")

def init_memory():
    """Initialize Supabase client"""

    url: str = os.getenv("SUPABASE_URL")
    key: str = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    return supabase

def embed_text(text: str) -> list[float]:
    """Generate embedding"""
    embeddings = model.encode(text).tolist()


    return embeddings


def store_memory(question: str, answer: str):
    """Store Q&A + embedding"""

    embeddings = embed_text(question + " " + answer)

    supabase = init_memory()

    data = {
        "question": question,
        "answer": answer,
        "embedding": embeddings
    }

    supabase.table("agent_memory").insert(data).execute()



def search_memory(query: str, threshold: float = 0.7, top_k: int = 3) -> list[dict]:
    """Semantic search over past interactions"""

    query_embedding = embed_text(query)

    supabase = init_memory()

    response = supabase.rpc(
        "match_agent_memory",
        {
            "query_embedding": query_embedding,
            "similarity_threshold": threshold,
            "match_count": 3
        }
    ).execute()

    return response.data or []



