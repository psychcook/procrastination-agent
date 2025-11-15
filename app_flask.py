"""
Prokrastinations-Interventions-Agent - Flask Version
====================================================
Complete migration from Streamlit to Flask with full backend integration.

Authors: Yves, Nathalie, Eileen & Jara
Tech Stack: Flask, Anthropic Claude API, Python 3.11
"""

import os
import re
import uuid
import json
import logging
from datetime import datetime
from pathlib import Path

from flask import Flask, render_template, request, session, redirect, url_for, jsonify, Response
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
from dotenv import load_dotenv
import anthropic
import bleach

# Import existing utilities (they work with Flask too!)
from config.questions import get_pre_questionnaire, get_post_questionnaire
from config.prompts import SYSTEM_PROMPTS
from config.security import (
    get_security_config, RATE_LIMITS, CSP, FORCE_HTTPS,
    MAX_CHAT_MESSAGE_LENGTH, MIN_CHAT_MESSAGE_LENGTH,
    VALID_SCALE_VALUES, PRE_QUESTIONNAIRE_COUNT, POST_QUESTIONNAIRE_COUNT,
    MAX_MESSAGES_PER_SESSION, GENERIC_API_ERROR_MESSAGE
)
from utils.storage import (
    save_pre_questionnaire,
    save_post_questionnaire,
    mark_chat_complete,
    get_session_status
)

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Apply security configuration
security_config = get_security_config()
app.config.update(security_config)

# Ensure SECRET_KEY is set in production
if not app.config.get('SECRET_KEY') and os.getenv('FLASK_ENV') == 'production':
    raise ValueError("SECRET_KEY environment variable MUST be set for production!")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Anthropic client
try:
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
except Exception as e:
    print(f"ERROR: Failed to initialize Anthropic client: {e}")
    client = None

# Initialize security extensions
csrf = CSRFProtect(app)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=[RATE_LIMITS.get('chat', '20 per hour')],
    storage_uri="memory://"
)

# Initialize Talisman for security headers
talisman = Talisman(
    app,
    force_https=FORCE_HTTPS,
    content_security_policy=CSP,
    content_security_policy_nonce_in=['script-src'],
    strict_transport_security=True,
    strict_transport_security_max_age=31536000,
)


# ============================================================================
# System prompts are now loaded from config/prompts/
# ============================================================================
# SYSTEM_PROMPTS imported from config.prompts at top of file


# ============================================================================
# SECURITY & VALIDATION FUNCTIONS
# ============================================================================

def sanitize_text(text):
    """
    Sanitize user input to prevent XSS attacks.
    Uses bleach to strip potentially dangerous HTML/JS.
    """
    if not text:
        return ""
    # Allow no HTML tags, strip everything
    return bleach.clean(text, tags=[], strip=True)


def validate_chat_message(message):
    """
    Validate chat message input.
    Returns: (is_valid, error_message)
    """
    if not message or not isinstance(message, str):
        return False, "Nachricht darf nicht leer sein."

    # Strip whitespace
    message = message.strip()

    # Check length
    if len(message) < MIN_CHAT_MESSAGE_LENGTH:
        return False, "Nachricht ist zu kurz."

    if len(message) > MAX_CHAT_MESSAGE_LENGTH:
        return False, f"Nachricht ist zu lang (max {MAX_CHAT_MESSAGE_LENGTH} Zeichen)."

    return True, None


def validate_questionnaire_answers(answers, expected_count):
    """
    Validate questionnaire answers.
    Returns: (is_valid, error_message)
    """
    if not isinstance(answers, dict):
        return False, "Ungültige Daten."

    # Check count
    if len(answers) != expected_count:
        return False, f"Erwartete {expected_count} Antworten, erhalten {len(answers)}."

    # Validate each answer
    for q_id, value in answers.items():
        # Check question ID is integer
        if not isinstance(q_id, int):
            return False, "Ungültige Fragen-ID."

        # Check value is in valid range
        if value not in VALID_SCALE_VALUES:
            return False, f"Ungültiger Wert: {value}. Muss zwischen 1 und 7 sein."

    return True, None


