# LangChain OpenAI Chat CLI

This is a simple command-line interface (CLI) for using LangChain with OpenAI's GPT models for conversational AI.

## Installation

1. Clone or download the repository.
2. Navigate to the directory containing the code.
3. Install the required dependencies using pip:
   
   ```
   pip install -r requirements.txt
   ```

## Configuration

Before using the CLI, you need to set up your OpenAI API key. You can obtain your API key from the OpenAI website.

1. Create a file named `.env` in the root directory of the project.
2. Add the following line to `.env`:

   ```
   OPENAI_API_KEY=<your_openai_api_key>
   ```

Replace `<your_openai_api_key>` with your actual OpenAI API key.

## Usage

Once you have set up your API key, you can run the CLI using the following command:

```
python main.py
```

The CLI will prompt you for input, and you can interact with the LangChain OpenAI model.

## Notes

- This CLI uses the LangChain library for interfacing with OpenAI's GPT models.
- Make sure you have an active internet connection to communicate with the OpenAI API.
- The default parameters for the model are:
  - Model: "gpt-3.5-turbo"
  - Temperature: 0.7

## Disclaimer

This CLI is provided as-is, and the use of the OpenAI API is subject to OpenAI's terms of service. Ensure compliance with their guidelines and policies when using the API.
