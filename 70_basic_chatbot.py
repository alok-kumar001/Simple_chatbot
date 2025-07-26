def simple_chatbot():
    print("🤖 Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks!")
        elif user_input == "what is your name":
            print("🤖 Chatbot: I'm a simple chatbot.")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day!")
            break
        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

# Run the chatbot
simple_chatbot()
