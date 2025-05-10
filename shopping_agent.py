import cohere  # type: ignore

# Initialize Cohere client with your API key
co = cohere.Client('your_api_key')  # Replace with your actual key

# Ask user for their shopping preferences
shopping_preference = input("What are you looking to buy? ")

# Prepare message for shopping recommendations
message = f"I'm looking to buy: {shopping_preference}. Can you recommend 5 products with short descriptions for each?"

# Use chat endpoint to get shopping recommendations
response = co.chat(
    model='command-r-plus',  # Or 'command-r' if that's your plan
    message=message
)

# Print the response
print("\n🛒 Recommended Products:\n")
print(response.text.strip())
