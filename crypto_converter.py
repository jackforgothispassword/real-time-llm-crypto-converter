import requests
import os
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
import json 

@tool
def crypto_converter(args):
    """Converts amount from one cryptocurrency to another"""
    print(f"Received args: {args}")  # Debug: Print arguments received
    from_symbol = args.get("from")  # Adjusted key names to match received args
    to_symbol = args.get("to")
    amount = args.get("amount")
    
    if not from_symbol or not to_symbol or not amount:
        return "Invalid arguments provided. Please specify from_symbol, to_symbol, and amount."

    api_key = os.getenv('COINMARKETCAP_API_KEY')  # Ensure this environment variable is set
    url = "https://pro-api.coinmarketcap.com/v1/tools/price-conversion"
    parameters = {
        'amount': amount,
        'symbol': from_symbol,
        'convert': to_symbol
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }
    
    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()
    if 'data' in data and 'quote' in data['data'] and to_symbol in data['data']['quote']:
        price = data['data']['quote'][to_symbol]['price']
        return f"{amount} {from_symbol} is equivalent to {price} {to_symbol}."
    return "Conversion data not available"

# Setup LangChain LLM with the crypto_converter tool
tools = [crypto_converter]
llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
llm_with_tools = llm.bind_tools(tools)

# Example query for cryptocurrency conversion
query = "How much is 1 BTC in ETH?"
messages = [query]
ai_msg = llm_with_tools.invoke(messages)

# Process the tool calls
for tool_call in ai_msg.tool_calls:
    selected_tool = {"crypto_converter": crypto_converter}[tool_call["name"].lower()]
    tool_output = selected_tool.invoke(tool_call["args"])
    print(tool_output)
