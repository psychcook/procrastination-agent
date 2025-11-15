"""
Questionnaire questions configuration.
Defines all pre and post questionnaire questions with their scales.
"""

from typing import Dict, List


# Pre-Questionnaire: 7 questions (baseline measures)
PRE_QUESTIONNAIRE = [
    {
        "id": 1,
        "text": "Wie stark prokrastinierst du derzeit bei wichtigen Aufgaben?",
        "left_label": "Gar nicht",
        "right_label": "Sehr stark",
    },
    {
        "id": 2,
        "text": "Wie zuversichtlich bist du, dass du deine Aufgaben rechtzeitig erledigen kannst?",
        "left_label": "Gar nicht",
        "right_label": "Sehr zuversichtlich",
    },
    {
        "id": 3,
        "text": "Wie gut verstehst du die Gründe für deine Prokrastination?",
        "left_label": "Gar nicht",
        "right_label": "Sehr gut",
    },
    {
        "id": 4,
        "text": "Wie stark belastet dich deine Prokrastination emotional?",
        "left_label": "Gar nicht",
        "right_label": "Sehr stark",
    },
    {
        "id": 5,
        "text": "Wie hilfreich findest du bisherige Strategien gegen Prokrastination?",
        "left_label": "Gar nicht",
        "right_label": "Sehr hilfreich",
    },
    {
        "id": 6,
        "text": "Wie motiviert bist du, etwas gegen deine Prokrastination zu unternehmen?",
        "left_label": "Gar nicht",
        "right_label": "Sehr motiviert",
    },
    {
        "id": 7,
        "text": "Wie wahrscheinlich ist es, dass du neue Strategien auch wirklich ausprobierst?",
        "left_label": "Sehr unwahrscheinlich",
        "right_label": "Sehr wahrscheinlich",
    },
]


# Post-Questionnaire: 12 questions (7 repeated + 5 new evaluation questions)
POST_QUESTIONNAIRE = [
    # Repeated questions (1-7) - same as pre-questionnaire
    {
        "id": 1,
        "text": "Wie stark prokrastinierst du derzeit bei wichtigen Aufgaben?",
        "left_label": "Gar nicht",
        "right_label": "Sehr stark",
    },
    {
        "id": 2,
        "text": "Wie zuversichtlich bist du, dass du deine Aufgaben rechtzeitig erledigen kannst?",
        "left_label": "Gar nicht",
        "right_label": "Sehr zuversichtlich",
    },
    {
        "id": 3,
        "text": "Wie gut verstehst du die Gründe für deine Prokrastination?",
        "left_label": "Gar nicht",
        "right_label": "Sehr gut",
    },
    {
        "id": 4,
        "text": "Wie stark belastet dich deine Prokrastination emotional?",
        "left_label": "Gar nicht",
        "right_label": "Sehr stark",
    },
    {
        "id": 5,
        "text": "Wie hilfreich findest du bisherige Strategien gegen Prokrastination?",
        "left_label": "Gar nicht",
        "right_label": "Sehr hilfreich",
    },
    {
        "id": 6,
        "text": "Wie motiviert bist du, etwas gegen deine Prokrastination zu unternehmen?",
        "left_label": "Gar nicht",
        "right_label": "Sehr motiviert",
    },
    {
        "id": 7,
        "text": "Wie wahrscheinlich ist es, dass du neue Strategien auch wirklich ausprobierst?",
        "left_label": "Sehr unwahrscheinlich",
        "right_label": "Sehr wahrscheinlich",
    },
    # New evaluation questions (8-12)
    {
        "id": 8,
        "text": "Wie hilfreich fandest du das Gespräch mit dem Agent?",
        "left_label": "Gar nicht",
        "right_label": "Sehr hilfreich",
    },
    {
        "id": 9,
        "text": "Wie wahrscheinlich ist es, dass du die besprochenen Strategien umsetzt?",
        "left_label": "Sehr unwahrscheinlich",
        "right_label": "Sehr wahrscheinlich",
    },
    {
        "id": 10,
        "text": "Wie gut fühlst du dich vom Agent verstanden?",
        "left_label": "Gar nicht",
        "right_label": "Sehr gut",
    },
    {
        "id": 11,
        "text": "Wie würdest du die Benutzerfreundlichkeit des Tools bewerten?",
        "left_label": "Sehr schlecht",
        "right_label": "Sehr gut",
    },
    {
        "id": 12,
        "text": "Würdest du dieses Tool anderen Studierenden weiterempfehlen?",
        "left_label": "Auf keinen Fall",
        "right_label": "Auf jeden Fall",
    },
]


def get_pre_questionnaire() -> List[Dict]:
    """Returns the pre-questionnaire questions."""
    return PRE_QUESTIONNAIRE


def get_post_questionnaire() -> List[Dict]:
    """Returns the post-questionnaire questions."""
    return POST_QUESTIONNAIRE