def check_session_message_limit():
    """
    Check if the session has exceeded the message limit.
    Returns: (is_within_limit, error_message)
    """
    message_count = len(session.get('messages', []))
    if message_count >= MAX_MESSAGES_PER_SESSION * 2:  # *2 because includes both user and assistant
        logger.warning(f"Session {session.get('session_id')} exceeded message limit")
        return False, "Du hast die maximale Anzahl an Nachrichten für diese Session erreicht."

    return True, None


def validate_session_id(session_id):
    """
    Validate session ID format (UUID).
    Returns: bool
    """
    if not session_id or not isinstance(session_id, str):
        return False

    try:
        uuid.UUID(session_id)
        return True
    except ValueError:
        return False


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    """Handle CSRF errors."""
    logger.warning(f"CSRF error: {e.description}")
    return jsonify({'error': 'Sicherheitsvalidierung fehlgeschlagen. Bitte lade die Seite neu.'}), 400


@app.errorhandler(429)
def handle_rate_limit(e):
    """Handle rate limit errors."""
    logger.warning(f"Rate limit exceeded: {request.remote_addr}")
    return jsonify({'error': 'Zu viele Anfragen. Bitte warte einen Moment und versuche es erneut.'}), 429


@app.errorhandler(413)
def handle_request_too_large(e):
    """Handle request too large errors."""
    logger.warning(f"Request too large from: {request.remote_addr}")
    return jsonify({'error': 'Anfrage ist zu groß.'}), 413


@app.errorhandler(500)
def handle_internal_error(e):
    """Handle internal server errors."""
    logger.error(f"Internal error: {str(e)}")
    return jsonify({'error': 'Ein interner Fehler ist aufgetreten. Bitte versuche es erneut.'}), 500


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_or_create_session_id():
    """Get existing session ID or create new one."""
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
    return session['session_id']


def initialize_chat_session():
    """Initialize chat-related session variables."""
    if 'messages' not in session:
        session['messages'] = []
    if 'current_state' not in session:
        session['current_state'] = 'intake'
    if 'interaction_count' not in session:
        session['interaction_count'] = 0
    if 'session_completed' not in session:
        session['session_completed'] = False


def check_for_state_transition(message):
    """
    Check if AI message contains a state transition marker.
    Returns: (cleaned_message, new_state or None)
    """
    pattern = r'\[TRANSITION:(\w+)\]'
    match = re.search(pattern, message)

    if match:
        new_state = match.group(1)
        cleaned_message = re.sub(pattern, '', message).strip()
        return cleaned_message, new_state
    return message, None


def get_ai_response(user_message):
    """
    Get AI response using Claude API with state machine logic.
    Returns: (response_text, new_state or None)
    """
    if not client:
        return "Fehler: AI-Service nicht verfügbar. Bitte kontaktiere den Administrator.", None

    # Get current state and build system prompt with prompt caching
    current_state = session.get('current_state', 'intake')
    system_prompt_text = SYSTEM_PROMPTS.get(current_state, SYSTEM_PROMPTS['intake'])

    # Add interaction count to strategies prompt
    if current_state == 'strategies':
        interaction_count = session.get('interaction_count', 0)
        system_prompt_text = system_prompt_text.format(interaction_count=interaction_count)

    # Convert to array format with cache_control for prompt caching
    system_prompt = [{
        "type": "text",
        "text": system_prompt_text,
        "cache_control": {"type": "ephemeral"}
    }]

    # Build messages for API
    messages = []
    for msg in session.get('messages', []):
        messages.append({
            "role": msg['role'],
            "content": msg['content']
        })

    # Add current user message
    messages.append({
        "role": "user",
        "content": user_message
    })

    # Add cache_control to second-to-last message to cache conversation history
    # This caches everything except the current user message
    if len(messages) >= 2:
        messages[-2]["cache_control"] = {"type": "ephemeral"}

    try:
        # Call Claude API
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system=system_prompt,
            messages=messages
        )

        ai_message = response.content[0].text

        # Log cache performance metrics
        usage = response.usage
        cache_creation = getattr(usage, 'cache_creation_input_tokens', 0)
        cache_read = getattr(usage, 'cache_read_input_tokens', 0)
        input_tokens = getattr(usage, 'input_tokens', 0)

        session_id = session.get('session_id', 'unknown')
        logger.info(
            f"Session {session_id} - Cache metrics: "
            f"created={cache_creation}, "
            f"read={cache_read}, "
            f"input={input_tokens}, "
            f"total_input={cache_creation + cache_read + input_tokens}, "
            f"state={current_state}"
        )

        # Check for state transition
        cleaned_message, new_state = check_for_state_transition(ai_message)

        return cleaned_message, new_state

    except Exception as e:
        logger.error(f"Error in get_ai_response: {str(e)}")
        return f"Fehler bei der AI-Antwort: {str(e)}", None


