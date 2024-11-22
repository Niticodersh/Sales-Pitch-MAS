from transformers import pipeline

class FeedbackAgent:
    def __init__(self):
        # Instantiate the sentiment-analysis pipeline only once
        self.analyzer = pipeline("sentiment-analysis")

    def analyze_response(self, response):
        # Check if the 'comment' exists in the response
        if 'comment' not in response:
            raise ValueError("Response does not contain 'comment' key")

        # Get sentiment analysis
        sentiment = self.analyzer(response['comment'])[0]
        
        # Log sentiment analysis results for debugging
        print(f"Analyzed sentiment: {sentiment['label']} with confidence: {sentiment['score']}")
        
        return {"sentiment": sentiment['label'], "confidence": sentiment['score']}
