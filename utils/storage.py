"""
Data storage utilities for questionnaire responses.
Handles saving and loading session data to/from JSON files.
"""

import json
import os
import stat
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional


# Data directory for storing JSON files
DATA_DIR = Path("data/responses")


def ensure_data_directory():
    """Ensures the data directory exists."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def get_session_file_path(session_id: str) -> Path:
    """
    Returns the file path for a session's data file.

    Args:
        session_id: UUID session identifier

    Returns:
        Path: Path to JSON file
    """
    ensure_data_directory()
    return DATA_DIR / f"{session_id}.json"


def load_session_data(session_id: str) -> Dict:
    """
    Loads session data from file, or creates new empty structure.

    Args:
        session_id: UUID session identifier

    Returns:
        dict: Session data structure
    """
    file_path = get_session_file_path(session_id)

    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # Create new session structure
        return {
            "session_id": session_id,
            "created_at": datetime.utcnow().isoformat() + "Z",
            "pre_questionnaire": None,
            "chat_completed_at": None,
            "post_questionnaire": None
        }


def save_session_data(session_id: str, data: Dict):
    """
    Saves session data to JSON file with secure permissions.

    Args:
        session_id: UUID session identifier
        data: Session data dictionary
    """
    ensure_data_directory()
    file_path = get_session_file_path(session_id)

    # Write file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # Set secure file permissions (owner read/write only: 0o600)
    # This prevents other users on the system from reading participant data
    try:
        os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR)  # 0o600
    except OSError:
        # On Windows or if permissions can't be set, continue anyway
        pass


def save_pre_questionnaire(session_id: str, answers: Dict[int, int]):
    """
    Saves pre-questionnaire answers.

    Args:
        session_id: UUID session identifier
        answers: Dictionary mapping question_id to answer value (1-7)
    """
    session_data = load_session_data(session_id)

    questionnaire_data = {
        "completed_at": datetime.utcnow().isoformat() + "Z",
        "answers": [
            {"question_id": q_id, "value": value}
            for q_id, value in sorted(answers.items())
        ]
    }

    session_data["pre_questionnaire"] = questionnaire_data
    save_session_data(session_id, session_data)


def save_post_questionnaire(session_id: str, answers: Dict[int, int]):
    """
    Saves post-questionnaire answers.

    Args:
        session_id: UUID session identifier
        answers: Dictionary mapping question_id to answer value (1-7)
    """
    session_data = load_session_data(session_id)

    questionnaire_data = {
        "completed_at": datetime.utcnow().isoformat() + "Z",
        "answers": [
            {"question_id": q_id, "value": value}
            for q_id, value in sorted(answers.items())
        ]
    }

    session_data["post_questionnaire"] = questionnaire_data
    save_session_data(session_id, session_data)


def mark_chat_complete(session_id: str):
    """
    Marks the chat as completed.

    Args:
        session_id: UUID session identifier
    """
    session_data = load_session_data(session_id)
    session_data["chat_completed_at"] = datetime.utcnow().isoformat() + "Z"
    save_session_data(session_id, session_data)


def get_session_status(session_id: str) -> Dict[str, bool]:
    """
    Returns the completion status of different session stages.

    Args:
        session_id: UUID session identifier

    Returns:
        dict: Status dictionary with boolean flags
    """
    session_data = load_session_data(session_id)

    return {
        "has_pre_questionnaire": session_data.get("pre_questionnaire") is not None,
        "has_chat_completion": session_data.get("chat_completed_at") is not None,
        "has_post_questionnaire": session_data.get("post_questionnaire") is not None,
    }


def list_all_sessions() -> List[str]:
    """
    Returns a list of all session IDs with data files.

    Returns:
        list: List of session ID strings
    """
    ensure_data_directory()
    session_files = DATA_DIR.glob("*.json")
    return [f.stem for f in session_files]  # stem = filename without extension


def get_all_session_data() -> List[Dict]:
    """
    Loads all session data files for analysis.

    Returns:
        list: List of session data dictionaries
    """
    sessions = []
    for session_id in list_all_sessions():
        sessions.append(load_session_data(session_id))
    return sessions
