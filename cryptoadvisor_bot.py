# CryptoAdvisor Bot - Your First AI Financial Sidekick! 🌟

def greet_user():
    print("👋 Hi, I’m CryptoAdvisor, your friendly crypto sidekick!")
    print("Ask me about profitable or sustainable coins. 💰🌱\n")

# Sample crypto data
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

# Chatbot logic
def handle_query(user_query):
    query = user_query.lower()

    if "sustainable" in query:
        best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"🌱 {best} is the most sustainable crypto with a score of {crypto_db[best]['sustainability_score']}/10!")

    elif "trending" in query or "rising" in query:
        trending = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        print("📈 Trending cryptos:")
        for coin in trending:
            print(f"- {coin}")

    elif "long-term" in query or "invest" in query:
        best = None
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 6:
                best = coin
        if best:
            print(f"🚀 Try {best}! It’s rising and has a good sustainability score.")
        else:
            print("⚠️ No coins meet long-term investment criteria.")

    else:
        print("❓ I didn’t understand. Ask about trending coins, sustainability, or investment tips.")

# Run chatbot loop
def run_chatbot():
    greet_user()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("👋 Goodbye! Crypto is risky—always do your own research!")
            break
        handle_query(user_input)

run_chatbot()
