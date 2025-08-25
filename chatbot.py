
# Simple Rule-based Chatbot

def chatbot():
    print("🤖 Chatbot: Hello! I am your chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()   # User input ko lowercase me convert
       
        if user_input in ["hi", "hello", "hey"]:
            print("🤖 Chatbot: Hello! How are you?")
        
        elif user_input in ["i am fine", "i am good", "fine"]:
            print("🤖 Chatbot: Glad to hear that! 😊")
        
        elif user_input in ["how are you", "how r u"]:
            print("🤖 Chatbot: I'm just a program, but I'm doing great! 😃")
        
        elif "name" in user_input:
            print("🤖 Chatbot: My name is PyBot. What's your name?")
        
        elif "weather" in user_input:
            print("🤖 Chatbot: Sorry, I can't check weather right now. 🌦")
        
        elif "bye" in user_input:
            print("🤖 Chatbot: Goodbye! Have a great day 👋")
            break
        
        else:
            print("🤖 Chatbot: Sorry, I don't understand that. Can you rephrase?")

# Run chatbot
chatbot()