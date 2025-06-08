crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 0.3  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 0.6  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 0.8  
    }  
}

print("Hello! I’m CryptoBuddy, your friendly crypto sidekick! Ask me anything about crypto trends or sustainability.")

while True:
    user_query = input("\nYou: ").lower()

    if "exit" in user_query or "bye" in user_query:
        print("CryptoBuddy: Stay safe and remember—crypto is risky! Do your own research before investing.")
        break

    elif "trending" in user_query or "price" in user_query:
        trending_cryptos = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        if trending_cryptos:
            print(f"CryptoBuddy: These coins are trending up: {', '.join(trending_cryptos)}")
        else:
            print("CryptoBuddy: No coins are trending up right now.")

    elif "sustainable" in user_query or "eco" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy: Invest in {recommend}! It's eco-friendly and has long-term potential.")

    elif "profitable" in user_query or "growth" in user_query:
        profitable = [
            coin for coin, data in crypto_db.items() 
            if data["price_trend"] == "rising" and data["market_cap"] == "high"
        ]
        if profitable:
            print(f"CryptoBuddy: For profitability, consider: {', '.join(profitable)}")
        else:
            print("CryptoBuddy: No high market cap coins are trending right now.")

    elif "energy" in user_query or "efficient" in user_query:
        efficient = [
            coin for coin, data in crypto_db.items()
            if data["energy_use"] == "low"
        ]
        if efficient:
            print(f"CryptoBuddy: Energy-efficient cryptos: {', '.join(efficient)}")
        else:
            print("CryptoBuddy: No energy-efficient coins found.")

    else:
        print("CryptoBuddy: Sorry, I didn’t catch that. Try asking about trending, sustainable, or profitable coins!")
