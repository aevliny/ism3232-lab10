# tests/test_chatbot.py
# Author: aevlin

# Import the classes we want to test.
from chatbot import SupportChatbot
from inventory_tool import InventoryLookup
from order_tool import OrderLookup


def make_bot():
    """Create a fresh chatbot for each test."""
    orders = {"A100": "shipped", "A101": "processing"}
    return SupportChatbot("Sunny", "Be friendly.", OrderLookup(orders))


# Test 1: Check a known order.
def test_tool_finds_known_status():
    tool = OrderLookup({"A100": "shipped"})
    assert tool.find_status("A100") == "shipped"


# Test 2: Check an unknown order.
def test_tool_returns_none_for_unknown_order():
    tool = OrderLookup({"A100": "shipped"})
    assert tool.find_status("A999") is None


# Test 3: Check conversation history.
def test_respond_records_both_messages():
    bot = make_bot()
    bot.respond("hello")
    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"


# Test 4: Check an order question.
def test_order_question_uses_the_tool():
    bot = make_bot()
    assert bot.respond("Where is order A100?") == "Order A100 is shipped."


# Test 5: Check a missing order ID.
def test_order_question_without_an_id_asks_for_one():
    bot = make_bot()
    assert "order ID" in bot.respond("Where is my order?")


# Test 6: Check human assistance.
def test_address_change_goes_to_a_human():
    bot = make_bot()
    assert "human" in bot.respond("Please change my shipping address")


# Test 7: Check an unknown question.
def test_unknown_request_gets_a_safe_reply():
    bot = make_bot()
    assert "not sure" in bot.respond("What is the weather today?")


# Test 8: Check separate chatbot histories.
def test_two_chatbots_keep_separate_histories():
    first = make_bot()
    second = make_bot()
    first.respond("hello")
    assert len(first.history) == 2
    assert len(second.history) == 0


# Test 9: Count only the user's messages.
def test_count_user_messages():
    bot = make_bot()

    # Send two messages to the chatbot.
    bot.respond("hello")
    bot.respond("Where is order A100?")

    # Check that only user messages are counted.
    assert bot.count_user_messages() == 2


# Test 10: Check product inventory.
def test_inventory_question_uses_tool():
    # Create sample orders.
    orders = {"A100": "shipped"}

    # Create sample inventory.
    inventory = {"rain jackets": 12}

    # Create the order lookup tool.
    order_tool = OrderLookup(orders)

    # Create the inventory lookup tool.
    inventory_tool = InventoryLookup(inventory)

    # Create a chatbot with both tools.
    bot = SupportChatbot("Sunny", "Be friendly.", order_tool, inventory_tool)

    # Ask the chatbot about product inventory.
    reply = bot.respond("How many rain jackets are in stock?")

    # Verify that the chatbot gives the correct quantity.
    assert reply == "We have 12 rain jackets in stock."
