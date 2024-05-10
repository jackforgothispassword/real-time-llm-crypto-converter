# Real-Time LLM Crypto Price Converter

### Powered by CoinMarketCap API, LangChain, and GPT-3.5-turbo

## This script integrates a cryptocurrency conversion function into a LangChain-based conversational AI model. Here's a breakdown of the script's workflow:

### Environment Setup:
The script initializes by importing necessary libraries and setting up the environment.

### Tool Definition:
A crypto_converter tool is defined using a decorator. This tool handles the conversion of one cryptocurrency to another by fetching real-time conversion rates from the CoinMarketCap API.

### LangChain Model Configuration:
The tool is bound to a LangChain conversational AI model (ChatOpenAI), which allows the model to invoke this tool as part of its responses to queries.

### Query Processing:
The script processes a predefined query about cryptocurrency conversion.

### Tool Invocation:
The LangChain model invokes the crypto_converter tool based on the query, and the script processes the output, displaying the conversion result.
