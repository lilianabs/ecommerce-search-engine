import streamlit as st

def app():
    st.set_page_config(page_title='🦜🔗 Home Depot products search')
    st.markdown('# 🦜🔗 Home Depot products search')
    
    input_text = st.text_input("Search:", key="query_input")
    search_type = st.radio(
        "Search Types",
        ['Keywords', 'Semantic', 'Hybrid', 'Recommendations'],
        index=0,
        key="operator_input",
        horizontal=True,
    )
    
    if st.button("SEARCH"):
        if search_type == "Keywords":
            output_data = ''
        elif search_type == "Semantic":
            output_data = ''
        elif search_type == "Hybrid":
            output_data = ''
        elif search_type == "Recommendations":
            output_data = ''
        else:
            output_data = {}
    
    st.markdown("## Search results")
    
if __name__ == '__main__':
    app()