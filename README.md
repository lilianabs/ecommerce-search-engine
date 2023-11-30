# ecommerce-search-engine
A search engine for ecommerce data. It uses the OpenAI API and the [Home Depot dataset](https://www.kaggle.com/datasets/thedevastator/the-home-depot-products-dataset).

## Run the project
Before running the application locally, make sure you have Python 3.9+ installed.

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

1. Run the application: 

   ```
   streamlit run main.py
   ```