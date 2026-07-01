# AI Integration 101 - ChatGPT Wrapper

A simple AI chat system with a Python wrapper for OpenAI's ChatGPT API featuring **real-time streaming responses**.

## Features

✨ **Streaming Support** - Get responses in real-time as they're generated  
🔧 **Simple API** - Easy-to-use wrapper class  
⚙️ **Flexible Configuration** - Customizable model selection  
📝 **Interactive Chat** - Example chat application included  

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SamSegz/AI-integration-101.git
   cd AI-integration-101
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```
   
   Or set as environment variable:
   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```

## Usage

### Basic Streaming Usage

```python
from chatgpt_wrapper import ChatGPTWrapper

# Initialize
wrapper = ChatGPTWrapper()

# Stream response
user_message = "Hello, how are you?"
for chunk in wrapper.stream_response(user_message):
    print(chunk, end="", flush=True)
```

### Get Complete Response

```python
# Get the full response at once
response = wrapper.get_response("What is Python?")
print(response)
```

### With Custom System Prompt

```python
system_prompt = "You are a helpful Python programming assistant."
for chunk in wrapper.stream_response("Explain decorators", system_prompt):
    print(chunk, end="", flush=True)
```

### Interactive Chat Application

Run the example chat application:

```bash
python example_chat_app.py
```

This starts an interactive chat session where you can type messages and receive streamed responses.

## API Reference

### ChatGPTWrapper Class

#### `__init__(api_key=None, model="gpt-3.5-turbo")`

Initialize the wrapper.

**Parameters:**
- `api_key` (str, optional): OpenAI API key. If not provided, reads from `OPENAI_API_KEY` environment variable.
- `model` (str): Model to use. Defaults to `gpt-3.5-turbo`.

#### `stream_response(user_input, system_prompt=None)`

Send a message and stream the response.

**Parameters:**
- `user_input` (str): The user's message/question.
- `system_prompt` (str, optional): System prompt to guide the model's behavior.

**Returns:**
- Generator yielding response chunks as strings.

**Example:**
```python
for chunk in wrapper.stream_response("Hello!"):
    print(chunk, end="", flush=True)
```

#### `get_response(user_input, system_prompt=None)`

Send a message and get the complete response.

**Parameters:**
- `user_input` (str): The user's message/question.
- `system_prompt` (str, optional): System prompt to guide the model's behavior.

**Returns:**
- str: The complete response from ChatGPT.

**Example:**
```python
response = wrapper.get_response("Hello!")
print(response)
```

## Files

- `chatgpt_wrapper.py` - Main wrapper class implementation
- `example_chat_app.py` - Interactive chat application example
- `requirements.txt` - Python dependencies
- `.env.example` - Environment variable template
- `README.md` - This file

## Getting Your API Key

1. Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Create a new secret key
3. Add it to your `.env` file or set it as an environment variable

## Requirements

- Python 3.8+
- OpenAI API key
- `openai>=1.0.0`
- `python-dotenv>=1.0.0`

## License

This project is open source. Feel free to use and modify.

## Notes

- The streaming feature provides a better user experience for long responses
- Make sure you have sufficient API credits with OpenAI
- Response times depend on model complexity and current API load
- The default model is `gpt-3.5-turbo`, but you can change it to `gpt-4` or other available models
