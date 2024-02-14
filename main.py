import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage


def main():
    load_dotenv()

    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("Please set OPENAI_API_KEY in .env")
        exit(1)
    else:
        print("API Key is set")

    # Main default model parameters
    #       model = "gpt-3.5-turbo"
    #       temperature = 0.7

    chat = ChatOpenAI()

    messages = [
        SystemMessage(content="Your are a helpful assistant!"),
    ]
    print("I am ChatGPT CLI!")

    # Infinite loop
    while True:
        # Get user input
        user_input = input(">> ")

        messages.append(HumanMessage(content=user_input))

        # Generate response
        ai_response = chat.invoke(messages)

        messages.append(AIMessage(content=ai_response.content))

        print("\nAssistant says:\n", ai_response.content)


if __name__ == "__main__":
    main()
