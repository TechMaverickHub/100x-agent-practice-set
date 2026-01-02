
import os
from dotenv import load_dotenv
from tavily import TavilyClient


load_dotenv()
def tavily_search_web(query: str) -> str:

    api_key = os.getenv("TAVILY_API_KEY")

    client = TavilyClient(api_key)

    try:
        response = client.search(
            query=query,
            max_results=3,
            include_content=True
        )
        return response.results
    except Exception as e:
        print(f"Error searching web: {e}")
        return ""



    