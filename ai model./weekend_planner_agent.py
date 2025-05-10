import streamlit as st
import cohere

# Initialize Cohere client with your API key
cohere_client = cohere.Client('WWCf2ZaYiofhEN70CSuXExt8AhA3FsjBAnjYRiKa')

# Streamlit interface
st.title("Weekend Planning Assistant - TimeOut")

# Get input from the user for their weekend plan prompt
user_input = st.text_area("Enter your weekend plan request:", 
                          "I want to plan my coming weekend filled with fun activities and Christmas-themed activities in Bangalore for 21 and 22 Dec 2024.")

# Function to generate the weekend plan from Cohere
def get_weekend_plan(user_input):
    # Define the prompt to ask Cohere for the weekend plan
    prompt = f"Plan a weekend itinerary for the user. Include events, activities, and dining options. The user provided the following request: '{user_input}'. Ensure all recommendations are for the specified dates and location. Provide the plan in sections: Events, Activities, Dining Options."

    # Make the API call to Cohere to generate the response
    response = cohere_client.generate(
        model='command-r-plus',  # Use 'command-r' or 'command-r-plus'
        prompt=prompt,
        max_tokens=600  # Adjust the token length as needed
    )

    # Return the generated text (weekend plan)
    return response.generations[0].text.strip()

if user_input:
    # Get the weekend plan from Cohere
    st.subheader("Weekend Plan:")
    weekend_plan = get_weekend_plan(user_input)
    
    # Display the weekend plan on Streamlit
    st.write(weekend_plan)
