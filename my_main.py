# my_main.py
# Mini-Project: Coastal Coffee Assistant

from my_assistant import CoffeeAssistant
from my_tool import FAQLookup

# Frequently asked questions for Coastal Coffee.
FAQS = {
    "hours": "We are open Monday through Saturday from 7 AM to 6 PM.",
    "location": "Coastal Coffee is located at 123 Beach Street.",
    "wifi": "Yes! We offer free Wi-Fi to all customers.",
    "menu": "We serve coffee, tea, pastries, and sandwiches.",
    "parking": "Free parking is available behind the shop.",
}


# Create the FAQ lookup tool using our mock data.
faq_tool = FAQLookup(FAQS)

# Create the Coastal Coffee assistant.
assistant = CoffeeAssistant("Coastal Coffee Bot", faq_tool)


# Start the customer service conversation.
print("Welcome to Coastal Coffee!")
print("Type 'quit' to exit.")

while True:
    user_message = input("You: ")

    if user_message.lower() == "quit":
        break

    reply = assistant.respond(user_message)
    print("Assistant:", reply)

print("Conversation history:", len(assistant.history))
