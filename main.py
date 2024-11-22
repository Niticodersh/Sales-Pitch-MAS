from flask import Flask, request, jsonify, render_template
from agents.pitch_agent import PitchAgent
from agents.customer_agent import CustomerAgent
from agents.feedback_agent import FeedbackAgent
from agents.manager_agent import ManagerAgent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')

# Initialize agents
pitch_agent = PitchAgent()
customer_agent = CustomerAgent()
feedback_agent = FeedbackAgent()
manager_agent = ManagerAgent(pitch_agent, customer_agent, feedback_agent)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_sales_pitch():
    customer_data = request.json
    if not customer_data or 'industry' not in customer_data or 'interest' not in customer_data:
        return jsonify({"error": "Missing required fields: 'industry' and 'interest'"}), 400
    
    response = manager_agent.run(customer_data)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
