import nltk
from nltk.chat.util import Chat, reflections

# Define chat pairs for an enhanced shopping chatbot
pairs = [
    ["hi|hello|hey", ["Welcome to our online shopping assistant!", "Hi there!"]],
    ["how are you", ["I'm just a bot, but I'm here to assist you with your shopping needs."]],
    ["bye|goodbye", ["Thank you for using our shopping assistant. Goodbye!", "Have a great day!"]],
    ["help", ["I can help you with product recommendations, order tracking, and more. Just ask!"]],
    ["product recommendations", ["Sure, could you please specify the type of product you're looking for?"]],
    ["order tracking", ["To track your order, provide your order number and I'll get the details for you."]],
    ["shipping information", ["Our standard shipping takes 3-5 business days. Express shipping is available for faster delivery."]],
    ["return policy", ["You can return items within 30 days of purchase. Please check our website for detailed return instructions."]],
    ["payment methods", ["We accept credit cards, PayPal, and other major payment methods. Your payment information is secure with us."]],
    ["latest offers", ["Check our website for the latest offers and discounts. We frequently update our promotions!"]],
    ["laptop information", ["We offer a variety of laptops from top brands. Our laptops are known for high performance and durability. Feel free to specify your preferences for more personalized recommendations."]],
    # Add more pairs based on your chatbot's features and the problem statement
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start shopping chat
def shopping_chat():
    print("Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Shopping Assistant: Thank you for using our shopping assistant. Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Shopping Assistant:", response)

# Run the chat function
shopping_chat()
