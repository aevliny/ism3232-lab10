# Coastal Coffee Mini-Project

My mini-project is a rule-based customer service assistant for a fictional coffee shop called Coastal Coffee. It uses mock FAQ data to answer questions about business hours, location, Wi-Fi, menu items, and parking. The assistant uses a separate FAQ lookup tool and stores customer conversations in a history list. Requests involving refunds or payments are directed to a human employee because they may involve sensitive information. If this assistant used real customer data, privacy, data security, and incorrect responses would be important risks to consider. The assistant should not collect or expose private customer information.

## AI Assistance Disclosure

I used ChatGPT to help develop and understand the Python code for this lab, including the object-oriented classes, chatbot methods, FAQ lookup tool, and automated tests. I reviewed and tested the code in VS Code. The classes demonstrate object-oriented programming concepts such as constructors, instance attributes, methods, and composition. Comments in the Python files explain the purpose of the code. I used pytest to verify the chatbot behavior and Ruff to check code quality.

## AI-Generated Code Explanation

I used ChatGPT to help create the classes for my Coastal Coffee mini-project.

**FAQLookup class (`my_tool.py`):**
- `class FAQLookup` defines the FAQ lookup tool.
- `__init__` initializes the object with a dictionary of FAQs.
- `self.faqs = faqs` stores the FAQ information.
- `find_answer` accepts a customer's question.
- `question.lower()` makes the search case-insensitive.
- The `for` loop searches each FAQ keyword.
- The `if` statement checks for a matching keyword.
- `return answer` returns the matching response.
- `return None` handles questions without a match.

**CoffeeAssistant class (`my_assistant.py`):**
- `class CoffeeAssistant` defines the customer service assistant.
- `__init__` initializes the assistant's name and FAQ tool.
- `self.name` stores the assistant's name.
- `self.faq_tool` connects the assistant to the lookup tool.
- `self.history` creates a conversation history.
- `respond` receives customer messages and records them.
- `choose_reply` selects an appropriate response.
- Refund and payment requests are referred to a human.
- The FAQ tool answers known questions.
- Unknown questions receive a safe fallback response.

This project demonstrates classes, objects, instance attributes, methods, and composition.