# ============================================================================
# ROUTES
# ============================================================================

@app.route('/')
def welcome():
    """Welcome / Landing page."""
    get_or_create_session_id()
    return render_template('welcome.html')


@app.route('/pre-questionnaire')
def pre_questionnaire():
    """Pre-questionnaire page."""
    get_or_create_session_id()
    questions = get_pre_questionnaire()
    return render_template('pre_questionnaire.html', questions=questions)


@app.route('/api/save-pre-questionnaire', methods=['POST'])
@limiter.limit(RATE_LIMITS['save_questionnaire'])
def save_pre_q():
    """API endpoint to save pre-questionnaire data."""
    session_id = get_or_create_session_id()

    # Validate session ID
    if not validate_session_id(session_id):
        logger.warning(f"Invalid session ID: {session_id}")
        return jsonify({'error': 'Ungültige Session'}), 400

    data = request.json
    if not data:
        return jsonify({'error': 'Keine Daten empfangen'}), 400

    # Convert "q1" keys to integer question IDs
    answers = {}
    try:
        for key, value in data.items():
            if key.startswith('q'):
                question_id = int(key[1:])  # Remove 'q' prefix
                answers[question_id] = int(value)  # Ensure value is integer
    except (ValueError, TypeError) as e:
        logger.warning(f"Invalid questionnaire data format: {e}")
        return jsonify({'error': 'Ungültiges Datenformat'}), 400

    # Validate answers
    is_valid, error_msg = validate_questionnaire_answers(answers, PRE_QUESTIONNAIRE_COUNT)
    if not is_valid:
        logger.warning(f"Invalid questionnaire answers: {error_msg}")
        return jsonify({'error': error_msg}), 400

    # Save to JSON using existing utility
    try:
        save_pre_questionnaire(session_id, answers)
        logger.info(f"Pre-questionnaire saved for session {session_id}")
        return jsonify({'status': 'success'})
    except Exception as e:
        logger.error(f"Error saving pre-questionnaire: {e}")
        return jsonify({'error': 'Fehler beim Speichern'}), 500


@app.route('/chat')
def chat():
    """Chat interface."""
    session_id = get_or_create_session_id()
    initialize_chat_session()

    # Add welcome message if chat is empty
    if not session.get('messages'):
        welcome_msg = "Hallo! Ich bin hier, um dir zu helfen, deine Prokrastination zu verstehen und zu überwinden. Erzähl mir: Welche Aufgabe schiebst du gerade vor dir her?"
        session['messages'] = [{
            'role': 'assistant',
            'content': welcome_msg
        }]

    return render_template(
        'chat.html',
        messages=session.get('messages', []),
        state=session.get('current_state', 'intake'),
        session_completed=session.get('session_completed', False)
    )


