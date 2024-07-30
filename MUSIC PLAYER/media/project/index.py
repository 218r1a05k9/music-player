class MockOpenAI:
    @staticmethod
    def ChatCompletion_create(model, messages):
        # This is a mock response for demonstration purposes.
        user_message = messages[-1]["content"]
        return {
            "choices": [
                {
                    "message": {
                        "content": f"Mock response to: {user_message}"
                    }
                }
            ]
        }

# Set the mock OpenAI class
openai = MockOpenAI()

# Initial system message to set the assistant's behavior
messages = [{"role": "system", "content": "You are an intelligent assistant."}]

# Infinite loop to continuously take user input
while True:
    # Take user input
    user_input = input("User: ")
    
    # Break the loop if the user types 'exit'
    if user_input.lower() == "exit":
        break
    
    # Add the user message to the conversation history
    if user_input:
        messages.append({"role": "user", "content": user_input})
        
        # Get the assistant's response from the mock API
        response = openai.ChatCompletion_create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        # Extract the assistant's reply
        reply = response["choices"][0]["message"]["content"]
        
        # Print the assistant's reply
        print(f"ChatGPT: {reply}")
        
        # Add the assistant's reply to the conversation history
        messages.append({"role": "assistant", "content": reply})
        