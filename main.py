import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage


def main():
    load_dotenv()

    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("Please set OPENAI_API_KEY in.env")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    # Main default model parameters
    #       model = "gpt-3.5-turbo"
    #       temperature = 0.7

    chat = ChatOpenAI()

    messages = [
        SystemMessage(content="Your are a helpful assistant!"),
    ]
    print("I am ChatGPT CLI!")


if __name__ == "__main__":
    main()
