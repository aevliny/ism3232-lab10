# my_tool.py
# Mini-Project: Coastal Coffee Assistant


class FAQLookup:
    """A tool that looks up common customer questions."""

    def __init__(self, faqs):
        # Store the FAQ dictionary.
        self.faqs = faqs

    def find_answer(self, question):
        """Find an answer to a customer question."""

        # Convert the question to lowercase.
        question = question.lower()

        # Search for matching FAQ keywords.
        for keyword, answer in self.faqs.items():
            if keyword.lower() in question:
                return answer

        # Return None if no answer is found.
        return None
