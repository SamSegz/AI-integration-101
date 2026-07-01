"""
Example Chat Application
Demonstrates how to use the ChatGPT wrapper in a simple chat application.
"""

from chatgpt_wrapper import ChatGPTWrapper


def main():
    """Run an interactive chat session with ChatGPT."""
    
    # Initialize the wrapper
    try:
        wrapper = ChatGPTWrapper()
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    print("=" * 50)
    print("ChatGPT Interactive Chat")
    print("=" * 50)
    print("Type 'exit' to quit\n")
    
    # Optional system prompt to guide the model
    system_prompt = "You are a helpful assistant."
    
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            print("\nAssistant: ", end="", flush=True)
            
            # Stream the response
            for chunk in wrapper.stream_response(user_input, system_prompt):
                print(chunk, end="", flush=True)
            
            print("\n")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            continue


if __name__ == "__main__":
    main()
