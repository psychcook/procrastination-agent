"""
Questionnaire questions configuration.
Defines all pre and post questionnaire questions with their scales.

Research Design:
- Pre-questionnaire: 4 questions (1-5 scale) - Baseline evaluation
- Post-questionnaire: 11 questions (mixed scales) - Post-intervention + quality control
  - Questions 1-5: Evaluation (1-5 scale, first 4 repeated from pre)
  - Questions 6-7: Bot Usability Scale / BUS-11 (1-5 scale)
  - Questions 8-9: Tui manual (1-7 scale)
  - Questions 10-11: Digital Working Alliance Inventory / D-WAI (1-7 scale)
"""

from typing import Dict, List


# =============================================================================
# PRE-QUESTIONNAIRE (Evaluation Vorher)
# =============================================================================
# 4 questions, all with 1-5 Likert scale
# Scale: 1 = "Ich stimme nicht zu", 5 = "Ich stimme zu"

PRE_QUESTIONNAIRE = [
    {
        "id": 1,
        "text": "Mir ist klar, warum ich die Aufgabe aufschiebe.",
        "left_label": "Ich stimme nicht zu",
        "right_label": "Ich stimme zu",
        "scale_max": 5,
    },
    {
        "id": 2,
        "text": "Ich weiss genau, was mein nächster Schritt ist, um die aufgeschobene Aufgabe anzugehen.",
        "left_label": "Ich stimme nicht zu",
        "right_label": "Ich stimme zu",
        "scale_max": 5,
    },
    {
        "id": 3,
        "text": "Ich bin zuversichtlich, die Aufgabe angehen zu können.",
        "left_label": "Ich stimme nicht zu",
        "right_label": "Ich stimme zu",
        "scale_max": 5,
    },
    {
        "id": 4,
        "text": "Ich fühle mich überfordert mit der Aufgabe.",
        "left_label": "Ich stimme nicht zu",
        "right_label": "Ich stimme zu",
        "scale_max": 5,
    },
]


# =============================================================================
# POST-QUESTIONNAIRE (Evaluation Nachher + Qualitätskontrolle)
# =============================================================================
# 11 questions total with mixed scales

POST_QUESTIONNAIRE = [
    # -------------------------------------------------------------------------
    # TEIL 1: Evaluation Nachher (Questions 1-5)
    # -------------------------------------------------------------------------
    # First 4 questions repeated from pre-questionnaire for comparison
    # Question 5 is new
    # All use 1-5 scale

    {
        "id": 1,
        "text": "Mir ist klar, warum ich die Aufgabe aufschiebe.",
        "left_label": "Ich stimme nicht zu",
        "right_label": "Ich stimme zu",
        "scale_max": 5,
    },
    {
        "id": 2,
        "text": "Ich weiss genau, was mein nächster Schritt ist, um die aufgeschobene Aufgabe anzugehen.",
        "left_label": "Ich stimme nicht zu",
        "right_label": "Ich stimme zu",
        "scale_max": 5,
    },
    {
        "id": 3,
        "text": "Ich bin zuversichtlich, die Aufgabe angehen zu können.",
        "left_label": "Ich stimme nicht zu",
        "right_label": "Ich stimme zu",
        "scale_max": 5,
    },
    {
        "id": 4,
        "text": "Ich fühle mich überfordert mit der Aufgabe.",
        "left_label": "Ich stimme nicht zu",
        "right_label": "Ich stimme zu",
        "scale_max": 5,
    },
    {
        "id": 5,
        "text": "Ich habe eine Strategie gefunden, die zu meiner Situation passt.",
        "left_label": "Ich stimme nicht zu",
        "right_label": "Ich stimme zu",
        "scale_max": 5,
    },

    # -------------------------------------------------------------------------
    # TEIL 2: Qualitätskontrolle
    # -------------------------------------------------------------------------

    # Bot Usability Scale (BUS-11) - 2 items
    # Scale: 1 = "Stimme überhaupt nicht zu", 5 = "Stimme voll zu"

    {
        "id": 6,
        "text": "Die Kommunikation mit dem Chatbot war klar.",
        "left_label": "Stimme überhaupt nicht zu",
        "right_label": "Stimme voll zu",
        "scale_max": 5,
    },
    {
        "id": 7,
        "text": "Ich habe den Eindruck, dass der Chatbot versteht, was ich will, und mir hilft, mein Ziel zu erreichen.",
        "left_label": "Stimme überhaupt nicht zu",
        "right_label": "Stimme voll zu",
        "scale_max": 5,
    },

    # Tui manual - 2 items
    # Scale: 1 = "Trifft nicht zu", 7 = "Trifft zu"

    {
        "id": 8,
        "text": "Wie wahrscheinlich ist es, dass du diesen Chatbot einer anderen Person empfehlen würdest?",
        "left_label": "Trifft nicht zu",
        "right_label": "Trifft zu",
        "scale_max": 7,
    },
    {
        "id": 9,
        "text": "Ich würde den Agenten wieder nutzen.",
        "left_label": "Trifft nicht zu",
        "right_label": "Trifft zu",
        "scale_max": 7,
    },

    # Digital Working Alliance Inventory (D-WAI) - 2 items
    # Scale: 1 = "Stimme überhaupt nicht zu", 7 = "Stimme völlig zu"

    {
        "id": 10,
        "text": "Der Chatbot motiviert mich, Aufgaben umzusetzen und Fortschritte zu machen.",
        "left_label": "Stimme überhaupt nicht zu",
        "right_label": "Stimme völlig zu",
        "scale_max": 7,
    },
    {
        "id": 11,
        "text": "Ich finde, dass die Empfehlungen des Chatbots für meine Ziele wichtig sind.",
        "left_label": "Stimme überhaupt nicht zu",
        "right_label": "Stimme völlig zu",
        "scale_max": 7,
    },
]


def get_pre_questionnaire() -> List[Dict]:
    """Returns the pre-questionnaire questions."""
    return PRE_QUESTIONNAIRE


def get_post_questionnaire() -> List[Dict]:
    """Returns the post-questionnaire questions."""
    return POST_QUESTIONNAIRE
