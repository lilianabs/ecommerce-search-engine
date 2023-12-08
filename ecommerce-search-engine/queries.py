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
    
async function get_keyword_results(text) {
    let data = await client.graphql
        .get()
        .withClassName('Movies')
        .withBm25({query: text,
            properties: ['title^3', 'director', 'genres', 'actors', 'keywords', 'description', 'plot'],
    })
        .withFields(['title', 'poster_link', 'genres', 'year', 'director', 'movie_id'])
        .withLimit(num_movies)
        .do()
        .then(info => {
            return info
        })
        .catch(err => {
            console.error(err)
        })
    return data;
    
def get_products_by_keyword(client, text):
    
    

def main():
    client = get_weaviate_client()
    get_similar_products(client, 10)

if __name__ == "__main__":
    load_dotenv()  
    main()