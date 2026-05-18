from anthropic import Anthropic
from dotenv import load_dotenv
import json
import os

load_dotenv()

client = Anthropic()

def save_game_design(title: str, content: str) -> str:
    filename = f"{title.lower().replace(' ', '_')}_design.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"Design document saved as {filename}"

tools = [
    {
        "name": "save_game_design",
        "description": "Save the completed game design document to a file. Call this when you have a complete game design ready.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "The game title, used for the filename"
                },
                "content": {
                    "type": "string", 
                    "description": "The full game design document in markdown format"
                }
            },
            "required": ["title", "content"]
        }
    }
]

system_prompt = """You are a senior game designer. When a user describes a game idea, you will:
1. Ask ONE clarifying question if needed
2. Create a concise game design document covering: concept, core mechanic, win/lose condition, and art style
3. Save it using the save_game_design tool without being asked

You decide when the design is complete enough to save. Don't wait for permission."""

conversation_history = []

print("Game Designer Agent ready. Describe your game idea:\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        break

    conversation_history.append({"role": "user", "content": user_input})

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=2048,
            system=system_prompt,
            tools=tools,
            messages=conversation_history
        )

        conversation_history.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    print(f"\n[Agent action: {block.name}]")
                    if block.name == "save_game_design":
                        result = save_game_design(**block.input)
                        print(f"[{result}]")
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result
                        })
                else:
                    if hasattr(block, 'text'):
                        print(f"\nDesigner: {block.text}")

            conversation_history.append({"role": "user", "content": tool_results})

        else:
            for block in response.content:
                if hasattr(block, 'text'):
                    print(f"\nDesigner: {block.text}\n")
            break