@app.route('/api/chat', methods=['POST'])
@limiter.limit(RATE_LIMITS['chat'])
def chat_api():
    """Streaming chat endpoint using Server-Sent Events (SSE)."""
    session_id = get_or_create_session_id()
    initialize_chat_session()

    # Validate session ID
    if not validate_session_id(session_id):
        logger.warning(f"Invalid session ID in chat: {session_id}")
        return jsonify({'error': 'Ungültige Session'}), 400

    # Check message limit
    is_within_limit, limit_error = check_session_message_limit()
    if not is_within_limit:
        return jsonify({'error': limit_error}), 429

    # Get and validate message
    data = request.json
    if not data:
        return jsonify({'error': 'Keine Daten empfangen'}), 400

    user_message = data.get('message', '')

    # Validate message
    is_valid, validation_error = validate_chat_message(user_message)
    if not is_valid:
        logger.warning(f"Invalid chat message: {validation_error}")
        return jsonify({'error': validation_error}), 400

    # Sanitize message
    user_message = sanitize_text(user_message.strip())

    # Add user message to history
    session['messages'].append({
        'role': 'user',
        'content': user_message
    })

    # Increment interaction count for strategies state
    current_state = session.get('current_state', 'intake')
    if current_state == 'strategies':
        session['interaction_count'] = session.get('interaction_count', 0) + 1

    def generate():
        """Generator function for SSE stream."""
        try:
            if not client:
                logger.error("Anthropic client not available")
                yield f"data: {json.dumps({'type': 'error', 'message': GENERIC_API_ERROR_MESSAGE})}\n\n"
                return

            # Build system prompt with prompt caching
            system_prompt_text = SYSTEM_PROMPTS.get(current_state, SYSTEM_PROMPTS['intake'])
            if current_state == 'strategies':
                interaction_count = session.get('interaction_count', 0)
                system_prompt_text = system_prompt_text.format(interaction_count=interaction_count)

            # Convert to array format with cache_control for prompt caching
            system_prompt = [{
                "type": "text",
                "text": system_prompt_text,
                "cache_control": {"type": "ephemeral"}
            }]

            # Build messages for API
            messages = []
            for msg in session.get('messages', []):
                messages.append({
                    "role": msg['role'],
                    "content": msg['content']
                })

            # Add cache_control to second-to-last message to cache conversation history
            # This caches everything except the current user message
            if len(messages) >= 2:
                # Add cache_control as a top-level key (not inside content)
                messages[-2]["cache_control"] = {"type": "ephemeral"}

            # Stream from Claude API
            full_response = ""
            with client.messages.stream(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                system=system_prompt,
                messages=messages
            ) as stream:
                for text in stream.text_stream:
                    full_response += text
                    # Send each chunk as SSE
                    yield f"data: {json.dumps({'text': text})}\n\n"

                # Get usage metrics after stream completes
                final_message = stream.get_final_message()
                usage = final_message.usage

                # Log cache performance metrics
                cache_creation = getattr(usage, 'cache_creation_input_tokens', 0)
                cache_read = getattr(usage, 'cache_read_input_tokens', 0)
                input_tokens = getattr(usage, 'input_tokens', 0)

                logger.info(
                    f"Session {session_id} - Cache metrics: "
                    f"created={cache_creation}, "
                    f"read={cache_read}, "
                    f"input={input_tokens}, "
                    f"total_input={cache_creation + cache_read + input_tokens}, "
                    f"state={current_state}"
                )

            # Check for state transition
            cleaned_message, new_state = check_for_state_transition(full_response)

            # Store first AI response in session
            session['messages'].append({
                'role': 'assistant',
                'content': cleaned_message
            })
            session.modified = True

            # Handle state transition with auto-continuation
            if new_state:
                # Update state
                session['current_state'] = new_state
                if new_state == 'strategies':
                    session['interaction_count'] = 0
                elif new_state == 'completion':
                    session['session_completed'] = True
                    mark_chat_complete(session_id)

                session.modified = True

                # AUTO-CONTINUATION: Generate second response in new state
                logger.info(f"Auto-continuation: Generating response in new state '{new_state}'")

                # Build new system prompt for the transitioned state
                new_system_prompt_text = SYSTEM_PROMPTS.get(new_state, SYSTEM_PROMPTS['intake'])
                if new_state == 'strategies':
                    interaction_count = session.get('interaction_count', 0)
                    new_system_prompt_text = new_system_prompt_text.format(interaction_count=interaction_count)

                # Convert to array format with cache_control
                new_system_prompt = [{
                    "type": "text",
                    "text": new_system_prompt_text,
                    "cache_control": {"type": "ephemeral"}
                }]

                # Build messages including the first response
                continuation_messages = []
                for msg in session.get('messages', []):
                    continuation_messages.append({
                        "role": msg['role'],
                        "content": msg['content']
                    })

                # Add cache_control to second-to-last message
                if len(continuation_messages) >= 2:
                    continuation_messages[-2]["cache_control"] = {"type": "ephemeral"}

                # Stream second response (continuation in new state)
                continuation_response = ""
                with client.messages.stream(
                    model="claude-sonnet-4-20250514",
                    max_tokens=1024,
                    system=new_system_prompt,
                    messages=continuation_messages
                ) as stream:
                    for text in stream.text_stream:
                        continuation_response += text
                        # Send continuation chunks as SSE
                        yield f"data: {json.dumps({'text': text})}\n\n"

                    # Get usage metrics for continuation
                    final_continuation = stream.get_final_message()
                    continuation_usage = final_continuation.usage

                    # Log continuation cache metrics
                    logger.info(
                        f"Session {session_id} - Continuation cache metrics: "
                        f"created={getattr(continuation_usage, 'cache_creation_input_tokens', 0)}, "
                        f"read={getattr(continuation_usage, 'cache_read_input_tokens', 0)}, "
                        f"input={getattr(continuation_usage, 'input_tokens', 0)}, "
                        f"state={new_state}"
                    )

                # Store continuation response in session
                session['messages'].append({
                    'role': 'assistant',
                    'content': continuation_response
                })
                session.modified = True

                # Prepare final metadata (after continuation)
                metadata = {
                    'type': 'metadata',
                    'full_text': cleaned_message + " " + continuation_response,
                    'new_state': new_state,
                    'session_completed': new_state == 'completion',
                    'auto_continued': True
                }

            else:
                # No transition - prepare metadata normally
                metadata = {
                    'type': 'metadata',
                    'full_text': cleaned_message,
                    'new_state': None,
                    'session_completed': False,
                    'auto_continued': False
                }

            # Send final metadata
            yield f"data: {json.dumps(metadata)}\n\n"
            yield f"data: [DONE]\n\n"

        except Exception as e:
            logger.error(f"Chat API error for session {session_id}: {str(e)}")
            error_data = {'type': 'error', 'message': GENERIC_API_ERROR_MESSAGE}
            yield f"data: {json.dumps(error_data)}\n\n"

    return Response(generate(), mimetype='text/event-stream')


