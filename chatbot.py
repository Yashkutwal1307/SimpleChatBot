print("=== Simple Chatbot ===")
print("Type 'bye' to exit.\n")

def get_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if any(word in user_input for word in ["hello", "hi", "hey", "hola", "yo", "sup"]):
        return "Hey! Nice to see you 😊"

    if "good morning" in user_input:
        return "Good morning! Have a productive day 🌞"

    if "good night" in user_input:
        return "Good night! Sleep well 😴"

    # Basic Q's
    if "how are you" in user_input:
        return "I'm doing awesome! Thanks for asking 😄"

    if "what's up" in user_input or "whats up" in user_input or "wassup" in user_input:
        return "Nothing much, just chatting with you!"

    if "what are you doing" in user_input:
        return "Just waiting to answer your questions 😉"

    
    if "your name" in user_input:
        return "I'm your simple Python chatbot!"

    if "who created you" in user_input:
        return "You did! And you did a great job 😄"

    # Jokes
    if "joke" in user_input:
        jokes = [
            "Why don’t skeletons fight each other? They don’t have the guts! 😂",
            "Why did the math book look sad? Because it had too many problems 😭",
            "I'm reading a book on anti-gravity. It's impossible to put down! 😆"
        ]
        import random
        return random.choice(jokes)

    # Feelings or moods
    if "i am sad" in user_input or "i'm sad" in user_input:
        return "Aww… I’m here for you! Want to talk about it? 🤍"

    if "i am happy" in user_input or "i'm happy" in user_input:
        return "Yay! I love hearing that! 😄✨"

    if "i am bored" in user_input:
        return "Hmm… want a joke? Or maybe I can suggest a game 🎮"

    # Study and motivation
    if "study" in user_input or "motivate" in user_input:
        return "You got this! Even a small step today counts. 📚🔥"

    if "give me advice" in user_input:
        return "Do something today that your future self will thank you for 💪"

    # Weather
    if "weather" in user_input:
        return "I can't check real weather, but I hope it's sunny in your life ☀️"

    # Date and time
    if "time" in user_input:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')} 🕒"

    if "date" in user_input:
        from datetime import datetime
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')} 📅"

    # Fun Q's
    if "favorite color" in user_input:
        return "I like all colors, but blue feels peaceful 🌊"

    if "favorite food" in user_input:
        return "I don’t eat, but I think pizza looks amazing 🍕"

   # Thanks
    if "thank" in user_input:
        return "You're welcome! Anytime 😊"

    # Insults
    if any(word in user_input for word in ["stupid", "dumb", "idiot"]):
        return "Oof… that hurt 😢 But I still like you."

    # Exit
    if "bye" in user_input or "exit" in user_input:
        return "Goodbye! Take care 👋"

    # Default fallback
    return "I didn't fully understand that, but I'm learning 😄"



while True:
    user = input("You: ")

    response = get_response(user)
    print("Bot:", response)

    if "bye" in user.lower() or "exit" in user.lower():
        break
