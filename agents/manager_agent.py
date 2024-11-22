class ManagerAgent:
    def __init__(self, pitch_agent, customer_agent, feedback_agent):
        # Ensure the agents are correctly passed and are objects with the expected methods
        if not hasattr(pitch_agent, 'generate_pitch'):
            raise ValueError("pitch_agent must have a 'generate_pitch' method")
        if not hasattr(customer_agent, 'simulate_response'):
            raise ValueError("customer_agent must have a 'simulate_response' method")
        if not hasattr(feedback_agent, 'analyze_response'):
            raise ValueError("feedback_agent must have an 'analyze_response' method")
        
        self.pitch_agent = pitch_agent
        self.customer_agent = customer_agent
        self.feedback_agent = feedback_agent

    def run(self, customer_profile):
        try:
            # Generate pitch
            pitch = self.pitch_agent.generate_pitch(customer_profile)
            print(f"Generated Pitch: {pitch}")  # Debugging print

            # Simulate customer response
            response = self.customer_agent.simulate_response()
            print(f"Simulated Response: {response}")  # Debugging print

            # Analyze feedback
            feedback = self.feedback_agent.analyze_response(response)
            print(f"Analyzed Feedback: {feedback}")  # Debugging print
            
            return {
                "pitch": pitch,
                "response": response,
                "feedback": feedback
            }
        
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
