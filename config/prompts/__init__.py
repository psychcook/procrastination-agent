"""
System Prompt for Prokrastinations-Agent
=========================================
Manages loading the unified system prompt with state injection.
"""

from pathlib import Path

PROMPTS_DIR = Path(__file__).parent


def load_system_prompt() -> str:
    """Load the unified system prompt."""
    file_path = PROMPTS_DIR / "system.txt"
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().strip()


# Load prompt once at module import
SYSTEM_PROMPT = load_system_prompt()


def get_prompt(state: str, interaction_count: int = 0) -> str:
    """
    Get prompt with state and interaction count injected.

    Args:
        state: Current conversation state (intake, hypotheses, strategies, completion)
        interaction_count: Number of exchanges in strategies state

    Returns:
        Formatted system prompt string
    """
    return SYSTEM_PROMPT.format(
        current_state=state.upper(),
        interaction_count=interaction_count
    )
