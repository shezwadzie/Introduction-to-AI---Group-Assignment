AI Introduction Assignment
Description
Week 1 Assignment: Build a Cryptocurrency Advisor Chatbot
Theme: "Your First AI-Powered Financial Sidekick!" 🌟
Objective

Create a rule-based chatbot that analyzes cryptocurrency data and provides investment advice based on profitability (e.g., price trends) and sustainability (e.g., energy efficiency, project viability).

What You’ll Learn

✅ Basics of AI-driven decision-making.
✅ How to design conversational logic.
✅ Simple data analysis for crypto trends.

Tools & Resources

Language: Python .

Libraries: Use if-else logic or ChatterBot (optional) for conversation flow.

Data: Predefined crypto datasets (provided below).

Platform: Code in Google Colab, Jupyter Notebook, or any IDE.

Step-by-Step Guide
1. Design the Chatbot’s Personality

Name your bot (e.g., CryptoBuddy).

Define its tone: Friendly, professional, or meme-loving? (e.g., “Hey there! Let’s find you a green and growing crypto!”).

2. Predefined Crypto Data

Use this sample dataset (or create your own):

python

crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
} 


 3. Chatbot Logic

User Inputs: Ask questions like:

“Which crypto is trending up?”

“What’s the most sustainable coin?”

Bot Responses:

Use if-else logic to match queries to data.

Example:

python
if "sustainable" in user_query:  
    recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])  
    print(f"Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")


4. Add Advice Rules

Profitability: Prioritize coins with price_trend = "rising" and market_cap = "high".

Sustainability: Prioritize coins with energy_use = "low" and sustainability_score > 7/10.

5. Test Your Bot

Sample conversation:


You: Which crypto should I buy for long-term growth?  
CryptoBuddy: Cardano (ADA) is trending up and has a top-tier sustainability score! 🚀 

Stretch Goals 

API Integration: Pull real-time data using CoinGecko’s free API.

NLP: Use NLTK to handle more natural language queries.

Ethics Alert: Add a disclaimer like “Crypto is risky—always do your own research!”