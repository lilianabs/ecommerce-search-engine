import weaviate
import os
from dotenv import load_dotenv 


def get_weaviate_client():
    weaviate_url = os.getenv("WEAVIATE_URL")
    
    client = weaviate.Client(
    url = weaviate_url,
    )
    
    return client

def get_similar_products(client, max_num_products):
    result = client.query.get(
        class_name='Products',
        properties=['title', 'description', 'brand', 'price']
    ).with_limit(max_num_products) \
        .with_near_text({'concepts': ['description']}) \
        .do()
    
    #print(result)
    print(result['data']['Get']['Products'])
    print("Number of results: ", len(result['data']['Get']['Products']))
    
    
def get_products_by_keyword(client, text, max_num_products):
    result = client.query.get(
        class_name='Products',
        properties=['title', 'description', 'brand', 'price']
    ).with_bm25(
        query=text,
        properties=['title', 'description^']
    ).with_limit(max_num_products) \
    .with_near_text({'concepts': ['description']}) \
    .do()
        
    print(result['data']['Get']['Products'])

def main():
    client = get_weaviate_client()
    text = 'duvet set'
    max_num_products = 10
    get_products_by_keyword(client, text, max_num_products)
    #get_similar_products(client, max_num_products)

if __name__ == "__main__":
    load_dotenv()  
    main()