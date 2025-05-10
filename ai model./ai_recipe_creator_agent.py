import streamlit as st
import cohere

# Initialize Cohere client with your API key
co = cohere.Client('WWCf2ZaYiofhEN70CSuXExt8AhA3FsjBAnjYRiKa')  # Replace with your actual key

# Function to generate recipes
def get_recipe(ingredients):
    # Use the Cohere API to generate the recipe
    response = co.generate(
        model='command-r-plus',  # Use 'command-r' or 'command-r-plus' as available
        prompt=f'Give me a recipe using {ingredients}.',
        max_tokens=500  # Adjust the token length as needed
    )
    
    # Access the generated text from the response
    return response.generations[0].text.strip()

# Streamlit app interface
st.title("Recipe Generator")

# User input for ingredients
ingredients = st.text_input("Enter the ingredients:", "")

if ingredients:
    # Get recipe suggestion from Cohere API
    recipe = get_recipe(ingredients)

    # Display the generated recipe
    st.subheader("Recipe Suggestion:")
    st.write(recipe)
