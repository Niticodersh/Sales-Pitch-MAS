import os
from transformers import pipeline

class PitchAgent:
    def __init__(self):
        # Get Hugging Face token from environment variable
        auth_token = os.getenv('HF_AUTH_TOKEN')
        if not auth_token:
            raise ValueError("Authentication token not found. Please set the HF_AUTH_TOKEN environment variable.")
        
        # Initialize the model pipeline using the token
        self.generator = pipeline("text-generation", model="openai-community/gpt2")

    def generate_pitch(self, customer_profile):
        # Ensure that the profile contains required information
        if not all(key in customer_profile for key in ['industry', 'interest']):
            raise ValueError("Customer profile must contain 'industry' and 'interest' keys.")

        # Prepare the prompt for the model
        pitch_prompt = f"Create a professional sales pitch for a client in the {customer_profile['industry']} industry, who is interested in {customer_profile['interest']} solutions."
        
        # Generate the pitch
        try:
            generated_text = self.generator(pitch_prompt, max_length=512, num_return_sequences=1)[0]['generated_text']
            print(generated_text)
            lines = generated_text.split('.')
            remaining_lines = [line.strip() for line in lines[1:] if line.strip()]
        
            # Join the remaining lines back into a single string, adding periods
            generated_text = '. '.join(remaining_lines) 
            pitch = generated_text.strip()
            print("pitch",pitch)
            return pitch
        except Exception as e:
            print(f"Error generating pitch: {str(e)}")
            return None
