def chatbot():
    while True:
        user_input = input("You: ").lower().strip()
        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "help":
            print("Bot: Available commands: hello, how are you, bye, help, name, time")
        elif user_input == "Who are you?":
            print("Bot: I'm a basic bot, nice to meet you!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Try 'hello', 'how are you', 'bye', 'help', 'name', or 'time'.")
chatbot()