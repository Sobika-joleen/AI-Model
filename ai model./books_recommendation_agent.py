import streamlit as st
import cohere

# Initialize Cohere client with your API key
cohere_client = cohere.Client('your_cohere_api')

# Streamlit interface
st.title("Book Recommendation Agent - Shelfie")

# Get input from the user
user_input = st.text_input("What books have you enjoyed recently?", "")

# Function to get book recommendations from Cohere
def get_book_recommendations(user_input):
    # Define the prompt to ask Cohere for book recommendations
    prompt = f"Suggest books similar to the ones that the user liked: '{user_input}'. Include book titles, authors, a short summary, and why they are recommended."
    
    # Make the API call to Cohere to generate the response
    response = cohere_client.generate(
        model='command-r-plus',  # Use 'command-r' or 'command-r-plus'
        prompt=prompt,
        max_tokens=500  # Adjust the token length as needed
    )
    
    # Return the generated text (book recommendations)
    return response.generations[0].text.strip()

if user_input:
    # Get book recommendations from Cohere
    st.subheader("Book Recommendations:")
    book_recommendations = get_book_recommendations(user_input)
    
    # Display the recommendations on Streamlit
    st.write(book_recommendations)
