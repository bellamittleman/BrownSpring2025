import openai

# Directly set your API key here
openai.api_key = 'here'

# Create a completion using the OpenAI API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello! How can I use the OpenAI API?"}
    ]
)

# Print the response from the API
print(response['choices'][0]['message']['content'])
