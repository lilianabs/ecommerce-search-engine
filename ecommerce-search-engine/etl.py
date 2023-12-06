import weaviate
import pandas as pd
import os
from tqdm import tqdm
from dotenv import load_dotenv  

RAW_DATA_PATH = "../data/home_depot_data_1_2021_12.csv"
RAW_DATA_COLS = ['title', 'description', 'brand', 'price']

def get_raw_data(path, cols):
    df = pd.read_csv(path)
    df = df[cols]
    return df

def get_weaviate_client():
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
    
    return client

def create_schema_weaviate(client):
    #Checking if schema already exists, then delete it
    current_schemas = client.schema.get()['classes']
    for schema in current_schemas:
        if schema['class']=='Products':
            client.schema.delete_class('Products')
            
    #creating the schema
    products_class_schema = {
        "class": "Products",
        "description": "A collection of Home Depot products.",
        "vectorizer": "text2vec-openai",
        "vectorIndexConfig" : {
            "distance" : "cosine",
        },
        "moduleConfig": {
            "text2vec-openai": {
                "vectorizeClassName": False,
                "model": "ada",
                "modelVersion": "002",
                "type": "text"
            },
        },
    }
    
    products_class_schema["properties"] = [
        {
            "name": "title",
            "dataType": ["text"],
            "description": "The name of item",   
        },
        {
            "name": "description",
            "dataType": ["text"],
            "description": "The description of item",   
        },
        {
            "name": "brand",
            "dataType": ["text"],
            "description": "The brand of item",   
        },
        {
            "name": "price",
            "dataType": ["number"],
            "description": "The price of the item", 
            "moduleConfig": {
                "text2vec-openai": {  
                    "skip" : True,
                    "vectorizePropertyName" : False
                }
            }   
        },
    ]
    
    client.schema.create_class(products_class_schema)


def load_data_weaviate(client, df):
    # Configure batch process - for faster imports 
    client.batch.configure(
    batch_size=10, 
    dynamic=True,   # dynamically update the `batch_size` based on import speed
    timeout_retries=3,
    )

    # Importing the data
    for i in tqdm(range(len(df))):
        item = df.iloc[i]
        
        product_object = {
            'title': str(item['title']).lower(),
            'description': str(item['description']).lower(),
            'brand': str(item['brand']).lower(),
            'price':float(item['price']),
        }

        try:
            client.batch.add_data_object(product_object, "Products")
        except BaseException as error:
            print("Import Failed at: ",i)
            print("An exception occurred: {}".format(error))
            # Stop the import on error
            break

    print(client.query.aggregate("Products").with_meta_count().do())
    client.batch.flush()

def main():
    df = get_raw_data(RAW_DATA_PATH , RAW_DATA_COLS)
    client = get_weaviate_client()
    create_schema_weaviate(client)
    load_data_weaviate(client, df)

if __name__ == "__main__":
    load_dotenv()  
    main()