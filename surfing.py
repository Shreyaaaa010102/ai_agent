import streamlit as st
import llm
import serp
import helpers

# Streamlit interface
st.title("Web Search and Summary")

# User input for the search query
query = st.text_input("Enter your search query:")

# Select the model to use
selected_model = "gpt-3.5-turbo"

# Button to initiate the search
if st.button("Search"):
    if query:
        # Search the web for the query
        search_results = serp.search_google_web_automation(query)

        # Loop through the search results
        for result in search_results:
            url = result.get('url')
            if not url:
                continue  # Skip if no URL is found

            st.write(f"URL: {url}")
            st.write("Summary:")
            st.write("---------")

            try:
                # Extract the article content from the URL
                article_content = helpers.get_article_from_url(url)

                if not article_content:
                    st.write("Failed to retrieve article content.")
                    continue

                # Prepare the prompt for the language model
                prompt = f"Summarize the following article:\n\n{article_content}"

                # Generate a summary using the language model
                response = llm.llm_generate_text(prompt, "OpenAI", selected_model)

                st.write(response)
            except Exception as e:
                st.write(f"An error occurred: {e}")

            st.write("\n")
    else:
        st.write("Please enter a search query.")
