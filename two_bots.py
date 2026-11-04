# Exercise 4 - Two Chatbots From One Class

# Import the chatbot class.
from chatbot import SupportChatbot

# Import the inventory lookup tool.
from inventory_tool import InventoryLookup

# Import the order lookup tool.
from order_tool import OrderLookup

# Create sample order data.
ORDERS = {
    "A100": "shipped",
    "A101": "processing",
    "A102": "delivered",
}

# Create sample inventory data.
INVENTORY = {
    "rain jackets": 12,
    "backpacks": 8,
    "water bottles": 25,
}

# Create one shared order lookup tool.
order_tool = OrderLookup(ORDERS)

# Create one shared inventory lookup tool.
inventory_tool = InventoryLookup(INVENTORY)


# Create Sunny, a cheerful and brief chatbot.
sunny = SupportChatbot(
    "Sunny", "You are cheerful and brief.", order_tool, inventory_tool
)

# Create River, a formal and detailed chatbot.
river = SupportChatbot(
    "River", "You are formal and detailed.", order_tool, inventory_tool
)

# Send two messages to Sunny.
sunny_first_reply = sunny.respond("hello")
sunny.respond("Where is order A100?")

# Send one message to River.
river_first_reply = river.respond("hello")

# Display Sunny's information.
print("Sunny's name:", sunny.name)
print("Sunny's instructions:", sunny.instructions)
print("Sunny's first reply:", sunny_first_reply)
print("Sunny's history length:", len(sunny.history))

print()

# Display River's information.
print("River's name:", river.name)
print("River's instructions:", river.instructions)
print("River's first reply:", river_first_reply)
print("River's history length:", len(river.history))