@app.route('/post-questionnaire')
def post_questionnaire():
    """Post-questionnaire page."""
    session_id = get_or_create_session_id()
    questions = get_post_questionnaire()
    return render_template('post_questionnaire.html', questions=questions)


@app.route('/api/save-post-questionnaire', methods=['POST'])
@limiter.limit(RATE_LIMITS['save_questionnaire'])
def save_post_q():
    """API endpoint to save post-questionnaire data."""
    session_id = get_or_create_session_id()

    # Validate session ID
    if not validate_session_id(session_id):
        logger.warning(f"Invalid session ID: {session_id}")
        return jsonify({'error': 'Ungültige Session'}), 400

    data = request.json
    if not data:
        return jsonify({'error': 'Keine Daten empfangen'}), 400

    # Convert "q1" keys to integer question IDs
    answers = {}
    try:
        for key, value in data.items():
            if key.startswith('q'):
                question_id = int(key[1:])
                answers[question_id] = int(value)  # Ensure value is integer
    except (ValueError, TypeError) as e:
        logger.warning(f"Invalid questionnaire data format: {e}")
        return jsonify({'error': 'Ungültiges Datenformat'}), 400

    # Validate answers
    is_valid, error_msg = validate_questionnaire_answers(answers, POST_QUESTIONNAIRE_COUNT)
    if not is_valid:
        logger.warning(f"Invalid post-questionnaire answers: {error_msg}")
        return jsonify({'error': error_msg}), 400

    # Save to JSON using existing utility
    try:
        save_post_questionnaire(session_id, answers)
        logger.info(f"Post-questionnaire saved for session {session_id}")
        return jsonify({'status': 'success'})
    except Exception as e:
        logger.error(f"Error saving post-questionnaire: {e}")
        return jsonify({'error': 'Fehler beim Speichern'}), 500


@app.route('/thank-you')
def thank_you():
    """Thank you page."""
    return render_template('thank_you.html')


@app.route('/_health')
@limiter.limit(RATE_LIMITS['health_check'])
def health_check():
    """Health check endpoint for Railway monitoring."""
    return jsonify({
        'status': 'healthy',
        'service': 'procrastination-agent',
        'version': '3.0-flask-secured'
    }), 200


# ============================================================================
# RUN SERVER
# ============================================================================

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🎉 Prokrastinations-Agent - Flask Version")
    print("="*70)
    print("\n📍 Server running at: http://localhost:8501")
    print("✨ Perfect HTML rendering with zero CSS issues!")
    print("\n⌨️  Press Ctrl+C to stop\n")
    print("="*70 + "\n")

    app.run(debug=True, port=8501, host='0.0.0.0')
