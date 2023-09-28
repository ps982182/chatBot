# Chatbot
import nltk
from nltk.chat.util import Chat, reflections
chatbot_responses = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am just a chatbot, but I am here to help!', 'I don\'t have feelings, but thanks for asking. How can I assist you?']),
    (r'what is your name?', ['I am a chatbot.', 'You can call me ChatGPT.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Have a great day!']),
]

chatbot = Chat(chatbot_responses, reflections)

def chat_with_bot():
    print("Hello! I'm your chatbot. You can type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat_with_bot()
