# ecommerce-search-engine
This repository (mono repo) contains a search engine for ecommerce data. It implements keyword, semantic and hybrid search. For storing the data as vectors, it uses Weaviate (via Docker). It can use any LLM of your choice.

## Subprojects
This repository contains the following subprojects:

- **Hybrid search:** Contains a set of modules for searching trhough the e-commerce data. It supports keyword, semantic and hybric search.
- **Seach engine api:** Contains an API to use the different types of search that the subproject above offers.
- **Search engine app**: Contains an application that interacts with the Search engine API.

## Data
This project uses the [Home Depot dataset](https://www.kaggle.com/datasets/thedevastator/the-home-depot-products-dataset) from Kaggle, which contains 2,551 product records from Home Depot. Each product includes metadata such as title, description, brand, price, SKU, and availability. This dataset serves as the foundation for developing and testing keyword, semantic, and hybrid search capabilities across ecommerce product catalogs.

## Running the project (deprecated)
Before running the application locally, make sure you have Python 3.13+ installed.

To run the application, follow these steps:

1. Create a new Python environment:

   ```
   python -m venv venv
   ```

1. Activate the Python environment:

   ```
   source venv/bin/activate
   ```

1. Update pip:

   ```
   python -m pip install --upgrade pip
   ```

1. Install the project requirements:

   ```
   python -m pip install -r requirements.txt
   ```

1. Add OpenAI key to .env file

1. Run the docker container, add key to docker-compose.yml

1. Run the etl process to load the data into the vector database:

   ```
   cd ecommerce-search-engine
   python etl.py
   ```


2. Run the application: 

   ```
   streamlit run main.py
   ```

### Using the venv in Vscode

Create file `.vscode/settings.json` with the following:

   ```
  {
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.terminal.activateEnvironment": true
  }
   ```
