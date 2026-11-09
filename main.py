# main.py
# Author: aevlin

# Import the chatbot and order lookup classes.
from chatbot import SupportChatbot
from inventory_tool import InventoryLookup
from ollama_model import OllamaModel
from order_tool import OrderLookup

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Sunny, a support assistant for Bayside Outfitters.
Answer in one short sentence.
Store hours are 10 am to 7 pm every day.
Returns are accepted within 30 days with a receipt.
Shipping takes 3 to 5 business days.
Sale items cannot be returned.
Only state facts that appear in these instructions.
If you do not know, say you do not know and offer to pass
the customer to a human agent."""
# Create a dictionary of example orders.
ORDERS = {
    "A100": "shipped",
    "A101": "processing",
    "A102": "delivered",
}

# Create a dictionary of products and quantities.
INVENTORY = {
    "rain jackets": 12,
    "backpacks": 8,
    "water bottles": 25,
}


# Create the order lookup tool.
order_tool = OrderLookup(ORDERS)

# Create the inventory lookup tool.
inventory_tool = InventoryLookup(INVENTORY)


# Create the chatbot and give it the tool.
bot = SupportChatbot(
    "Sunny", "You are a friendly support assistant for Bayside Outfitters.", order_tool
)

# Create Sunny with both tools.
bot = SupportChatbot(
    "Sunny",
    "You are a friendly support assistant for Bayside Outfitters.",
    order_tool,
    inventory_tool,
)

# Tell the user how to start.
print("Type a message, or type quit to stop.")

# Ask for the first message.
user_message = input("You: ")

# Keep chatting until the user types quit.
while user_message != "quit":
    # Get and print the chatbot's response.
    print(f"{bot.name}: {bot.respond(user_message)}")

    # Ask for the next message.
    user_message = input("You: ")

# Show the total number of messages.
print(f"Messages in this conversation: {len(bot.history)}")
