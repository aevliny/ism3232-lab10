# Exercise 1 — Label the Parts

**ISM3232 — Week 10 Lab**

### 1. What are the two classes?

The two classes are `OrderLookup` and `SupportChatbot`.

`OrderLookup` is responsible for finding order IDs and checking order statuses. `SupportChatbot` is responsible for responding to users and managing conversations.

### 2. What are the two objects created in main.py?

The two objects are `order_tool` and `bot`.

`order_tool` is an instance of the `OrderLookup` class. `bot` is an instance of the `SupportChatbot` class.

### 3. What are the four attributes of SupportChatbot?

The four attributes are:

- `self.name` — Stores the chatbot's name.
- `self.instructions` — Stores instructions for the chatbot.
- `self.order_tool` — Stores the order lookup tool.
- `self.history` — Stores the conversation history.

### 4. What are the three methods in OrderLookup?

The three methods are:

- `__init__()` — Initializes the object and stores the orders.
- `find_order_id()` — Searches a message for a known order ID.
- `find_status()` — Finds the status of an order.

### 5. Which line demonstrates composition?

The line is:

`self.order_tool = order_tool`

This demonstrates composition because the `SupportChatbot` object contains and uses an `OrderLookup` object to perform order searches.

### 6. In bot.respond("hello"), what does self refer to?

`self` refers to the `bot` object, which is an instance of the `SupportChatbot` class.

It allows the method to access that particular chatbot's attributes and methods.