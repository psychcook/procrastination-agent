"""
System Prompts for Prokrastinations-Agent
==========================================
Manages loading and accessing system prompts for different conversation states.
"""

from pathlib import Path
from typing import Dict


PROMPTS_DIR = Path(__file__).parent


def load_prompts() -> Dict[str, str]:
    """
    Load all system prompts from text files.

    Returns:
        dict: Dictionary mapping state names to prompt content
    """
    prompts = {}

    prompt_files = {
        "intake": "intake.txt",
        "hypotheses": "hypotheses.txt",
        "strategies": "strategies.txt",
        "completion": "completion.txt"
    }

    for state, filename in prompt_files.items():
        file_path = PROMPTS_DIR / filename
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                prompts[state] = f.read().strip()
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Prompt file not found: {file_path}. "
                f"Ensure all prompt files exist in config/prompts/"
            )

    return prompts


# Load prompts once at module import
SYSTEM_PROMPTS = load_prompts()
