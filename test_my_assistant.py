from my_assistant import CoffeeAssistant
from my_tool import FAQLookup


def make_assistant():
    faqs = {
        "hours": "We are open from 7 AM to 6 PM.",
        "wifi": "We offer free Wi-Fi.",
    }
    tool = FAQLookup(faqs)
    return CoffeeAssistant("Test Bot", tool)


def test_known_question():
    bot = make_assistant()
    assert bot.respond("What are your hours?") == ("We are open from 7 AM to 6 PM.")


def test_unknown_question():
    bot = make_assistant()
    assert "don't have that information" in bot.respond("Do you sell bicycles?")


def test_human_handoff():
    bot = make_assistant()
    assert "human employee" in bot.respond("I need a refund")


def test_conversation_history():
    bot = make_assistant()
    bot.respond("Do you have wifi?")
    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"
