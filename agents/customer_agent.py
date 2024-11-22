from random import choice
import logging

class CustomerAgent:
    def __init__(self):
        self.responses = [
            {"sentiment": "positive", "comment": "I love this idea!"},
            {"sentiment": "neutral", "comment": "Sounds okay, tell me more."},
            {"sentiment": "negative", "comment": "Not interested."}
        ]
        # Set up logging for this agent
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    def simulate_response(self):
        response = choice(self.responses)
        # Log the simulated response
        self.logger.info(f"Simulated customer response: {response}")
        return response
