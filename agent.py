from anthropic import Anthropic
from dotenv import load_dotenv
import json

load_dotenv()

client = Anthropic()

def save_game_design(title: str, content: str) -> str:
    filename = f"{title.lower().replace(' ', '_')}_design.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"Design document saved as {filename}"

def search_similar_games(genre: str, mechanics: str) -> str:
    similar = {
        "management": ["Prison Architect", "RimWorld", "Dwarf Fortress"],
        "platformer": ["Celeste", "Hollow Knight", "Dead Cells"],
        "puzzle": ["Portal", "The Witness", "Baba Is You"],
        "rpg": ["Undertale", "Stardew Valley", "Disco Elysium"],
        "strategy": ["Into the Breach", "FTL", "Slay the Spire"],
    }
    genre_lower = genre.lower()
    matches = []
    for key, games in similar.items():
        if key in genre_lower or key in mechanics.lower():
            matches.extend(games)
    if not matches:
        matches = ["Celeste", "Stardew Valley", "Into the Breach"]
    return f"Similar successful indie games in this space: {', '.join(matches[:3])}. Study these for scope and mechanics reference."

def estimate_dev_time(features: list, team_size: int) -> str:
    base_weeks = len(features) * 2
    adjusted = base_weeks / max(team_size, 1)
    solo_note = " Note: as a solo dev, budget 3x this estimate for polish and bugs." if team_size == 1 else ""
    return f"Estimated development time: {adjusted:.0f}-{adjusted*1.5:.0f} weeks for core prototype.{solo_note}"

tools = [
    {
        "name": "save_game_design",
        "description": "Save the completed game design document to a file. Only call this when the full design is ready.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "Game title for the filename"},
                "content": {"type": "string", "description": "Full game design document in markdown"}
            },
            "required": ["title", "content"]
        }
    },
    {
        "name": "search_similar_games",
        "description": "Search for similar existing games to use as reference for scope and mechanics. Call this early to ground the design in reality.",
        "input_schema": {
            "type": "object",
            "properties": {
                "genre": {"type": "string", "description": "The game genre"},
                "mechanics": {"type": "string", "description": "Core mechanics of the game"}
            },
            "required": ["genre", "mechanics"]
        }
    },
    {
        "name": "estimate_dev_time",
        "description": "Estimate development time based on planned features and team size. Call this before finalizing the design to ensure scope is realistic.",
        "input_schema": {
            "type": "object",
            "properties": {
                "features": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of planned game features"
                },
                "team_size": {"type": "integer", "description": "Number of developers (use 1 for solo)"}
            },
            "required": ["features", "team_size"]
        }
    }
]

system_prompt = """You are a senior game designer. When given a game idea:
1. Search for similar games first to ground your design in reality
2. Draft the core design concept
3. Estimate development time based on planned features
4. Adjust scope if the estimate is too long for a solo developer
5. Save the final design document

Use your tools in whatever order makes sense. Be practical about scope — this is a solo indie project."""

conversation_history = []

print("Game Designer Agent (Module 2) — Multi-tool edition")
print("Describe your game idea:\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    conversation_history.append({"role": "user", "content": user_input})

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4096,
            system=system_prompt,
            tools=tools,
            messages=conversation_history
        )

        conversation_history.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    print(f"\n[Agent using tool: {block.name}]")
                    print(f"[Input: {json.dumps(block.input, indent=2)}]")

                    if block.name == "save_game_design":
                        result = save_game_design(**block.input)
                    elif block.name == "search_similar_games":
                        result = search_similar_games(**block.input)
                    elif block.name == "estimate_dev_time":
                        result = estimate_dev_time(**block.input)
                    else:
                        result = "Unknown tool"

                    print(f"[Result: {result}]\n")
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })
                else:
                    if hasattr(block, 'text') and block.text:
                        print(f"\nDesigner: {block.text}")

            conversation_history.append({"role": "user", "content": tool_results})

        else:
            for block in response.content:
                if hasattr(block, 'text') and block.text:
                    print(f"\nDesigner: {block.text}\n")
            break