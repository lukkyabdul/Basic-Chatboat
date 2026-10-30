def get_bot_response(user_input):
    """
    Processes the user's input string and returns a predefined response.
    Converts text to lowercase and strips whitespace for reliable matching.
    """
    # Normalize input: convert to lowercase and remove leading/trailing spaces
    cleaned_input = user_input.lower().strip()

    if cleaned_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you today?"
    elif cleaned_input in ["how are you", "how are you?", "how's it going"]:
        return "I'm fine, thanks for asking! How are you?"
    elif cleaned_input in ["what is your name", "what's your name", "who are you"]:
        return "I am a basic Python rule-based chatbot."
    elif cleaned_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Try saying 'hello', 'how are you', or 'bye'."


def run_chatbot():
    """
    Main loop to run the chatbot until the user decides to exit.
    """
    print("--- Basic Rule-Based Chatbot ---")
    print("Type your message below (or type 'bye' to quit):\n")

    while True:
        # Take input from the user
        user_text = input("You: ")

        # Get response from the bot function
        bot_text = get_bot_response(user_text)

        # Print the bot's reply
        print(f"Bot: {bot_text}")

        # Break the loop if user says goodbye/exit
        if user_text.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


# Run the chatbot program
if __name__ == "__main__":
    run_chatbot()