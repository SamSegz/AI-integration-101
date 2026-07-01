"""
ChatGPT Streaming Wrapper
A simple wrapper that relays user input to ChatGPT API and streams the response.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

class ChatGPTWrapper:
    """
    A wrapper class for interacting with OpenAI's ChatGPT API with streaming support.
    """
    
    def __init__(self, api_key=None, model="gpt-3.5-turbo"):
        """
        Initialize the ChatGPT wrapper.
        
        Args:
            api_key (str, optional): OpenAI API key. If not provided, reads from OPENAI_API_KEY env var.
            model (str): Model to use. Defaults to gpt-3.5-turbo.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found. Please set it as an environment variable or pass it as an argument.")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
    
    def stream_response(self, user_input, system_prompt=None):
        """
        Send a message to ChatGPT and stream the response.
        
        Args:
            user_input (str): The user's message/question.
            system_prompt (str, optional): System prompt to guide the model's behavior.
        
        Yields:
            str: Chunks of the response as they are received.
        """
        messages = []
        
        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })
        
        messages.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            with self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                stream=True
            ) as stream:
                for text in stream.text_stream:
                    yield text
        except Exception as e:
            raise Exception(f"Error communicating with OpenAI API: {str(e)}")
    
    def get_response(self, user_input, system_prompt=None):
        """
        Send a message to ChatGPT and return the complete response.
        
        Args:
            user_input (str): The user's message/question.
            system_prompt (str, optional): System prompt to guide the model's behavior.
        
        Returns:
            str: The complete response from ChatGPT.
        """
        complete_response = ""
        for chunk in self.stream_response(user_input, system_prompt):
            complete_response += chunk
        return complete_response


# Example usage
if __name__ == "__main__":
    # Initialize the wrapper
    wrapper = ChatGPTWrapper()
    
    # Get user input
    user_message = input("Enter your message: ")
    
    print("\n--- ChatGPT Response (Streaming) ---\n")
    
    # Stream the response
    for chunk in wrapper.stream_response(user_message):
        print(chunk, end="", flush=True)
    
    print("\n")
