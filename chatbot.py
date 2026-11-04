# chatbot.py
# Author: aevlin

HANDOFF_WORDS = ["address", "payment", "card"]


class SupportChatbot:
    """A mock chatbot that uses simple rules."""

    def __init__(self, name, instructions, order_tool, inventory_tool=None):
        # Save the chatbot's name.
        self.name = name

        # Save its instructions.
        self.instructions = instructions

        # Store the order lookup tool.
        self.order_tool = order_tool

        # Store the inventory lookup tool.
        self.inventory_tool = inventory_tool

        # Create an empty conversation history.
        self.history = []

    def respond(self, user_message):
        # Save the user's message.
        self.history.append({"role": "user", "content": user_message})

        # Decide how to respond.
        reply = self.choose_reply(user_message)

        # Save the chatbot's response.
        self.history.append({"role": "assistant", "content": reply})

        return reply

    def choose_reply(self, user_message):
        # Convert the message to lowercase.
        text = user_message.lower()

        # Check whether a human is needed.
        if self.needs_human(text):
            return "I can't help with that here. I'm passing you to a human agent."

        # Check for an order question.
        if "order" in text:
            return self.order_reply(user_message)

        # Check for an inventory question.
        if "stock" in text or "inventory" in text:
            return self.inventory_reply(user_message)

        # Respond to greetings.
        if "hello" in text:
            return f"Hello! I'm {self.name}. I can check an order status for you."

        # Handle unknown questions.
        return "I'm not sure how to help with that. I can check an order status."

    def needs_human(self, text):
        # Check for words requiring human help.
        for word in HANDOFF_WORDS:
            if word in text:
                return True

        return False

    def order_reply(self, user_message):
        # Find the order ID.
        order_id = self.order_tool.find_order_id(user_message)

        # Ask for an ID if none was found.
        if order_id is None:
            return "Which order? Please send an order ID like A100."

        # Find the order's status.
        status = self.order_tool.find_status(order_id)

        return f"Order {order_id} is {status}."

    def inventory_reply(self, user_message):
        """Check inventory and respond to the customer."""

        # Make sure an inventory tool is available.
        if self.inventory_tool is None:
            return "Inventory information is unavailable."

        # Search the message for a product.
        product = self.inventory_tool.find_product(user_message)

        # Ask for a product if none was found.
        if product is None:
            return "Which product? Please provide a product name."

        # Look up the quantity in stock.
        count = self.inventory_tool.count_for(product)

        # Return the inventory information.
        return f"We have {count} {product} in stock."

    def count_user_messages(self):
        # Start counting at zero.
        count = 0

        # Look through every message in the history.
        for message in self.history:
            # Only count messages sent by the user.
            if message["role"] == "user":
                count += 1

        # Return the total number of user messages.
        return count
