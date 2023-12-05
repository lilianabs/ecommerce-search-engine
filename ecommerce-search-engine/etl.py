import weaviate
import pandas as pd
import os
from tqdm import tqdm
from dotenv import load_dotenv  

def main():
    openai_key = os.getenv("OPENAI_API_KEY")
    weaviate_url = os.getenv("WEAVIATE_URL")
    weaviate_key = os.getenv("WEAVIATE_KEY")
    
    #auth_config = weaviate.AuthApiKey(api_key=weaviate_key)
    
    client = weaviate.Client(
    url = weaviate_url,
    #auth_client_secret=auth_config,
    additional_headers={
         "X-OpenAI-Api-Key": openai_key,
    }
    )


if __name__ == "__main__":
    load_dotenv()  
    main()