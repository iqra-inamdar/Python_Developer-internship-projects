import random


class ChatBot:

    def __init__(self):

        self.responses = {

            # Greetings
            "hello": [
                "Hello! How can I help you?",
                "Hi! Nice to meet you.",
                "Hey! How can I assist you?"
            ],

            "hi": [
                "Hi! How can I help you?",
                "Hello! Nice to meet you."
            ],

            "good morning": [
                "Good morning! Have a wonderful day.",
                "Good morning! How can I help you?"
            ],

            "good afternoon": [
                "Good afternoon! How can I help you?",
                "Good afternoon! Hope you're having a great day."
            ],

            "good evening": [
                "Good evening! How can I assist you?",
                "Good evening! Nice to chat with you."
            ],

            # General questions
            "how are you": [
                "I'm doing great! Thanks for asking.",
                "I'm fine and ready to help you."
            ],

            "what is your name": [
                "I am your AI Chatbot.",
                "You can call me Python ChatBot."
            ],

            "how old are you": [
                "I am a virtual chatbot, so I don't have an age.",
                "I don't have an age like humans do."
            ],

            "where are you": [
                "I exist inside this Python program.",
                "I'm running right here in your Python application."
            ],

            "what can you do": [
                "I can answer basic questions and have a simple conversation with you.",
                "I can respond to greetings and common questions."
            ],

            # Python
            "python": [
                "Python is a popular programming language used for AI, automation, web development, and data science.",
                "Python is a beginner-friendly and powerful programming language."
            ],

            "how can i learn python": [
                "Practice Python every day and build small projects.",
                "Start with Python basics, then learn functions, OOP, file handling, and libraries."
            ],

            # AI
            "what is ai": [
                "AI stands for Artificial Intelligence.",
                "Artificial Intelligence allows computers to perform tasks that normally require human intelligence."
            ],

            # Chatbot
            "what is chatbot": [
                "A chatbot is a computer program that communicates with users through conversation.",
                "A chatbot understands user input and provides appropriate responses."
            ],

            # Help
            "help": [
                "Sure! Tell me what you need help with.",
                "I'm here to help you."
            ],

            # Thanks
            "thank you": [
                "You're welcome!",
                "Happy to help!",
                "My pleasure!"
            ],

            "thanks": [
                "You're welcome!",
                "Anytime!",
                "Happy to help!"
            ],

            # Positive responses
            "good": [
                "Great!",
                "I'm glad to hear that!"
            ],

            "nice": [
                "Thank you!",
                "That's nice to hear!"
            ]
        }

    def get_response(self, user_input):

        user_input = user_input.lower().strip()

        # Check longer phrases first
        sorted_keywords = sorted(
            self.responses.keys(),
            key=len,
            reverse=True
        )

        for keyword in sorted_keywords:

            if keyword in user_input:
                return random.choice(self.responses[keyword])

        return "Sorry, I don't understand that. Please try another question."


# Create chatbot
bot = ChatBot()


# Welcome message
print("============================================================")
print("                 AI CHATBOT APPLICATION")
print("============================================================")



# Chat loop
while True:

    user_input = input("\nYou: ")

    # Exit commands
    if user_input.lower().strip() in ["bye", "stop", "exit", "quit"]:

        print("Bot: Goodbye! Have a great day!")
        break

    # Generate response
    response = bot.get_response(user_input)

    print("Bot:", response)